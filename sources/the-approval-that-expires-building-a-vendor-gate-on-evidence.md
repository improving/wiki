---
title: "The Approval That Expires - Building a Vendor Gate on Evidence"
type: "Source Summary"
description: "A flat vendor allow-list approved stale evidence over 30% of the time; a request-time evidence pipeline with explicit thresholds dropped that to zero."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-approval-that-expires-building-a-vendor-gate-on-evidence/the-approval-that-expires-building-a-vendor-gate-on-evidence.md"
---

# The Approval That Expires - Building a Vendor Gate on Evidence — Summary

**Original source**: `references/devlinliles.com/the-approval-that-expires-building-a-vendor-gate-on-evidence/the-approval-that-expires-building-a-vendor-gate-on-evidence.md`

## Summary

A governance agent answering "can I use this vendor" checked a flat allow-list, so five of twelve vendors whose evidence was more than twelve months stale still read as approved; twenty requests, seven of which should have been denied, were approved against stale evidence at better than thirty percent. The fix is a request-time pipeline that fetches current evidence, checks each artifact against written thresholds, and cites the failed threshold on denial — dropping the stale-evidence approval rate to zero.

## Key Claims

- The allow-list version approved requests against stale evidence at better than a 30% rate across twenty requests.
- A list answers "was this vendor approved" (past tense); the relevant question is "is this vendor still what it was when we approved it."
- The replacement pipeline fetches current evidence at request time and evaluates each artifact against explicit thresholds (e.g., SOC 2 and pen test inside twelve months).
- The gated version dropped the stale-evidence approval rate to zero; a vendor approved yesterday is denied today once its evidence expires.
- SOC 2 auditing practice in 2026 (Bitsight) now expects continuous-monitoring exports, and MCP guidance (NSA, Cloud Security Alliance) pushes hash-pinning and signing tool definitions.

## Relevance

Applies [AI governance](/concepts/ai-governance.md) and [runtime governance](/concepts/runtime-governance.md) to vendor approval.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a clear before/after metric and useful links to audit and MCP guidance. Caveats: a synthetic request set and no integration cost data.

## Entities Mentioned

- [SOC 2 Type II](/entities/soc-2-type-ii.md) — the audit report used as a freshness-gated artifact
- [Cloud Security Alliance](/entities/cloud-security-alliance.md) — cited as pushing hash-pinning and signing of MCP tool definitions
- [Model Context Protocol](/entities/model-context-protocol.md) — the tool ecosystem where the same evidence mechanism extends

## Concepts Covered

- [AI Governance](/concepts/ai-governance.md) — gating vendor use on current evidence rather than a static list
- [runtime governance](/concepts/runtime-governance.md) — decisions made at request time instead of approval time
