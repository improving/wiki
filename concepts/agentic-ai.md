---
title: "agentic AI"
type: "Concept"
description: "AI that pursues goals across multiple steps and tools rather than answering a single prompt."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, agents, governance]
sources:
  - "/sources/agentic-ai-governance.md"
  - "/sources/agentic-ai-gemini-enterprise-agent-platform-retail-ecommerce.md"
  - "/sources/the-40-percent-problem.md"
  - "/sources/bridging-the-gap-how-a-product-person-learned-to-build-with-agentic-ai.md"
  - "/sources/humans-agents-time-and-tools-redefining-the-future-of-work.md"
  - "/sources/your-ai-governance-policy-is-not-governance.md"
---

# agentic AI

Agentic AI is AI that pursues goals across multiple steps and tools rather than answering a single prompt. The sources define it as autonomous or semi-autonomous software entities that perceive, decide, take actions, and achieve goals, and they warn that its failures compound arithmetically across chained steps — so governance and guardrails must be engineered before autonomy is extended.

## Key Claims

- Gartner defines agentic AI as autonomous or semi-autonomous software entities that perceive, decide, take actions, and achieve goals; agentic AI differs from perception AI by using LLMs to reason and act.
- Gartner projected a 1,445% jump in multi-agent system inquiries between early 2024 and mid-2025, and 40% of agentic AI projects will be canceled by end-2027.
- Agent errors compound: at 95% per step a 10-step chain completes correctly about 60% of the time and a 20-step chain about 36%; at 99% per step those rise to roughly 90% and 82%.
- A single enterprise agentic workflow might complete ~40 discrete actions before a human sees output, so post-hoc review is structurally too slow and governance must run at execution time.
- Cautionary case: in late 2023 a user prompt-injected a Chevrolet dealership's chatbot into "selling" a Tahoe for $1, forcing the bot offline.
- Retail is moving from rigid chatbots to agents that act across OMS, CRM, and ERP, but agents are only as effective as the unified, real-time data foundation beneath them.
- Non-developers can now build with agentic frameworks: a product owner used BMAD to build a working app in an afternoon, feeling scope, cost, and architectural trade-offs firsthand.

## Related

- [AI Governance](/concepts/ai-governance.md) — the controls agentic autonomy requires
- [runtime governance](/concepts/runtime-governance.md) — enforcement at execution time
- [Prompt Injection](/concepts/prompt-injection.md) — the containment problem agents expose
- [agent identity](/concepts/agent-identity.md) — treating agents as scoped non-human principals
- [human-in-the-loop](/concepts/human-in-the-loop.md) — approval reserved for irreversible actions
- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — failures at the boundaries
- [stacking errors](/concepts/stacking-errors.md) — the compounding reliability math
- [AI augmentation](/concepts/ai-augmentation.md) — agents as task automation, not job replacement
