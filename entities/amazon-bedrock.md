---
title: "Amazon Bedrock"
type: "Entity"
description: "AWS's managed model service, cited for zero-data-retention defaults and for selling serving-layer engineering."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, managed-inference, governance]
sources:
  - "/sources/the-competitive-axis-moved-to-governance.md"
  - "/sources/what-youre-actually-buying-when-you-choose-managed-inference.md"
---

# Amazon Bedrock

[AWS](/entities/aws.md)'s managed service for accessing foundation models, used in this corpus to illustrate both the governance turn and the real economics of managed inference.

## Overview

Bedrock appears twice: once as a policy decision (zero data retention by default) and once as a product whose value lies in the serving layer rather than the models it hosts.

## Key Claims

- AWS made zero data retention the default on Bedrock for all customers — part of the claim that, as frontier benchmark scores converge to within a point of each other, labs with enterprise and government exposure compete on governance credentials instead.
- The move fits the corpus's [AI governance](/concepts/ai-governance.md) theme, where aviation-style safety certification foreshadows governance becoming the deciding competitive axis.
- As a managed inference offering, Bedrock sells the serving-layer engineering — scheduling, KV-cache management, routing, and power tuning — that self-hosters must otherwise rebuild.
- The corpus argues the serving layer, not the model, usually decides self-hosted inference cost; cited techniques include NEAT cutting reasoning token generation 22–28% and KAIROS cutting agentic serving power draw up to 46%.

## Related

- [AWS](/entities/aws.md) — the platform operating Bedrock
- [Amazon](/entities/amazon.md) — parent company
- [AI Governance](/concepts/ai-governance.md) — the competitive axis the retention default advances
- [What You're Actually Buying When You Choose Managed Inference](/sources/what-youre-actually-buying-when-you-choose-managed-inference.md) — primary source
