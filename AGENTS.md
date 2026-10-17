---
type: Manual
title: "Wiki System — Agent Operating Manual"
description: "How agents maintain this OKF v0.1 knowledge bundle: structure, conventions, workflows, logging, and quality standards."
created: '2026-10-17'
updated: '2026-10-17'
tags: [manual, okf, conventions]
---

# Wiki System — Agent Operating Manual

This manual defines how agents maintain the wiki in this repository. The wiki is a self-contained **Open Knowledge Format (OKF) v0.1** knowledge bundle: a directory tree of UTF-8 markdown files with YAML frontmatter. It is readable by humans without tooling, parseable by agents without bespoke SDKs, diffable in version control, and portable across systems and organizations. It depends on no external vault, tool, or corpus.

## Directory Structure

```
[repo root]/                # The OKF bundle root
├── AGENTS.md               # This file — the operating manual
├── CLAUDE.md               # Pointer to this file
├── index.md                # Root index (update as pages are added)
├── log.md                  # Operations log (append during every workflow)
├── overview.md             # High-level synthesis (update during lint)
├── concepts/               # Common nouns: techniques, patterns, ideas
│   └── index.md
├── entities/               # Proper nouns: people, organizations, products, places
│   └── index.md
├── sources/                # Source summaries (one per ingested reference)
│   └── index.md
├── queries/                # Filed question-and-answer sessions
│   └── index.md
└── references/             # READ-ONLY: immutable raw source documents
    └── index.md
```

`references/` holds raw material — articles, papers, transcripts, notes — exactly as captured, before analysis. It may be organized into subdirectories by origin. Never edit a file in `references/`; the wiki's living pages summarize and cross-link them.

### Reserved Filenames

`index.md` and `log.md` are reserved at every level of the tree and are never used for content pages.

## OKF Conformance Rules

1. Every content page (any `.md` file except `index.md` and `log.md`) carries a YAML frontmatter block with a non-empty `type` field.
2. The only `index.md` permitted to carry frontmatter is the root one, which declares `okf_version: "0.1"`.
3. Cross-links are standard markdown links, not wikilinks.
4. Consumers tolerate unknown types, extra frontmatter fields, and broken links — a link whose target does not exist yet is not-yet-written knowledge, not an error. The verification steps in the workflows below keep the link graph healthy anyway.

## File Conventions

### Naming

- **Lowercase with hyphens**: `continuous-integration.md`, `martin-fowler.md`
- **No date prefixes**: wiki pages are timeless; dates live in frontmatter
- **Descriptive stems**: the filename matches the page's primary subject

### YAML Frontmatter (required on every content page)

```yaml
---
title: "Display Title"
type: "Concept"              # or "Entity", "Source Summary", "Query"
description: "One-sentence summary; indexes and previews are built from this."
created: 'YYYY-MM-DD'
updated: 'YYYY-MM-DD'
tags: [tag1, tag2]
sources:                     # Where this page's knowledge came from
  - "/sources/source-summary-slug.md"
---
```

`type` and `description` carry the most weight: index files are built from them, and consumers route on `type`. Update `updated` whenever a page changes meaningfully.

### Cross-Linking (Standard Markdown)

Links between pages are standard markdown links, **bundle-relative**, beginning with `/` and ending in `.md`:

- ✅ `[saga pattern](/concepts/saga-pattern.md)`
- ✅ `[Martin Fowler](/entities/martin-fowler.md)`
- ✅ `[custom display text](/concepts/saga-pattern.md)`
- ❌ `[[concepts/saga-pattern]]` — wikilink syntax is not OKF
- ❌ `(/concepts/saga-pattern)` — link targets always end in `.md`
- ❌ backslash paths — forward slashes on every platform

Relative links (`./neighbor.md`) are used only inside per-directory `index.md` files, which list that directory's own pages. Raw documents in `references/` are cited from source summaries via the `sources` frontmatter field, not as page cross-links.

## Index Formats

### Root index.md

The bundle's front door, and the only `index.md` with frontmatter:

```markdown
---
okf_version: "0.1"
---
# Wiki Index

Last updated: YYYY-MM-DD

## Concepts (N)

* [Title](/concepts/slug.md) - one-line description

## Entities (N)

* [Title](/entities/slug.md) - one-line description

## Sources (N)

* [Title](/sources/slug.md) - one-line description

## Queries (N)

* [Title](/queries/slug.md) - one-line description
```

Ordering: concepts and entities alphabetical; sources newest first. After every ingest, update the counts, the `Last updated` date, and the entries.

### Per-directory index.md

```markdown
# Concepts Index

* [Title](./slug.md) - one-line description
```

## Log Format

`log.md` is a flat chronological operations log, **newest first**. One entry per operation:

```markdown
## [YYYY-MM-DD] operation | Short Title
- Created source summary: sources/slug
- Created N entities: entities/one, entities/two
- Created M concepts: concepts/one
- Updated P existing pages with cross-references
- Verified zero broken links; updated indexes
```

Operations in use: `init`, `ingest`, `create`, `query`, `lint`.

Append an entry at the end of every workflow. The log is the wiki's memory: an agent should be able to reconstruct what happened, and when, by reading it top to bottom.

## Workflows

### 1. Ingest Workflow

**Trigger**: "Ingest [source]", "Add this to the wiki"

0. **Check for duplicates first**
   - Read `log.md` for recent ingests
   - Grep the new source's key terms across `concepts/`, `entities/`, and `sources/`
   - If already ingested: say so, and offer to add supplementary information instead
1. **Read the source** from `references/` — never edit it
2. **Discuss before writing**
   - Summarize what the source says
   - Propose the entities (proper nouns) and concepts (common nouns) to extract
   - Get confirmation before proceeding
3. **Create the source summary**
   - File: `sources/[same-stem-as-the-reference].md`
   - Sections: Summary, Key Claims, Relevance, Quality, Entities Mentioned, Concepts Covered
4. **Create or update entity pages** — one per person, organization, product, or place worth tracking
5. **Create or update concept pages** — one per technique, pattern, or idea
6. **Add cross-references**
   - Source summary ↔ every entity and concept it covers
   - Entities ↔ related concepts, and vice versa
   - Related sources ↔ each other
   - Bidirectional wherever appropriate
7. **Verify links** — every new link's target file exists; key new pages have incoming links from the pages that mention them
8. **Update indexes** — root `index.md` plus the touched per-directory indexes
9. **Log the operation** using the format above
10. **Final check** — no broken links, every new page has `type` frontmatter, no orphaned new pages

### 2. Query Workflow

**Trigger**: a question answerable from wiki knowledge

1. Read `index.md` to locate relevant pages
2. Read the relevant entities, concepts, and sources; follow links outward
3. Synthesize an answer with citations as markdown links
4. Offer to file the Q&A for future reference
5. If filed: write `queries/[descriptive-slug].md` (frontmatter with `type: "Query"`; body with Question, Answer with citations, and Related queries); update the indexes
6. Log the operation

### 3. Lint Workflow

**Trigger**: "Check wiki health", "Lint the wiki"

1. Run the checks:
   - **Broken links** — every page-to-page markdown link resolves to an existing file
   - **Orphans** — pages no other page links to
   - **Dead-ends** — pages with no outgoing links
   - **Stale sources** — source summaries referenced by no entity or concept page
   - **Frontmatter** — every content page has non-empty `type`; flag missing `description`
2. Fix by priority: broken links, then orphans, dead-ends, stale sources
3. Update `overview.md` — refresh Current Focus, Key Themes, and Open Questions
4. Log the operation

## Decision Trees

### Entity vs Concept

- **Entity** (proper noun): a specific person, organization, product, or place → `entities/`
- **Concept** (common noun): a technique, pattern, idea, or category → `concepts/`
- **Test**: if "the" or "a" fits in front of it, it's a concept; if it's a unique name, it's an entity

### New Page vs Update Existing

- **Create new** when no page covers the subject, or a major subtopic deserves its own page
- **Update existing** when a page already covers the subject and the new source adds detail, context, or correction
- When in doubt: check the indexes first, then grep

### Handling Contradictions

When sources disagree:

1. Document both perspectives in the relevant page
2. Cite each claim: "According to [source A](/sources/a.md), X. However, [source B](/sources/b.md) claims Y."
3. Tag the page `conflicting-sources`
4. Note the tension in `overview.md` under Open Questions

## Quality Standards

A good page:

✅ Has complete frontmatter (title, type, description, created, updated, tags, sources)
✅ Opens with a paragraph summarizing the topic
✅ Cites at least one source (two or more as the wiki grows)
✅ Cross-references at least two other pages
✅ Uses structured headings, lists, and tables over freeform prose

Avoid:

❌ Orphans — pages nothing links to
❌ Unsourced claims — always cite
❌ Duplicates — check before creating
❌ Stale pages — update when new sources arrive
❌ Broken links — verify targets exist

## Scope

This wiki is a standalone research and learning knowledge base: research findings, technical knowledge, the people and organizations in the field, and the concepts under study.

It does not hold personal journals, daily notes, meeting notes, or activity tracking. Those live outside this bundle, and nothing here links to them. If a conversation or note reveals a citable idea, capture it as a document in `references/` first, then ingest it normally.

## Examples

### Example Entity Page

```markdown
---
title: "Martin Fowler"
type: "Entity"
description: "Author and speaker on software delivery; popularized continuous integration and refactoring."
created: '2026-10-17'
updated: '2026-10-17'
tags: [author, software-engineering]
sources:
  - "/sources/continuous-integration-explained.md"
---

# Martin Fowler

Author and speaker on software delivery practices.

## Work

Popularized [continuous integration](/concepts/continuous-integration.md); see the summary at [continuous integration explained](/sources/continuous-integration-explained.md).

## Related

- [continuous integration](/concepts/continuous-integration.md)
- [continuous integration explained](/sources/continuous-integration-explained.md)
```

### Example Concept Page

```markdown
---
title: "Continuous Integration"
type: "Concept"
description: "Merging small changes frequently and running automated builds and tests on every merge."
created: '2026-10-17'
updated: '2026-10-17'
tags: [software-engineering, delivery]
sources:
  - "/sources/continuous-integration-explained.md"
---

# Continuous Integration

The practice of merging small changes into a shared mainline frequently, with an automated build and test run on every merge.

## How It Works

1. Every change merges to mainline at least daily
2. An automated pipeline builds and tests the result
3. A broken build is treated as the team's top priority

## Key Claims

- Frequent merges keep integration risk small and continuous
- Automated tests are the safety net that makes frequency affordable

## Related

- [Martin Fowler](/entities/martin-fowler.md) — the practice's best-known advocate
- [continuous integration explained](/sources/continuous-integration-explained.md) — primary source
```

### Example Source Summary

```markdown
---
title: "Continuous Integration Explained"
type: "Source Summary"
description: "An article introducing continuous integration: frequent merges, automated builds, and broken-build discipline."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, software-engineering, delivery]
sources:
  - "references/articles/continuous-integration-explained.md"
---

# Continuous Integration Explained — Summary

**Original source**: `references/articles/continuous-integration-explained.md`

## Summary

Introduces continuous integration as a discipline of frequent merging backed by automation.

## Key Claims

- Integrate at least daily; big-bang merges are the failure mode
- Automated builds and tests gate every merge
- Fix a broken mainline before merging anything else

## Relevance

Foundational for [continuous integration](/concepts/continuous-integration.md).

## Quality

Practitioner article, widely cited. Reasonable quality; no empirical claims.

## Entities Mentioned

- [Martin Fowler](/entities/martin-fowler.md) — author

## Concepts Covered

- [continuous integration](/concepts/continuous-integration.md) — main topic
```
