---
title: "AWS"
type: "Entity"
description: "Cloud provider whose Bedrock governance controls and zero-data-retention default exemplify policy outside the prompt."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, governance, enterprise]
sources:
  - "/sources/a-rule-in-the-prompt-is-a-suggestion.md"
  - "/sources/the-competitive-axis-moved-to-governance.md"
---

# AWS

AWS appears in this corpus as an enterprise cloud provider whose agent and model-serving controls are cited as examples of [runtime governance](/concepts/runtime-governance.md) — enforcement that sits outside the agent's prompt. The posts treat its governance posture as evidence that the competitive axis for AI platforms has shifted.

## Overview

- One post reports that Bedrock AgentCore Policy enforces rules in Cedar outside the agent's prompt, contrasting with prompt-based rules that passed only 82.5% of 600 runs.
- The other notes AWS made zero data retention the default on [Amazon Bedrock](/entities/amazon-bedrock.md) for all customers.
- Together they argue the axis of competition moved from raw capability to governance credentials as frontier benchmark scores converged.

## Key Claims

- Rules in a prompt are suggestions; enforcement must sit at the tool call as steering hooks or gateway policy.
- Steering hooks hit 100% compliance where prompt rules hit 82.5%.
- Top model benchmark scores have compressed to within a point of each other.
- Aviation safety certification foreshadows governance becoming the deciding axis.

## Related

- [Amazon Bedrock](/entities/amazon-bedrock.md) — the platform carrying these controls
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — the enforcement model cited
- [Policy as Code](/concepts/policy-as-code.md) — Cedar rules expressed as code
- [AI Governance](/concepts/ai-governance.md) — the competitive axis
- [A Rule in the Prompt Is a Suggestion](/sources/a-rule-in-the-prompt-is-a-suggestion.md) — primary source
- [The Competitive Axis Moved to Governance](/sources/the-competitive-axis-moved-to-governance.md) — companion source
