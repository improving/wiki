## [2026-10-17] ingest | improving.com — all 511 posts
- Created 511 source summaries: sources/* (Improving's Thoughts blog, 2011–2026, by ~60 authors)
- Created 409 new pages: 185 concepts and 224 entities (each recurring across >=2 posts); applied the recurring threshold for a large corpus, leaving one-off terms in summary prose
- Updated 12 existing pages with new sources (active-listening, ai-maturity-model, definition-of-done, delegation, forward-deployed-engineering, gratitude, growth-mindset, outcome-based-pricing, policy-as-code, psychological-safety, work-life-balance, github)
- Regenerated root index.md plus concepts/, entities/, and sources/ indexes (1,105 summaries, 439 concepts, 430 entities)
- Updated overview.md with the three-corpus synthesis (devlinliles.com, driventodevelop.com, improving.com)
- Verified the link graph: fixed 2 namespace errors; zero broken content links

## [2026-10-17] fetch | improving.com — 511 new posts
- Fetched 511 posts (910 images) into references/improving.com/
- Regenerated references/improving.com/index.md (511 posts) and references/index.md
- Skipped page(s) without an article body: podcast

## [2026-10-17] create | improving.com Thoughts fetcher
- Added scripts/fetch_improving_thoughts.py: archiver for Improving's Thoughts blog (not a Ghost site — Contentful-backed with no RSS; discovers articles via the all-blogs listing + sitemap, parses JSON-LD metadata and the div.prose article body, skips webinars/category/locale/hub pages)
- Reuses the generic helpers in scripts/ghost_blog.py; added an optional footer parameter to build_source_index so the per-source index describes this site's discovery accurately (Ghost callers unchanged)
- Updated AGENTS.md directory tree and Tooling section

## [2026-10-17] ingest | driventodevelop.com — all 240 posts
- Created 240 source summaries: sources/* (driventodevelop.com posts by David O'Hara)
- Created 115 new pages: 65 concepts and 50 entities (each recurring across >=2 posts)
- Updated 28 existing pages with new driventodevelop sources (ai-governance, improving, mckinsey-company, microsoft, openai, gartner, agent-identity, ai-inventory, ...)
- Merged synonyms and mapped overlapping terms to existing pages; normalized 14 over-singularized slugs
- Verified zero broken links, zero orphans, zero dead-ends; regenerated root and per-directory indexes
- Updated overview.md with the two-source synthesis (594 summaries, 460 cross-cutting pages)

## [2026-10-17] fetch | driventodevelop.com — 236 new posts
- Fetched 236 posts (253 images) into references/driventodevelop.com/
- Regenerated references/driventodevelop.com/index.md (240 posts) and references/index.md

## [2026-10-17] create | driventodevelop.com fetcher + shared Ghost module
- Added scripts/ghost_blog.py: shared Ghost-blog archiver (RSS + sitemap discovery, HTML→markdown, image download, index and log maintenance)
- Refactored scripts/fetch_devlinliles.py onto the shared module (CLI and output unchanged)
- Added scripts/fetch_driventodevelop.py for David O'Hara's blog "Driven To Develop"
- Updated AGENTS.md directory tree and Tooling section

## [2026-10-17] fetch | driventodevelop.com — 1 new posts
- Fetched 1 posts (2 images) into references/driventodevelop.com/
- Regenerated references/driventodevelop.com/index.md (4 posts) and references/index.md

## [2026-10-17] fetch | driventodevelop.com — 1 new posts
- Fetched 1 posts (1 images) into references/driventodevelop.com/
- Regenerated references/driventodevelop.com/index.md (4 posts) and references/index.md

## [2026-10-17] fetch | driventodevelop.com — 3 new posts
- Fetched 3 posts (3 images) into references/driventodevelop.com/
- Regenerated references/driventodevelop.com/index.md (3 posts) and references/index.md

## [2026-10-17] create | Codify large-ingest curation rules in AGENTS.md
- Added "Curating the Vocabulary (large ingests)" decision tree: recurring (>=2 source) threshold, synonym merging, title-matching slugs, later promotion
- Added "Reachability and Orphans" decision tree: index-only reachability is the accepted floor for peripheral source summaries
- Clarified orphan and stale-source checks in the Ingest, Lint, and Quality Standards sections to match

## [2026-10-17] ingest | devlinliles.com — all 354 posts
- Created 354 source summaries: sources/* (one per post, linked to the raw references)
- Created 189 concept pages: concepts/* and 156 entity pages: entities/*
- Extracted taxonomy metadata from every post, consolidated it into a canonical vocabulary, and cross-linked sources ↔ concepts/entities bidirectionally
- Added related-source cross-links for orphaned summaries and the last dead-ends
- Verified zero broken links, zero orphans, zero dead-ends; regenerated root and per-directory indexes
- Updated overview.md with current focus, key themes, and open questions

## [2026-10-17] fetch | devlinliles.com — 343 new posts
- Fetched 343 posts (126 images) into references/devlinliles.com/
- Regenerated references/devlinliles.com/index.md (354 posts) and references/index.md

## [2026-10-17] create | Blog fetch script for devlinliles.com
- Added scripts/fetch_devlinliles.py: archives devlinliles.com posts and images into references/devlinliles.com/<slug>/ via the site's RSS feed and sitemap
- Updated AGENTS.md: scripts/ in the directory tree, new Tooling section, fetch added to log operations

## [2026-10-17] fetch | devlinliles.com — 11 posts (script validation)
- Fetched 11 posts (3 images) into references/devlinliles.com/ while validating the script across the RSS and page-fetch paths
- Fixed a table-conversion bug found during validation (highway-data-getting-started-video)
- Regenerated references/devlinliles.com/index.md and references/index.md

## [2026-10-17] init | Wiki initialized
- Created directory structure: concepts/, entities/, sources/, queries/, references/
- Initialized core files: index.md, log.md, overview.md, AGENTS.md, CLAUDE.md
- Declared OKF v0.1 conformance via okf_version frontmatter in the root index
- Initialized this directory as a git repository
