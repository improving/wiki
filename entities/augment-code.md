---
title: "Augment Code"
type: "Entity"
description: "An agentic development tool cited in this corpus as an example of the definition, containment, and semantic-error problems in AI-assisted delivery."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agentic-development, tooling, code-generation]
sources:
  - "/sources/agentic-development-is-eleven-problems-not-one.md"
  - "/sources/how-to-stop-an-agent-thats-gone-wrong.md"
  - "/sources/the-defect-is-in-the-definition.md"
  - "/sources/the-error-your-stack-trace-will-never-catch.md"
---

# Augment Code

Augment Code is an agentic development tool that appears in this corpus as a concrete reference point for how AI-assisted delivery fails. The posts use it less as a product review than as an anchor for the claim that most failures trace to task definition and containment, not to raw model capability.

## Overview

The recurring framing is that agentic development is many distinct problems across four layers — foundation, operational, governance, intelligence — and teams fail by solving only one. [Definition of Done](/concepts/definition-of-done.md) and [acceptance criteria](/concepts/acceptance-criteria.md) decide whether an agent runs in the right direction; [human approval points](/concepts/human-approval-points.md) decide whether it can be stopped.

## Key Claims

- Most agentic development failures trace back to definition, not execution.
- A well-defined task states goal, done criteria, out-of-scope work, and assumptions; agents are completion-seeking and expand into undeclared adjacent problems.
- Agentic errors fall into five types — REG, BUG, SEC, INF, and DAT — and [semantic drift](/concepts/semantic-drift.md) accumulates with no exception thrown.
- Reversibility determines where oversight gates belong; approve-before-irreversible is the production default.
- Safeguards split into pre-execution gates (test sufficiency, scope validation, pre-flight checks) and runtime ones ([circuit breakers](/concepts/circuit-breakers.md), timeouts, token budgets).

## Related

- [Definition of Done](/concepts/definition-of-done.md) — the gate most failures skip
- [Semantic drift](/concepts/semantic-drift.md) — the silent failure mode
- [Approval gate](/concepts/human-approval-points.md) — containment by reversibility
- [LangGraph](/entities/langgraph.md) — the framework cited for interrupt-and-resume
- [The Defect Is in the Definition](/sources/the-defect-is-in-the-definition.md) — primary source
