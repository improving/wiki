---
title: "A Rule in the Prompt Is a Suggestion"
type: "Source Summary"
description: "An AWS study shows prompt-stated rules fail one run in six, while code-level steering hooks and gateway policies enforce them reliably."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/a-rule-in-the-prompt-is-a-suggestion/a-rule-in-the-prompt-is-a-suggestion.md"
---

# A Rule in the Prompt Is a Suggestion — Summary

**Original source**: `references/devlinliles.com/a-rule-in-the-prompt-is-a-suggestion/a-rule-in-the-prompt-is-a-suggestion.md`

## Summary

An agent given four rules as plain system-prompt instructions passed only 82.5 percent of 600 test runs in an [AWS](/entities/aws.md) evaluation, breaking a rule in one run out of every six despite the rule being in writing every time. The post uses that study to argue a rule stated in a prompt competes with everything else in context for attention at the moment of action. Code-level steering hooks, which intercept the agent right before a tool call and send it back with a specific correction, hit 100 percent, while rigid graph workflows collapsed on off-script requests.

## Key Claims

- Clare Liguori's AWS evaluation ran five enforcement mechanisms 100 times across six scenarios (600 runs each, 3,000 total) on a library-renewal agent.
- Steering hooks hit 100 percent; an SOP document reached 99.8 percent but spent roughly three times the input tokens per call; the plain prompt and rigid workflow scored 82.5 percent and 80.8 percent; no guidance managed 15.7 percent.
- In 43 percent of the prompt version's failed runs the agent skipped checking whether the book was recalled, despite the rule sitting in its instructions.
- The rigid workflow fell to 2 percent on an off-script scenario because it had no node for "answer the question and stop."
- [AWS](/entities/aws.md) shipped Amazon Bedrock AgentCore Policy to GA on March 3, 2026, enforcing rules in Cedar outside the agent's code and prompt.

## Relevance

Core to [runtime policy enforcement](/concepts/runtime-policy-enforcement.md) and [AI governance](/concepts/ai-governance.md); contrasts prompt-level [prompt engineering](/concepts/prompt-engineering.md) with mechanical checks.

## Quality

Practitioner blog post by Devlin Liles. Strengths: cites a specific, well-documented AWS evaluation with per-mechanism pass rates and a token-cost comparison, and names its sources. Caveats: single vendor study on one narrow agent; the author's own RTCC framing is opinion.

## Entities Mentioned

- [AWS](/entities/aws.md) — published the evaluation and shipped AgentCore Policy

## Concepts Covered

- [runtime-policy-enforcement](/concepts/runtime-policy-enforcement.md) — checking rules where the model must pass through them
- [ai-governance](/concepts/ai-governance.md) — where guardrails actually hold
