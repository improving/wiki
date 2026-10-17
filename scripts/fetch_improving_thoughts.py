#!/usr/bin/env python3
"""
fetch_improving_thoughts.py — archive the Improving "Thoughts" blog as raw references.

Downloads articles (and their images) from Improving's Thoughts blog into the
wiki's references/ area as raw, immutable source material for later ingestion:

    references/improving.com/<slug>/<slug>.md      article body as markdown
    references/improving.com/<slug>/images/*       images referenced by the article

improving.com is not a Ghost site (static pages backed by Contentful), so this
fetcher carries its own discovery and page-parsing logic and reuses only the
generic helpers in scripts/ghost_blog.py (HTTP, HTML->markdown conversion,
reference writing, index and log maintenance).

Scope: article pages under the English /thoughts/ tree — blog posts
(/thoughts/<slug>/), series parts (/thoughts/top-10-reasons-ai-projects-fail/
<part>/), and newsroom articles (/thoughts/newsroom/<slug>/), which the blog's
own "All Blogs" listing includes. Webinars (event pages with no article body),
category listings, hub pages (e.g. /thoughts/podcast/), and the es-MX / fr-CA
locale variants are excluded; a Thoughts URL that turns out to have no article
body is skipped with a note rather than counted as a failure.

How it works:
  * The Thoughts listing (/thoughts/blogs/all/) enumerates every article,
    newest first; it supplies the ordering (the sitemap's lastmod values are
    all identical, so they cannot).
  * The sitemap (sitemap.xml) enumerates the full archive; URLs it has that
    the listing lacks are appended after it.
  * Each article page's JSON-LD (schema.org BlogPosting) supplies the title,
    author, and publish date; the body is the first div.prose inside
    <article>.
  * Images are downloaded locally and image references rewritten to ./images/.
  * Articles already fetched are skipped, so the script is safe to re-run.

Usage:
  python3 scripts/fetch_improving_thoughts.py [--limit N] [--only SLUG] [--force]
                                              [--sitemap-only] [--dry-run]
                                              [--sleep SEC] [--references DIR]
"""

import argparse
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ghost_blog as gh  # noqa: E402

SITE = gh.Site(
    name="Improving Thoughts",
    url="https://www.improving.com",
    source_dir="improving.com",
    default_author="Improving",
    description="Improving's Thoughts blog — articles and newsroom posts by Improvers",
    script_name="fetch_improving_thoughts.py",
)

# The blog listing: every article, newest first (no pagination).
LISTING_URL = SITE.url + "/thoughts/blogs/all/"

# /thoughts/ pages that are listings or hubs, not articles.
NON_ARTICLE_PAGES = {
    "/thoughts/",
    "/thoughts/blogs/",
    "/thoughts/blogs/all/",
    "/thoughts/newsroom/",
    "/thoughts/webinars/",
}

# Suffix the site appends to page titles ("... | Improving", often behind a
# non-breaking space).
_TITLE_SUFFIX = re.compile(r"[\s\xa0]*\|[\s\xa0]*Improving[\s\xa0]*$")


# ----------------------------------------------------------------------------
# Discovery: blog listing + sitemap
# ----------------------------------------------------------------------------

def in_scope(url):
    """True for article URLs under the English /thoughts/ tree."""
    path = urllib.parse.urlparse(url).path
    if not path.startswith("/thoughts/"):
        return False
    if path.startswith("/thoughts/webinars/") or path.startswith("/thoughts/category/"):
        return False
    return path not in NON_ARTICLE_PAGES


def fetch_listing_posts():
    """Article URLs from the Thoughts listing, newest first; [] on failure."""
    try:
        html_text = gh.http_get(LISTING_URL).decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001 - fall back to sitemap order
        gh.log(f"Listing fetch failed ({exc}); using sitemap order only")
        return []
    posts, seen = [], set()
    for href in re.findall(r'href="(/thoughts/[A-Za-z0-9-]+(?:/[A-Za-z0-9-]+)*/?)"', html_text):
        url = SITE.url + (href if href.endswith("/") else href + "/")
        if in_scope(url) and url not in seen:
            seen.add(url)
            posts.append(url)
    return posts


def fetch_sitemap_posts():
    """(url, lastmod) for every in-scope sitemap URL, via the shared logic."""
    return [p for p in gh.fetch_sitemap_posts(SITE) if in_scope(p["url"])]


def slug_for(url, taken):
    """Archive slug for a Thoughts URL: the final path segment, or the full
    /thoughts/ path hyphen-joined if that segment is already taken."""
    slug = gh.slug_from_url(url)
    if not slug or slug in taken:
        tail = urllib.parse.urlparse(url).path.strip("/")
        slug = re.sub(r"[^a-z0-9-]+", "-", tail.lower()).strip("-")
    return slug


# ----------------------------------------------------------------------------
# Article page parsing
# ----------------------------------------------------------------------------

def json_ld_article(html_text):
    """The schema.org BlogPosting/Article node from the page's JSON-LD."""
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html_text, re.S)
    if not m:
        return {}
    try:
        graph = json.loads(m.group(1)).get("@graph", [])
    except json.JSONDecodeError:
        return {}
    for node in graph:
        if isinstance(node, dict) and node.get("@type") in ("BlogPosting", "Article"):
            return node
    return {}


def extract_article_body(html_text):
    """Inner HTML of the first div.prose inside <article>, or None.

    The first prose div inside the article is the post body; later prose divs
    hold page furniture such as the 'Recent Thought Leadership' section.
    """
    start = html_text.find("<article")
    if start < 0:
        return None
    end = html_text.find("</article>", start)
    article = html_text[start:end if end >= 0 else len(html_text)]
    m = re.search(r'<div\b[^>]*\bclass="[^"]*\bprose\b[^"]*"[^>]*>', article)
    if not m:
        return None
    pos, depth = m.end(), 1
    for tag in re.finditer(r"<(/?)div\b[^>]*>", article[pos:]):
        depth += -1 if tag.group(1) else 1
        if depth == 0:
            return article[pos:pos + tag.start()]
    return None


def parse_post_page(url):
    """Fetch one Thoughts page; return an item dict, or None if no article body."""
    html_text = gh.http_get(url).decode("utf-8", errors="replace")

    node = json_ld_article(html_text)
    title = _TITLE_SUFFIX.sub("", (node.get("headline") or "").strip())
    if not title:
        meta_title = gh.extract_meta(html_text, {"og:title", "twitter:title"}) or ""
        title = _TITLE_SUFFIX.sub("", meta_title).strip()
    published = (node.get("datePublished") or "")[:10]
    if not published:
        published = (gh.extract_meta(html_text, {"article:published_time"}) or "")[:10]

    author = node.get("author")
    if isinstance(author, list):
        author = ", ".join(a.get("name", "") for a in author if isinstance(a, dict))
    elif isinstance(author, dict):
        author = author.get("name", "")
    else:
        author = author or ""

    content = extract_article_body(html_text)
    if content is None:
        return None
    # Normalize protocol-relative and root-relative asset URLs to absolute.
    content = re.sub(r'(src|href)="(//[^"]*)"', r'\1="https:\2"', content)
    content = re.sub(r'src="(/[^"]*)"', r'src="' + SITE.url + r'\1"', content)

    return {
        "url": url,
        "title": title,
        "author": author.strip() or SITE.default_author,
        "published": published,
        "html": content,
    }


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def run(argv=None):
    parser = argparse.ArgumentParser(
        description="Archive improving.com Thoughts blog articles into references/ as raw documents.",
    )
    parser.add_argument("--references", type=Path, default=None,
                        help="references directory (default: <bundle>/references)")
    parser.add_argument("--limit", type=int, default=None, metavar="N",
                        help="fetch at most N new articles (newest first)")
    parser.add_argument("--only", action="append", default=[], metavar="SLUG",
                        help="fetch only this article slug (repeatable)")
    parser.add_argument("--force", action="store_true",
                        help="re-fetch articles that already exist (replaces the folder)")
    parser.add_argument("--sitemap-only", action="store_true",
                        help="skip the blog listing; discover and order via the sitemap")
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would be fetched without writing anything")
    parser.add_argument("--sleep", type=float, default=1.0, metavar="SEC",
                        help="seconds to sleep between HTTP requests (default: 1)")
    args = parser.parse_args(argv)

    gh.SLEEP = max(0.0, args.sleep)
    bundle_root = Path(__file__).resolve().parent.parent
    references_dir = args.references or (bundle_root / "references")
    src_root = references_dir / SITE.source_dir

    listing = [] if args.sitemap_only else fetch_listing_posts()
    if args.sitemap_only:
        gh.log("Thoughts listing: skipped (--sitemap-only)")
    else:
        gh.log(f"Thoughts listing: {len(listing)} article URLs (newest first)")
    sitemap_posts = fetch_sitemap_posts()
    gh.log(f"Sitemap: {len(sitemap_posts)} article URLs in scope")

    # Work list: listing order (newest first), then sitemap-only URLs.
    work, seen = [], set()
    for url in listing:
        work.append(url)
        seen.add(url.rstrip("/"))
    for post in sitemap_posts:
        url = post["url"]
        if url.rstrip("/") not in seen:
            seen.add(url.rstrip("/"))
            work.append(url)

    planned, skipped, taken = [], 0, set()
    for url in work:
        slug = slug_for(url, taken)
        taken.add(slug)
        if args.only and slug not in args.only:
            continue
        slug_dir = src_root / slug
        if slug_dir.exists() and (slug_dir / f"{slug}.md").exists() and not args.force:
            skipped += 1
            continue
        if args.limit is not None and len(planned) >= args.limit:
            continue
        planned.append((url, slug))

    gh.log(f"Planned: {len(planned)} article(s) to fetch, {skipped} already present")

    if args.dry_run:
        for url, slug in planned:
            origin = "listing" if url.rstrip("/") in {u.rstrip("/") for u in listing} else "sitemap"
            print(f"  would fetch [{origin}] {slug}  <{url}>")
        gh.log("Dry run: nothing written.")
        return 0

    src_root.mkdir(parents=True, exist_ok=True)
    fetched, total_images = 0, 0
    failures, non_articles = [], []
    for i, (url, slug) in enumerate(planned, 1):
        try:
            item = parse_post_page(url)
            if item is None:
                non_articles.append(slug)
                gh.log(f"  [{i}/{len(planned)}] {slug} — skipped (no article body)")
                continue
            n_images = gh.write_post(item, src_root / slug, SITE, force=args.force)
            fetched += 1
            total_images += n_images
            gh.log(f"  [{i}/{len(planned)}] {slug} — ok ({n_images} image(s))")
        except Exception as exc:  # noqa: BLE001 - collect and continue
            failures.append((slug, str(exc)))
            gh.log(f"  [{i}/{len(planned)}] {slug} — FAILED: {exc}")

    if fetched:
        count = gh.build_source_index(
            src_root, SITE,
            footer=(
                "Raw articles with local images, fetched from the site's blog "
                f"listing and sitemap by `scripts/{SITE.script_name}`. Re-run "
                "the script to pick up new articles."
            ),
        )
        gh.build_references_index(references_dir)
        entry = [
            f"## [{gh.TODAY}] fetch | {SITE.source_dir} — {fetched} new posts",
            f"- Fetched {fetched} posts ({total_images} images) into references/{SITE.source_dir}/",
            f"- Regenerated references/{SITE.source_dir}/index.md ({count} posts) and references/index.md",
        ]
        if failures:
            entry.append(f"- {len(failures)} post(s) failed: " + ", ".join(s for s, _ in failures))
        if non_articles:
            entry.append("- Skipped page(s) without an article body: " + ", ".join(non_articles))
        gh.prepend_log_entry(bundle_root, "\n".join(entry))
        gh.log("Indexes updated; log.md entry added.")

    gh.log(f"Done: {fetched} fetched, {skipped} skipped, {len(non_articles)} not articles, "
           f"{len(failures)} failed, {total_images} images")
    for slug, err in failures:
        gh.log(f"  FAILED {slug}: {err}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(run())
