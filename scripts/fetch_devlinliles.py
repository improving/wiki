#!/usr/bin/env python3
"""
fetch_devlinliles.py — archive devlinliles.com blog posts as raw reference documents.

Downloads posts (and their images) from Devlin Liles's Ghost blog "Emptying the
Cup" into the wiki's references/ area as raw, immutable source material for
later ingestion:

    references/devlinliles.com/<slug>/<slug>.md      post body as markdown
    references/devlinliles.com/<slug>/images/*       images referenced by the post

The fetching logic lives in scripts/ghost_blog.py (shared by every Ghost blog);
this file only supplies the site's details. Posts already fetched are skipped,
so it is safe to re-run; run it periodically to pick up new posts.

Usage:
  python3 scripts/fetch_devlinliles.py [--limit N] [--only SLUG] [--force]
                                       [--rss-only] [--dry-run] [--sleep SEC]
                                       [--references DIR]
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ghost_blog import Site, run  # noqa: E402

SITE = Site(
    name="Emptying the Cup",
    url="https://www.devlinliles.com",
    source_dir="devlinliles.com",
    default_author="Devlin Liles",
    description="Devlin Liles's blog, Emptying the Cup",
    script_name="fetch_devlinliles.py",
)

if __name__ == "__main__":
    sys.exit(run(SITE))
