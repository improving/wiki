---
title: "Load the Schema, Don't Paste It"
type: "Source Summary"
description: "Pasting a schema into a prompt creates a second source of truth that drifts; load the canonical schema fresh at assembly time instead."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/load-the-schema-dont-paste-it/load-the-schema-dont-paste-it.md"
---

# Load the Schema, Don't Paste It — Summary

**Original source**: `references/devlinliles.com/load-the-schema-dont-paste-it/load-the-schema-dont-paste-it.md`

## Summary

A procurement extraction agent had the forty-field purchase-order schema pasted directly into its prompt. When the data platform team added three fields and renamed two, the prompt's copy silently went stale, and 15 of 25 test orders failed validation against the current schema. The fix removes the copy entirely: the prompt loads the canonical schema file at assembly time and injects the current field list on every call, so upstream changes propagate with no prompt edits. The author notes the tradeoff — a runtime dependency that fails loudly instead of silently — and the token-cost angle, since a loaded schema grows with the canonical file.

## Key Claims

- At least 15 of 25 purchase orders failed validation after the pasted schema drifted (missing fields and wrong names).
- Loading the canonical schema at assembly time dropped failures to near zero and survived a simulated schema bump with no new drift.
- The tradeoff is a runtime dependency: a missing file fails loudly, while a stale copy fails silently weeks later.
- Loaded schemas make token cost track the canonical file's growth without anyone deciding that tradeoff explicitly.
- The pattern earns its keep when the schema is owned by a different team or system than the prompt.

## Relevance

A concrete case of [schema drift](/concepts/schema-drift.md) in agentic extraction, with a [token cost](/concepts/token-cost.md) implication.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a measured before-and-after on 25 documents and a candid tradeoff section. Caveats: single-case evidence with an illustrative 25-order sample.

## Entities Mentioned

- None.

## Concepts Covered

- [Schema drift](/concepts/schema-drift.md) — the second, unsynchronized copy that diverged from the canonical schema
- [token cost](/concepts/token-cost.md) — loaded schemas grow with the canonical file
