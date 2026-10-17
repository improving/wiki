---
title: "David Parnas"
type: "Entity"
description: "Software engineering pioneer whose work on modularity and information hiding underpins the corpus's case for agent isolation and boundary enforcement."
created: '2026-10-17'
updated: '2026-10-17'
tags: [person, software-engineering, modularity, architecture]
sources:
  - "/sources/architecture-drift-at-ai-speed-when-your-agents-dont-respect-boundaries.md"
  - "/sources/decoupling-ai-agent-logic-from-model-providers-the-dispatcher-pattern.md"
  - "/sources/engineering-reliability-into-autonomous-ai-agents.md"
---

# David Parnas

David Parnas is a foundational software engineering researcher, known for information hiding and modular design. This corpus invokes his principles when arguing that AI agents need explicit boundaries and isolation to avoid architecture drift at machine speed.

## Overview

- AI agents take the shortest path to working code, crossing architectural boundaries invisibly.
- Parallel agents without isolation create merge conflicts and entanglement; isolation plus automated boundary enforcement preserves architecture.
- Uncontrolled AI generation can cost 25 to 50 percent of delivery capacity.
- Ten steps at 95% accuracy yield only about 60% end-to-end pipeline reliability, so reliability must be engineered through layered defenses.
- Coupling agent logic to a specific model creates migration costs when models change; a dispatcher routing table makes model selection configuration.

## Related

- [Boundary enforcement](/concepts/boundary-enforcement.md) — automated modularity checks at AI speed
- [state isolation](/concepts/state-isolation.md) — prevents parallel-agent entanglement
- [dispatcher pattern](/concepts/dispatcher-pattern.md) — decouples agent logic from model providers
- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — why per-step accuracy compounds downward
- [Engineering Reliability into Autonomous AI Agents](/sources/engineering-reliability-into-autonomous-ai-agents.md) — primary source
