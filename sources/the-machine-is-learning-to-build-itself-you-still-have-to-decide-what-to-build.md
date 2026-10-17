---
title: "The Machine Is Learning to Build Itself. You Still Have to Decide What to Build."
type: "Source Summary"
description: "Anthropic's self-building trajectory as a case study in an eight-stage AI maturity model where gates and judgment become the bottleneck."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-machine-is-learning-to-build-itself-you-still-have-to-decide-what-to-build/the-machine-is-learning-to-build-itself-you-still-have-to-decide-what-to-build.md"
---

# The Machine Is Learning to Build Itself. You Still Have to Decide What to Build. — Summary

**Original Source**: `references/devlinliles.com/the-machine-is-learning-to-build-itself-you-still-have-to-decide-what-to-build/the-machine-is-learning-to-build-itself-you-still-have-to-decide-what-to-build.md`

## Summary

Reading [Anthropic](/entities/anthropic.md)'s "AI building AI" numbers as a fire alarm produces bad decisions; reading them as a map of which work moves to machines and in what order produces good ones. The post maps Anthropic's trajectory onto Improving's [AI maturity model](/concepts/ai-maturity-model.md), arguing that amplification relocates rather than removes the bottleneck and that the human role narrows in surface area while growing in leverage.

## Key Claims

- Anthropic engineers now ship roughly 8x as much code per quarter as in 2021–2025, and more than 80% of merged code is written by [Claude](/entities/claude.md); a class of API errors that would have taken four years was fixed in a month, and an optimization task went from a 4x human speedup to 52x.
- Speeding up generation exposed human code review as the bottleneck; Anthropic stood up an automated [Claude Code](/entities/claude-code.md) reviewer that catches about a third of the bugs behind past production incidents before merge.
- Compounding reliability is brutal: at 95% per step, a twenty-step workflow succeeds ~36% of the time and a fifty-step chain ~8%; at 99%, fifty steps still only clear 60%.
- The Stage 4 [quality gates](/concepts/quality-gates.md) — deterministic checks, schema validation, adversarial agents — are what stop one bad step from poisoning the rest.
- The genuinely human work is research taste and judgment: choosing problems, deciding what to trust, and killing dead ends.

## Relevance

Central to [AI maturity model](/concepts/ai-maturity-model.md), [quality gates](/concepts/quality-gates.md), [compounding error](/concepts/compounding-error.md), and [review bottleneck](/concepts/review-bottleneck.md).

## Quality

Practitioner blog post by Devlin Liles. Rich with quoted Anthropic figures and four original visuals; the gate-catch percentage and task-complexity chart are flagged as illustrative, and the post's own notes concede some quoted metrics overstate productivity.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — the case study of a company climbing the maturity stairs
- [Claude](/entities/claude.md) — the model writing the majority of merged code
- [Claude Code](/entities/claude-code.md) — the product whose automated reviewer acts as a Stage 4 control

## Concepts Covered

- [AI maturity model](/concepts/ai-maturity-model.md) — the eight-stage framework organizing the post
- [quality gates](/concepts/quality-gates.md) — the deterministic controls that make imperfect agents safe
- [compounding error](/concepts/compounding-error.md) — per-step reliability raised to the number of steps
- [review bottleneck](/concepts/review-bottleneck.md) — the constraint that amplification relocates

## Related Sources

- [Checking the Math on the $500 Million AI Spend Story](/sources/checking-the-math-on-the-500-million-ai-spend-story.md)
