---
type: "Manual"
title: "Improving Wiki"
description: "A unified, incrementally growing Open Knowledge Format wiki of Improving's AI thought leadership."
created: '2026-10-17'
updated: '2026-10-17'
tags: [readme, okf, ai, improving]
---

# Improving Wiki

A **unified, incremental discovery wiki of Improving's AI thought leadership**.

This repository gathers the thinking Improving and its leaders publish about AI — how enterprises adopt
agents without losing reliability, accountability, or trust — into one cross-linked, human-readable, and
agent-readable knowledge base. It is not a mirror of any single blog. It is a synthesis: every source is
summarized once, then distilled into reusable **concepts** and **entities** that connect ideas across
authors, years, and publications.

The wiki is built on the **Open Knowledge Format (OKF) v0.1** — a plain directory tree of UTF-8 markdown
files with YAML frontmatter. It needs no database, SDK, or special tooling: it reads in a text editor,
renders on GitHub, diffs cleanly in version control, and is directly consumable by AI agents.

## What's Inside

The bundle currently holds **1,105 source summaries** and **869 cross-linked wiki pages**
(**439 concepts**, **430 entities**), drawn from three blogs:

| Source | Author | Posts | Focus |
| --- | --- | --- | --- |
| [Emptying the Cup](/references/devlinliles.com/index.md) | [Devlin Liles](/entities/devlin-liles.md) | 354 | Agentic software delivery, AI governance, enterprise retrieval, observability, real-time video, and the philosophy and economics underneath. |
| [Driven To Develop](/references/driventodevelop.com/index.md) | [David O'Hara](/entities/david-o-hara.md) | 240 | Leadership, culture, personal development and health, the DFW/Texas AI economy, and the consulting business model. |
| [Improving's Thoughts](/references/improving.com/index.md) | [Improving](/entities/improving.md) (many authors) | 511 | The firm's collective voice: AI in the enterprise, data engineering, platform engineering, cloud, security, delivery practice, UX, and culture. |

The through-line is **AI in the enterprise**: how organizations move AI from experiments into measured
production workflows without giving up reliability or trust. Liles supplies the engineering depth — quality
gates, orchestration, evaluation, retrieval. O'Hara supplies the executive frame — governance economics,
workforce restructuring, and the regional build-out. The Improving corpus adds the delivery-practice layer —
how a services firm packages that thinking for clients.

## Repository Layout

```
├── README.md          # This file
├── AGENTS.md          # The operating manual for agents maintaining the wiki
├── index.md           # Root index — the bundle's front door
├── overview.md        # High-level synthesis of themes and open questions
├── log.md             # Chronological operations log (newest first)
├── concepts/          # Common nouns: techniques, patterns, ideas
├── entities/          # Proper nouns: people, organizations, products, places
├── sources/           # One summary per ingested reference
├── queries/           # Filed question-and-answer sessions
├── references/        # READ-ONLY raw source documents, organized by origin
└── scripts/           # Reusable fetchers that populate references/
```

**Start here:** the [root index](/index.md) lists every page. For orientation, read the
[overview](/overview.md); to see the raw material, browse [references](/references/index.md); to see how the
wiki is maintained, read [AGENTS.md](/AGENTS.md).

## How It Grows

The wiki is **incremental**: it expands as new writing appears, one source at a time, without rebuilding what
is already there.

1. **Fetch** — the scripts in [`scripts/`](/scripts) archive blog posts into `references/`, exactly as
   published, and maintain the per-source indexes. They never edit the raw documents.
2. **Ingest** — the [ingest workflow](/AGENTS.md) in the operating manual summarizes each source, extracts the
   recurring concepts and entities it introduces, and cross-links them to existing pages.
3. **Curate** — for a large corpus, a page is created only when a concept or entity is central to, or recurs
   across, two or more sources. One-off mentions stay in the source summary's prose until a later source
   makes them worth a page. This keeps the concept and entity layers a curated map of what the corpus is
   *about*, rather than a thin page per passing mention.
4. **Log** — every fetch, ingest, query, and lint operation is appended to [`log.md`](/log.md), so the wiki's
   history can be reconstructed from top to bottom.

Because raw sources are immutable and summaries link back to them, the wiki can be re-derived, audited, and
extended without ever losing provenance.

## Navigating the Knowledge

- **By topic** — browse the [concepts index](/concepts/index.md) for the recurring techniques, patterns, and
  ideas the corpus teaches (AI governance, quality gates, platform engineering, retrieval, and more).
- **By who** — browse the [entities index](/entities/index.md) for the people, organizations, products, and
  places that recur.
- **By source** — browse the [sources index](/sources/index.md) for one summary per ingested reference.
- **By question** — filed Q&A sessions live in [`queries/`](/queries/index.md).

Cross-links are standard, bundle-relative markdown links (for example,
[AI governance](/concepts/ai-governance.md)), so the graph stays portable across editors, static site
generators, and agents.

## Contributing

The wiki is maintained by agents and humans following [AGENTS.md](/AGENTS.md). Before adding content, read
that manual: it defines the directory structure, OKF conformance rules, naming and frontmatter conventions,
the ingest/query/lint workflows, and the quality bar. In short — never edit `references/`; summarize it in
`sources/`, distill it into `concepts/` and `entities/`, link bidirectionally, and log the operation.
