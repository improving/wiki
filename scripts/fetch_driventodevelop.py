#!/usr/bin/env python3
"""
fetch_driventodevelop.py — archive driventodevelop.com blog posts as raw references.

Downloads posts (and their images) from David O'Hara's Ghost blog "Driven To
Develop" into the wiki's references/ area as raw, immutable source material for
later ingestion:

    references/driventodevelop.com/<slug>/<slug>.md      post body as markdown
    references/driventodevelop.com/<slug>/images/*       images referenced by the post

The fetching logic lives in scripts/ghost_blog.py (shared by every Ghost blog);
this file only supplies the site's details. Posts already fetched are skipped,
so it is safe to re-run; run it periodically to pick up new posts.

Note: this site publishes at date-based URLs (/YYYY/MM/DD/<slug>/); the archived
folder uses the final slug segment.

Usage:
  python3 scripts/fetch_driventodevelop.py [--limit N] [--only SLUG] [--force]
                                           [--rss-only] [--dry-run] [--sleep SEC]
                                           [--references DIR]
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ghost_blog import Site, run  # noqa: E402

SITE = Site(
    name="Driven To Develop",
    url="https://driventodevelop.com",
    source_dir="driventodevelop.com",
    default_author="David O'Hara",
    description="David O'Hara's blog, Driven To Develop",
    script_name="fetch_driventodevelop.py",
)

if __name__ == "__main__":
    sys.exit(run(SITE))
