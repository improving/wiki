---
title: "Permissions Are Not Tags: The Pre-Filter Problem Nobody Names"
type: "Source Summary"
description: "Permissions are a deterministic hard filter; metadata tags are a probabilistic classifier and should soft-boost, not hard-exclude."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/permissions-are-not-tags-the-pre-filter-problem-nobody-names/permissions-are-not-tags-the-pre-filter-problem-nobody-names.md"
---

# Permissions Are Not Tags: The Pre-Filter Problem Nobody Names — Summary

**Original source**: `references/devlinliles.com/permissions-are-not-tags-the-pre-filter-problem-nobody-names/permissions-are-not-tags-the-pre-filter-problem-nobody-names.md`

## Summary

Access permissions and metadata tags both occupy the pre-search stage of hybrid retrieval, so they get designed alike, but they are different mechanisms. Permissions are a deterministic identity/ACL lookup with one acceptable failure direction, so they must be a hard exclude every time. Tags require an inference (often an LLM self-query classifier) about what a natural-language question implies, so a wrong guess should soft-boost, never hard-exclude, or the system silently drops the right answer.

## Key Claims

- Permissions must run as a hard exclude before relevance scoring; a leaked document is a real incident, while an over-exclusion only costs a worse result — an asymmetry that fixes the design.
- Tags are probabilistic: nothing hands the system a clean tag, so a classifier decides which filters apply, and classifiers are wrong some fraction of the time.
- Hard-excluding on a misclassified tag yields a confidently wrong answer with no visible symptom.
- Soft-boosting costs ranking precision the reranker can clean up instead of costing the answer.
- A filtering/ranking system is only as good as its candidate pool: an internal platform search rollout was gated by only about ten percent of employee profiles having usable data.

## Relevance

Informs [permission pre-filtering](/concepts/permission-pre-filtering.md), [hybrid retrieval](/concepts/hybrid-retrieval.md), and [least privilege](/concepts/least-privilege.md).

## Quality

Practitioner blog post by Devlin Liles. Clear mechanism-level reasoning with two concrete project anecdotes; the "ten percent" figure is a single-case illustration.

## Entities Mentioned

- None.

## Concepts Covered

- [Permission Pre-Filtering](/concepts/permission-pre-filtering.md) — the pre-search eligibility stage this post centers on
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the architecture whose pre-filter stage is the topic
- [Least privilege](/concepts/least-privilege.md) — the deterministic access-control posture permissions enforce

## Related Sources

- [The Architecture of Enterprise AI Retrieval](/sources/the-architecture-of-enterprise-ai-retrieval.md)
