---
title: "Every Stage Logged Green While Acme Corp Split in Two"
type: "Source Summary"
description: "A five-stage contract pipeline logged every stage green while entity resolution silently failed, splitting vendors into duplicate graph nodes."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/every-stage-logged-green-while-acme-corp-split-in-two/every-stage-logged-green-while-acme-corp-split-in-two.md"
---

# Every Stage Logged Green While Acme Corp Split in Two — Summary

**Original source**: `references/devlinliles.com/every-stage-logged-green-while-acme-corp-split-in-two/every-stage-logged-green-while-acme-corp-split-in-two.md`

## Summary

A legal-ops pipeline ingested sixty vendor contracts through parse, extract, resolve, classify, and embed stages. A bug skipped entity resolution for the first batch, yet every stage logged green because green meant only "the function returned without raising." "Acme Corp" and "Acme Corporation" became separate graph nodes, corrupting per-vendor obligation totals. The fix treats each stage as a separate monitored unit, with the resolve stage reporting a resolution rate against a minimum-expected-match threshold before later stages may run.

## Key Claims

- Green carried exactly one meaning — no exception thrown — while whether the output was correct was a separate, unchecked question.
- Duplicate-entity rate reached at least 25% of known name-variant pairs, measured against a ground-truth mapping kept alongside the sixty contracts.
- A monolithic ingest function has no seam where a stage can stop and report that its data does not meet a bar, so contamination that does not throw sails through.
- With staged gates, the same injected bug was caught immediately; the affected batch was held and the duplicate-entity rate dropped to near zero.
- A threshold only sees what it was written to check: it catches a stage that broke completely, not one that ran above threshold but mis-handled individual edge cases.
- Gates cost pipeline latency and operational complexity, worth it only when contamination is expensive to find and unwind downstream.

## Relevance

Informs [quality gates](/concepts/quality-gates.md) and observability practice, especially stage-level health signals versus a single terminal status.

## Quality

Practitioner blog post by Devlin Liles. A concrete single-case experiment with a measured before/after rate; the evidence is one pipeline and an author-constructed ground truth.

## Entities Mentioned

- None.

## Concepts Covered

- [quality gates](/concepts/quality-gates.md) — per-stage health signals that let a stage refuse a bad handoff
