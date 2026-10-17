#!/usr/bin/env python3
"""
fetch_devlinliles.py — archive devlinliles.com blog posts as raw reference documents.

Downloads posts (and their images) from Devlin Liles's blog into the wiki's
references/ area as raw, immutable source material for later ingestion:

    references/devlinliles.com/<slug>/<slug>.md      post body as markdown
    references/devlinliles.com/<slug>/images/*       images referenced by the post

How it works:
  * The RSS feed (/rss/) supplies the newest posts with full HTML content.
  * The sitemap (sitemap-posts.xml) enumerates the full archive; posts not in
    the feed are fetched as pages and the article body is extracted from the
    gh-content section.
  * Images are downloaded locally and image references rewritten to ./images/.
  * Posts already fetched are skipped, so the script is safe to re-run; run it
    periodically to pick up new posts. Use --rss-only for a quick check of
    recent posts, --force to re-fetch, --only SLUG to fetch one post.

The script maintains references/devlinliles.com/index.md and the Sources list
in references/index.md, and prepends a `fetch` entry to log.md when it adds
new documents. It never edits existing reference documents unless --force is
given (which re-downloads the post from scratch).

Usage:
  python3 scripts/fetch_devlinliles.py [--limit N] [--only SLUG] [--force]
                                       [--rss-only] [--dry-run] [--sleep SEC]
                                       [--references DIR]

Stdlib only. Polite to the source: identifies itself, sleeps between requests.
"""

import argparse
import re
import shutil
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path

SITE = "https://www.devlinliles.com"
SITE_NAME = "Emptying the Cup"
RSS_URL = SITE + "/rss/"
SITEMAP_URL = SITE + "/sitemap.xml"
SOURCE_DIR = "devlinliles.com"
DEFAULT_AUTHOR = "Devlin Liles"
USER_AGENT = "improving-wiki-references/1.0 (raw source archiver)"

SM_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
RSS_CONTENT = "{http://purl.org/rss/1.0/modules/content/}encoded"
RSS_CREATOR = "{http://purl.org/dc/elements/1.1/}creator"

TODAY = date.today().isoformat()
SLEEP = 1.0


def log(msg):
    print(msg, flush=True)


# ----------------------------------------------------------------------------
# HTTP
# ----------------------------------------------------------------------------

def http_get(url, timeout=30, retries=2):
    """GET a URL with retries; sleeps after each successful request."""
    last_error = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
            time.sleep(SLEEP)
            return data
        except Exception as exc:  # noqa: BLE001 - report whatever failed
            last_error = exc
            if attempt < retries:
                time.sleep(2.0 * (attempt + 1))
    raise RuntimeError(f"GET {url} failed: {last_error}")


# ----------------------------------------------------------------------------
# Site discovery: RSS + sitemap
# ----------------------------------------------------------------------------

def fetch_rss():
    """Return {url-without-trailing-slash: post dict} for the newest RSS items."""
    root = ET.fromstring(http_get(RSS_URL))
    items = {}
    for item in root.findall("./channel/item"):
        link = (item.findtext("link") or "").strip()
        if not link:
            continue
        content = item.findtext(RSS_CONTENT) or item.findtext("description") or ""
        creator = (item.findtext(RSS_CREATOR) or DEFAULT_AUTHOR).strip()
        published = ""
        pub = item.findtext("pubDate")
        if pub:
            try:
                published = parsedate_to_datetime(pub).date().isoformat()
            except Exception:  # noqa: BLE001 - tolerate odd date formats
                published = ""
        items[link.rstrip("/")] = {
            "url": link,
            "title": (item.findtext("title") or "").strip(),
            "author": creator,
            "published": published,
            "html": content,
        }
    return items


def fetch_sitemap_posts():
    """Return all post URLs from the sitemap, newest first."""
    root = ET.fromstring(http_get(SITEMAP_URL))
    if root.tag.endswith("sitemapindex"):
        child_locs = [
            (el.text or "").strip()
            for el in root.iter()
            if el.tag.endswith("}loc") or el.tag == "loc"
        ]
        post_maps = [u for u in child_locs if "sitemap-posts" in u]
    else:
        post_maps = [SITEMAP_URL]

    posts = []
    for pm in post_maps:
        proot = ET.fromstring(http_get(pm))
        for url_el in proot.findall(f"{{{SM_NS}}}url"):
            loc = (url_el.findtext(f"{{{SM_NS}}}loc") or "").strip()
            lastmod = (url_el.findtext(f"{{{SM_NS}}}lastmod") or "").strip()
            if loc:
                posts.append({"url": loc, "lastmod": lastmod})
    posts.sort(key=lambda p: (p["lastmod"], p["url"]), reverse=True)
    return posts


def slug_from_url(url):
    path = urllib.parse.urlparse(url).path.rstrip("/")
    slug = path.rsplit("/", 1)[-1].lower()
    return re.sub(r"[^a-z0-9-]+", "-", slug).strip("-")


# ----------------------------------------------------------------------------
# Post page parsing (for posts not covered by RSS)
# ----------------------------------------------------------------------------

def extract_gh_content(html_text):
    """Extract the article body from the <section class="gh-content ..."> block."""
    m = re.search(r'<section\b[^>]*\bclass="[^"]*\bgh-content\b[^"]*"[^>]*>', html_text)
    if not m:
        return None
    start = m.end()
    depth = 1
    for tag in re.finditer(r"<(/?)section\b[^>]*>", html_text[start:]):
        depth += -1 if tag.group(1) else 1
        if depth == 0:
            return html_text[start:start + tag.start()]
    return None


def extract_meta(html_text, names):
    for m in re.finditer(r"<meta\s+[^>]*>", html_text):
        tag = m.group(0)
        prop = re.search(r'(?:property|name)\s*=\s*"([^"]+)"', tag)
        content = re.search(r'content\s*=\s*"([^"]*)"', tag)
        if prop and content and prop.group(1) in names:
            return content.group(1)
    return None


def parse_post_page(url):
    raw = http_get(url)
    html_text = raw.decode("utf-8", errors="replace")
    content = extract_gh_content(html_text)
    if content is None:
        raise RuntimeError("could not find gh-content section")
    title = extract_meta(html_text, {"og:title", "twitter:title"}) or ""
    published = (extract_meta(html_text, {"article:published_time"}) or "")[:10]
    if not published:
        t = re.search(r'<time\b[^>]*\bdatetime="([^"]+)"', html_text)
        published = t.group(1)[:10] if t else ""
    author_m = re.search(r'class="author-name"[^>]*>\s*(?:<a\b[^>]*>)?([^<]+)', html_text)
    author = author_m.group(1).strip() if author_m else DEFAULT_AUTHOR
    return {
        "url": url,
        "title": title,
        "author": author,
        "published": published,
        "html": content,
    }


# ----------------------------------------------------------------------------
# HTML -> Markdown conversion (Ghost/Koenig subset)
# ----------------------------------------------------------------------------

class MarkdownConverter(HTMLParser):
    """Convert the HTML subset Ghost emits for post bodies into markdown."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.cur = []
        self.images = {}        # remote url -> local filename
        self._used_names = set()
        self.lists = []         # {'ordered', 'n', 'items', 'pending'}
        self._li = None         # (indent, marker) for the open <li>
        self.quote = 0
        self._pre = None        # parts buffer while inside <pre>
        self._pre_lang = ""
        self._links = []        # open <a> hrefs (None for non-links)
        self._skip = 0          # inside <script>/<style>
        self._heading = 0
        self._figure_caption = None
        self._in_caption = False
        self._cap = []
        self._table = None      # {'rows': [(cells, is_header)], 'row', 'row_header', 'cell'}

    # -- helpers ------------------------------------------------------------

    def _inline(self, parts=None):
        buf = parts if parts is not None else self.cur
        text = "".join(buf)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r" ?\n ?", "\n", text)
        return text.strip()

    def _flush(self):
        text = self._inline()
        self.cur = []
        if text:
            self._emit(text)

    def _emit(self, block):
        if not block or not block.strip():
            return
        if self.quote:
            block = "\n".join(("> " + line).rstrip() for line in block.split("\n"))
        if self.lists:
            self.lists[-1]["pending"].append(block)
        else:
            self.blocks.append(block)

    def _open_list(self, ordered):
        self._flush()
        self.lists.append({"ordered": ordered, "n": 0, "items": [], "pending": []})

    def _close_list(self):
        if not self.lists:
            return
        if self._li is not None:
            self._close_li()
        lst = self.lists.pop()
        block = "\n".join(lst["items"])
        self._emit(block)

    def _open_li(self):
        lst = self.lists[-1]
        if lst["pending"]:
            self._close_li()
        lst["n"] += 1
        indent = "    " * (len(self.lists) - 1)
        marker = f'{lst["n"]}. ' if lst["ordered"] else "- "
        self._li = (indent, marker)
        self.cur = []

    def _close_li(self):
        if not self.lists or self._li is None:
            return
        text = self._inline()
        if text:
            self.lists[-1]["pending"].append(text)
        self.cur = []
        pending = self.lists[-1]["pending"]
        self.lists[-1]["pending"] = []
        indent, marker = self._li
        self._li = None
        if not pending:
            return
        out = [indent + marker + pending[0]]
        for line in pending[1:]:
            if line.startswith((" ", "\t")):
                out.append(line)  # already indented (nested list)
            else:
                out.append(indent + " " * len(marker) + line)
        self.lists[-1]["items"].append("\n".join(out))

    def _local_image(self, src):
        if src in self.images:
            return self.images[src]
        name = Path(urllib.parse.urlparse(src).path).name or "image"
        name = urllib.parse.unquote(name)
        candidate = name
        i = 2
        while candidate in self._used_names:
            p = Path(name)
            candidate = f"{p.stem}-{i}{p.suffix}"
            i += 1
        self._used_names.add(candidate)
        self.images[src] = candidate
        return candidate

    def _best_srcset(self, srcset):
        if not srcset:
            return None
        best_url, best_w = None, -1
        for part in srcset.split(","):
            bits = part.strip().split()
            if not bits:
                continue
            w = -1
            if len(bits) > 1 and bits[1].rstrip("wx").isdigit():
                w = int(bits[1].rstrip("wx"))
            if w >= best_w:
                best_url, best_w = bits[0], w
        return best_url

    def _handle_img(self, attrs):
        d = dict(attrs)
        src = d.get("src") or self._best_srcset(d.get("srcset"))
        if not src or src.startswith("data:"):
            return
        alt = re.sub(r"\s+", " ", d.get("alt") or "").replace("[", "(").replace("]", ")")
        local = self._local_image(src)
        self.cur.append(f"\n![{alt}](images/{local})\n")

    # -- parser callbacks ----------------------------------------------------

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1
            return
        if self._skip:
            return
        if self._pre is not None:
            if tag == "code":
                cls = dict(attrs).get("class") or ""
                m = re.search(r"(?:^|\s)language-([\w+-]+)", cls)
                if m and not self._pre_lang:
                    self._pre_lang = m.group(1)
            return
        if self._in_caption and tag != "figcaption":
            return
        if self._table is not None and self._table["cell"] is not None and tag not in ("td", "th"):
            return  # drop inline formatting inside table cells

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._flush()
            self._heading = int(tag[1])
        elif tag == "p":
            self._flush()
        elif tag in ("strong", "b"):
            self.cur.append("**")
        elif tag in ("em", "i"):
            self.cur.append("*")
        elif tag == "code":
            self.cur.append("`")
        elif tag == "a":
            href = dict(attrs).get("href")
            if href and href.startswith("/"):
                href = SITE + href
            if href and not href.startswith(("#", "javascript:")):
                self._links.append(href)
                self.cur.append("[")
            else:
                self._links.append(None)
        elif tag == "img":
            self._handle_img(attrs)
        elif tag == "br":
            self.cur.append("\n")
        elif tag == "ul":
            self._open_list(ordered=False)
        elif tag == "ol":
            self._open_list(ordered=True)
        elif tag == "li":
            if self.lists:
                self._open_li()
        elif tag == "blockquote":
            self._flush()
            self.quote += 1
        elif tag == "pre":
            self._flush()
            self._pre = []
            self._pre_lang = ""
        elif tag == "hr":
            self._flush()
            self._emit("---")
        elif tag == "figure":
            self._flush()
            self._figure_caption = None
        elif tag == "figcaption":
            self._in_caption = True
            self._cap = []
        elif tag == "table":
            self._flush()
            self._table = {"rows": [], "row": None, "row_header": False, "cell": None}
        elif tag == "tr":
            if self._table is not None:
                self._table["row"] = []
                self._table["row_header"] = False
        elif tag in ("td", "th"):
            if self._table is not None and self._table["row"] is not None:
                if tag == "th":
                    self._table["row_header"] = True
                self._table["cell"] = []
        elif tag == "div":
            self._flush()
        # span and unknown tags: transparent

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            if self._skip:
                self._skip -= 1
            return
        if self._skip:
            return
        if self._pre is not None:
            if tag == "pre":
                text = "".join(self._pre).strip("\n")
                if text:
                    self._emit(f"```{self._pre_lang}\n{text}\n```")
                self._pre = None
                self._pre_lang = ""
            return
        if self._in_caption and tag != "figcaption":
            return

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._heading:
            text = self._inline()
            self.cur = []
            if text:
                self._emit("#" * self._heading + " " + text)
            self._heading = 0
        elif tag == "p":
            self._flush()
        elif tag in ("strong", "b"):
            self.cur.append("**")
        elif tag in ("em", "i"):
            self.cur.append("*")
        elif tag == "code":
            self.cur.append("`")
        elif tag == "a":
            href = self._links.pop() if self._links else None
            if href:
                self.cur.append(f"]({href})")
        elif tag == "ul":
            self._close_list()
        elif tag == "ol":
            self._close_list()
        elif tag == "li":
            self._close_li()
        elif tag == "blockquote":
            self.quote -= 1
            self._flush()
        elif tag == "figure":
            self._flush()
            if self._figure_caption:
                self._emit("*" + self._figure_caption + "*")
        elif tag == "figcaption":
            self._figure_caption = self._inline(self._cap)
            self._in_caption = False
        elif tag in ("td", "th"):
            if self._table is not None and self._table["cell"] is not None:
                text = self._inline(self._table["cell"]).replace("|", "\\|")
                if self._table["row"] is not None:
                    self._table["row"].append(text)
                self._table["cell"] = None
        elif tag == "tr":
            t = self._table
            if t is not None and t["row"] is not None:
                if t["row"]:
                    t["rows"].append((t["row"], t["row_header"]))
                t["row"] = None
        elif tag == "table":
            t = self._table
            if t is not None:
                rows = [r for r in t["rows"] if r[0]]
                if rows:
                    header_idx = next((i for i, rh in enumerate(rows) if rh[1]), 0)
                    header = rows[header_idx][0]
                    body = [row for i, (row, _) in enumerate(rows) if i != header_idx]
                    width = max([len(header)] + [len(r) for r in body])
                    header += [""] * (width - len(header))
                    lines = [
                        "| " + " | ".join(header) + " |",
                        "|" + "|".join([" --- "] * width) + "|",
                    ]
                    for r in body:
                        r = r + [""] * (width - len(r))
                        lines.append("| " + " | ".join(r) + " |")
                    self._emit("\n".join(lines))
                self._table = None
        elif tag == "div":
            self._flush()

    def handle_data(self, data):
        if self._skip:
            return
        if self._pre is not None:
            self._pre.append(data)
            return
        if self._in_caption:
            self._cap.append(data)
            return
        if self._table is not None and self._table["cell"] is not None:
            self._table["cell"].append(data)
            return
        if data:
            self.cur.append(re.sub(r"\s+", " ", data))

    def result(self):
        return "\n\n".join(self.blocks).strip()


def html_to_markdown(html_text):
    """Convert post HTML to markdown. Returns (markdown, images {remote: local})."""
    images = {}
    blocks = []
    # Ghost "markdown cards" hold raw markdown between kg-card comments; pass
    # them through verbatim instead of parsing.
    segments = re.split(
        r"(<!--kg-card-begin: markdown-->.*?<!--kg-card-end: markdown-->)",
        html_text,
        flags=re.S,
    )
    for segment in segments:
        if not segment or not segment.strip():
            continue
        if segment.startswith("<!--kg-card-begin: markdown"):
            raw = re.sub(r"^<!--kg-card-begin: markdown-->\s*|\s*<!--kg-card-end: markdown-->$", "", segment)
            if raw.strip():
                blocks.append(raw.strip("\n"))
            continue
        conv = MarkdownConverter()
        conv.feed(segment)
        conv.close()
        md = conv.result()
        if md:
            blocks.append(md)
        images.update(conv.images)
    return "\n\n".join(blocks).strip() + "\n", images


# ----------------------------------------------------------------------------
# Writing reference documents
# ----------------------------------------------------------------------------

def yaml_quote(value):
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        m = re.match(r"([\w-]+):\s*(.*)\s*$", line)
        if m:
            value = m.group(2).strip()
            if value.startswith(('"', "'")) and value.endswith(value[0]) and len(value) >= 2:
                value = value[1:-1]
            fm[m.group(1)] = value
    return fm


def write_post(item, slug_dir, force):
    """Write one post as references/<source>/<slug>/<slug>.md (+ images/)."""
    slug = slug_dir.name
    md, images = html_to_markdown(item["html"])

    # The article body opens with an <h1> repeating the title; the title lives
    # in frontmatter, so drop that heading.
    first_line = md.split("\n", 1)[0].strip()
    title = item["title"] or slug
    if first_line.startswith("# ") and first_line[2:].strip().lower() == title.lower():
        md = md.split("\n", 1)[1].lstrip("\n") if "\n" in md else ""

    if force and slug_dir.exists():
        shutil.rmtree(slug_dir)
    slug_dir.mkdir(parents=True, exist_ok=True)

    image_count = 0
    for remote, local_name in images.items():
        try:
            data = http_get(remote)
            (slug_dir / "images").mkdir(exist_ok=True)
            (slug_dir / "images" / local_name).write_bytes(data)
            image_count += 1
        except Exception as exc:  # noqa: BLE001 - keep the remote URL on failure
            log(f"    ! image failed ({remote}): {exc}")
            md = md.replace(f"](images/{local_name})", f"]({remote})")

    frontmatter = "\n".join([
        "---",
        "type: Reference",
        f"title: {yaml_quote(title)}",
        f"resource: {yaml_quote(item['url'])}",
        f"author: {yaml_quote(item.get('author') or DEFAULT_AUTHOR)}",
        f"published: '{item.get('published') or ''}'",
        f"fetched: '{TODAY}'",
        "tags: [blog, devlinliles.com]",
        "---",
    ])
    body = frontmatter + "\n\n" + md.strip() + "\n"
    (slug_dir / f"{slug}.md").write_text(body, encoding="utf-8")
    return image_count


# ----------------------------------------------------------------------------
# Index maintenance
# ----------------------------------------------------------------------------

SOURCE_DESCRIPTION = f"Devlin Liles's blog, {SITE_NAME}"


def build_source_index(src_root):
    """Regenerate references/devlinliles.com/index.md; returns the post count."""
    entries = []
    for d in sorted(src_root.iterdir()):
        if not d.is_dir():
            continue
        md = d / f"{d.name}.md"
        if not md.exists():
            continue
        fm = read_frontmatter(md)
        entries.append({
            "title": fm.get("title") or d.name,
            "slug": d.name,
            "published": fm.get("published") or "",
        })
    entries.sort(key=lambda e: (e["published"], e["slug"]), reverse=True)

    lines = [
        "# devlinliles.com",
        "",
        SOURCE_DESCRIPTION,
        "",
    ]
    for e in entries:
        pub = f" - published {e['published']}" if e["published"] else ""
        lines.append(f"* [{e['title']}](./{e['slug']}/{e['slug']}.md){pub}")
    if not entries:
        lines.append("* (No posts fetched yet.)")
    lines += [
        "",
        "Raw posts with local images, fetched from the site's RSS feed and "
        "sitemap by `scripts/fetch_devlinliles.py`. Re-run the script to pick "
        "up new posts.",
    ]
    (src_root / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(entries)


def build_references_index(references_dir):
    """Regenerate the Sources list in references/index.md."""
    sources = []
    for d in sorted(references_dir.iterdir()):
        idx = d / "index.md"
        if not d.is_dir() or not idx.exists():
            continue
        desc = d.name
        count = 0
        for line in idx.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s:
                continue
            if s.startswith("# "):
                continue
            if s.startswith("* ") and not s.startswith("* ("):
                count += 1
            elif not s.startswith("* (") and desc == d.name:
                desc = s.rstrip(".")
        sources.append((d.name, desc, count))

    lines = [
        "# References Index",
        "",
        "READ-ONLY: immutable raw source documents, captured exactly as found "
        "and organized by origin. Never edit files here; summarize them in the "
        "[source summaries](/sources/index.md) instead.",
        "",
        "## Sources",
        "",
    ]
    for name, desc, count in sources:
        suffix = f" ({count} documents)" if count else ""
        lines.append(f"* [{name}](./{name}/index.md) - {desc}{suffix}.")
    if not sources:
        lines.append("* (No reference sources yet.)")
    (references_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def prepend_log_entry(bundle_root, text):
    log_path = bundle_root / "log.md"
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    log_path.write_text(
        text.rstrip("\n") + "\n\n" + existing.lstrip("\n"),
        encoding="utf-8",
    )


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main(argv=None):
    global SLEEP
    parser = argparse.ArgumentParser(
        description="Archive devlinliles.com blog posts into references/ as raw documents.",
    )
    parser.add_argument("--references", type=Path, default=None,
                        help="references directory (default: <bundle>/references)")
    parser.add_argument("--limit", type=int, default=None, metavar="N",
                        help="fetch at most N new posts (newest first)")
    parser.add_argument("--only", action="append", default=[], metavar="SLUG",
                        help="fetch only this post slug (repeatable)")
    parser.add_argument("--force", action="store_true",
                        help="re-fetch posts that already exist (replaces the folder)")
    parser.add_argument("--rss-only", action="store_true",
                        help="skip the sitemap; only process posts in the RSS feed")
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would be fetched without writing anything")
    parser.add_argument("--sleep", type=float, default=1.0, metavar="SEC",
                        help="seconds to sleep between HTTP requests (default: 1)")
    parser.add_argument("--timeout", type=int, default=30, metavar="SEC",
                        help="per-request timeout (default: 30)")
    args = parser.parse_args(argv)

    SLEEP = max(0.0, args.sleep)
    bundle_root = Path(__file__).resolve().parent.parent
    references_dir = args.references or (bundle_root / "references")
    src_root = references_dir / SOURCE_DIR

    rss = fetch_rss()
    log(f"RSS feed: {len(rss)} recent posts")

    if args.rss_only:
        sitemap_posts = []
        log("Sitemap: skipped (--rss-only)")
    else:
        sitemap_posts = fetch_sitemap_posts()
        log(f"Sitemap: {len(sitemap_posts)} posts total")

    # Build the work list: sitemap order (newest first), RSS items appended if
    # not already covered (covers the --rss-only case).
    work = []
    seen_urls = set()
    for p in sitemap_posts:
        work.append(p["url"])
        seen_urls.add(p["url"].rstrip("/"))
    for key, item in rss.items():
        if key not in seen_urls:
            work.append(item["url"])

    planned = []
    skipped = 0
    seen_slugs = set()
    for url in work:
        slug = slug_from_url(url)
        if not slug or slug in seen_slugs:
            continue
        seen_slugs.add(slug)
        if args.only and slug not in args.only:
            continue
        slug_dir = src_root / slug
        if slug_dir.exists() and (slug_dir / f"{slug}.md").exists() and not args.force:
            skipped += 1
            continue
        if args.limit is not None and len(planned) >= args.limit:
            continue
        planned.append((url, slug))

    log(f"Planned: {len(planned)} post(s) to fetch, {skipped} already present")

    if args.dry_run:
        for url, slug in planned:
            origin = "rss" if url.rstrip("/") in rss else "page"
            print(f"  would fetch [{origin}] {slug}  <{url}>")
        log("Dry run: nothing written.")
        return 0

    src_root.mkdir(parents=True, exist_ok=True)
    fetched = 0
    total_images = 0
    failures = []
    for i, (url, slug) in enumerate(planned, 1):
        try:
            key = url.rstrip("/")
            if key in rss:
                item = dict(rss[key])
                item["url"] = url
            else:
                item = parse_post_page(url)
            n_images = write_post(item, src_root / slug, force=args.force)
            fetched += 1
            total_images += n_images
            log(f"  [{i}/{len(planned)}] {slug} — ok ({n_images} image(s))")
        except Exception as exc:  # noqa: BLE001 - collect and continue
            failures.append((slug, str(exc)))
            log(f"  [{i}/{len(planned)}] {slug} — FAILED: {exc}")

    if fetched:
        count = build_source_index(src_root)
        build_references_index(references_dir)
        entry = [
            f"## [{TODAY}] fetch | devlinliles.com — {fetched} new posts",
            f"- Fetched {fetched} posts ({total_images} images) into references/{SOURCE_DIR}/",
            f"- Regenerated references/{SOURCE_DIR}/index.md ({count} posts) and references/index.md",
        ]
        if failures:
            entry.append(f"- {len(failures)} post(s) failed: " + ", ".join(s for s, _ in failures))
        prepend_log_entry(bundle_root, "\n".join(entry))
        log(f"Indexes updated; log.md entry added.")

    log(f"Done: {fetched} fetched, {skipped} skipped, {len(failures)} failed, {total_images} images")
    for slug, err in failures:
        log(f"  FAILED {slug}: {err}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
