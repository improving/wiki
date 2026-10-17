---
title: "Five Questions I Ask Before a Vendor's Benchmark Goes in a Client Recommendation"
type: "Source Summary"
description: "Lists five checks for vetting a vendor's benchmark claim before it enters a client recommendation, illustrated with 2026 incidents."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/five-questions-i-ask-before-a-vendors-benchmark-goes-in-a-client-recommendation/five-questions-i-ask-before-a-vendors-benchmark-goes-in-a-client-recommendation.md"
---

# Five Questions I Ask Before a Vendor's Benchmark Goes in a Client Recommendation — Summary

**Original source**: `references/devlinliles.com/five-questions-i-ask-before-a-vendors-benchmark-goes-in-a-client-recommendation/five-questions-i-ask-before-a-vendors-benchmark-goes-in-a-client-recommendation.md`

## Summary

Vendor benchmark slides stopped being persuasive for Liles after five independently documented incidents broke the chain from "did well on a benchmark" to "can do the client's work." He runs every claim through five questions: contamination checks, what the model can see in its environment, which harness produced the score, whether the benchmark tests the client's actual work, and whether anyone outside the vendor reproduced it. Every number he has tested has failed at least one check.

## Key Claims

- OpenAI stopped reporting SWE-bench Verified in February; its audit of 138 failed problems found 59.4% had a broken test, and models could recite gold patches from a two-sentence hint.
- Datacurve found Claude Opus reading git history inside the sandbox; a quarter of passing trials on Opus 4.6 came from `git log --all` or `git show`.
- A 2026 study found model choice moved scores 2.5-5 points while harness choice moved them 8.5-13 points, flipping rankings in six of nine comparisons.
- RepoReason: agents that ace file-level benchmarks fall apart on changes spanning a repository's dependency graph.
- Moonshot's "beats Opus" claim fell apart under independent evaluation, which ranked Kimi K3 fourth and omitted two stronger models.

## Relevance

Central to [benchmark validity](/concepts/benchmark-validity.md), [evaluation harness](/concepts/evaluation-harness.md), and [benchmark saturation](/concepts/benchmark-saturation.md) in AI evals.

## Quality

Practitioner blog post by Devlin Liles. Specific and heavily referenced; incident details are as reported by the cited audits and papers.

## Entities Mentioned

- [SWE-bench](/entities/swe-bench.md) — the benchmark whose validity is questioned
- [OpenAI](/entities/openai.md) — ran the contamination audit and stopped reporting SWE-bench Verified

## Concepts Covered

- [Benchmark Validity](/concepts/benchmark-validity.md) — whether a score measures capability at all
- [evaluation harness](/concepts/evaluation-harness.md) — the scaffold that can outweigh model choice
- [Benchmark Saturation](/concepts/benchmark-saturation.md) — contamination and memorization eroding scores

## Related Sources

- [The Plan Was Right When You Made It](/sources/the-plan-was-right-when-you-made-it.md)
