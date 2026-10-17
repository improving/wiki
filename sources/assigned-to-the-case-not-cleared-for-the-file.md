---
title: "Assigned to the Case, Not Cleared for the File"
type: "Source Summary"
description: "Case-level permission gating leaked privileged documents to staff; splitting visibility from document-level access dropped exposure to zero."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/assigned-to-the-case-not-cleared-for-the-file/assigned-to-the-case-not-cleared-for-the-file.md"
---

# Assigned to the Case, Not Cleared for the File — Summary

**Original source**: `references/devlinliles.com/assigned-to-the-case-not-cleared-for-the-file/assigned-to-the-case-not-cleared-for-the-file.md`

## Summary

A retrieval assistant over legal case files gated everything on one boolean: is this staff member assigned to this case. That check conflates knowing a case exists with being entitled to read a specific document, so a paralegal staffed on a matter could retrieve passages from privileged attorney work-product memos. Measured across twenty paralegal queries, the over-broad exposure rate was 20%. Splitting permission into two independent checks — case visibility and document-level access — dropped it to zero, without changing the similarity scoring or ranking.

## Key Claims

- The system mapped eight staff accounts to ten case files via a single assignment table, with privileged and ordinary documents in the same folders.
- Over-broad exposure rate — a returned passage from a document the user had no content grant to — came back at 20% across twenty paralegal queries.
- The fix checks case visibility and document-level access independently; neither grant may substitute for the other.
- Visibility without access still returns a metadata stub, enough to confirm a document exists without revealing content.
- Splitting into two small named functions makes each unit-testable and prevents degradation back into one combined check.

## Relevance

Informs [permission pre-filtering](/concepts/permission-pre-filtering.md) and [least privilege](/concepts/least-privilege.md) in enterprise retrieval systems handling mixed-sensitivity corpora.

## Quality

Practitioner blog post by Devlin Liles. Concrete, self-reported experiment with a named metric and candid limits; evidence is a small synthetic corpus of ten cases rather than production data.

## Entities Mentioned

- None.

## Concepts Covered

- [Permission Pre-Filtering](/concepts/permission-pre-filtering.md) — resolving permission at the returned record level
- [Least privilege](/concepts/least-privilege.md) — visibility without content access as the governing principle
