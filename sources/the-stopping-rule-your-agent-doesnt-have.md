---
title: "The Stopping Rule Your Agent Doesn't Have"
type: "Source Summary"
description: "Fixed verify-repair round limits waste rounds and can harm valid outputs; a grounded stopping rule helps."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/the-stopping-rule-your-agent-doesnt-have/the-stopping-rule-your-agent-doesnt-have.md"
---

# The Stopping Rule Your Agent Doesn't Have — Summary

**Original source**: `references/devlinliles.com/the-stopping-rule-your-agent-doesnt-have/the-stopping-rule-your-agent-doesnt-have.md`

## Summary

Points out that every coding-agent harness ships a fixed verify-repair round limit nobody measured, and that a July paper ("Verify, Repair, Repeat, or Stop?") puts a number on the gap. With noisy verifiers and imperfect repairers, reported acceptance can keep climbing while true validity falls — repair can damage an already-correct answer that a noisy verifier waves through. A statistically grounded stopping rule (VRR-Stop) both improved correctness and spent far fewer rounds, because most rounds were buying nothing and some were making things worse.

## Key Claims

- Replacing a fixed five-round policy with VRR-Stop improved final true validity by 60.6 percentage points while spending an average of 0.72 repair rounds instead of five.
- Reported acceptance can rise round over round while true validity falls; errors compound because each round is another chance to break something good and for a noisy verifier to miss it.
- VRR-Stop only needs the sign of the expected gain from one more round, estimated from repeated verification votes — a lighter bar than the field assumed self-correction requires.
- When the verifier's discrimination approaches zero, the estimate itself becomes unreliable; VRR-Guard handles this by swapping candidates only when the verification margin clears a real threshold.
- The 60.6-point result comes from a GSM8K stress setting with deliberately elevated noise, not a claim about every production agent.

## Relevance

Informs [compounding error](/concepts/compounding-error.md) in agent loops and the reliability of [model-as-judge](/concepts/model-as-judge.md) graders, arguing that a loop's [evaluation harness](/concepts/evaluation-harness.md) — and the [golden dataset](/concepts/golden-dataset.md) used to check the verifier — must be trustworthy before any stopping policy on top of it means anything.

## Quality

Practitioner blog post by Devlin Liles. Strengths: cites a specific paper with numbers and is careful to bound what those numbers describe. Caveat: single-paper, stress-test evidence, and the author's own reasoning about mapping it to production harnesses.

## Entities Mentioned

- [GSM8K](/entities/gsm8k.md) — the benchmark used in the paper's stress test

## Concepts Covered

- [compounding error](/concepts/compounding-error.md) — how extra repair rounds make things worse
- [model-as-judge](/concepts/model-as-judge.md) — noisy verifiers that misjudge
- [evaluation harness](/concepts/evaluation-harness.md) — the retry/verify machinery being configured
- [golden dataset](/concepts/golden-dataset.md) — held-out known-good/known-bad completions for checking verifier reliability

## Related Sources

- [The Model Knows More Than It's Telling You](/sources/the-model-knows-more-than-its-telling-you.md)
