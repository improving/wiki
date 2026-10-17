---
title: "Charles Sanders Peirce"
type: "Entity"
description: "Philosopher whose abduction and type-token distinction underpin how this corpus explains what LLMs actually do."
created: '2026-10-17'
updated: '2026-10-17'
tags: [philosophy, logic, inference]
sources:
  - "/sources/llms-dont-reason-they-hypothesize.md"
  - "/sources/you-are-not-talking-to-an-individual.md"
---

# Charles Sanders Peirce

American philosopher and logician whose two ideas — abductive inference and the type-token distinction — are used across this corpus to describe what large language models actually do.

## Overview

Peirce distinguished three forms of inference: deduction, induction, and abduction, the last being the generation of the most plausible explanation for an observation. One post argues that an LLM's next-token generation is abductive rather than deductive, which is why models score better on abductive tasks than on multi-hop deductive chains and why hallucination is better described as a defeated hypothesis than as random noise.

## Work

Peirce's type-token distinction is applied to model weights as the type and each inference run as a token. Because each run is a stochastic token of that type, continuity and identity must be engineered externally rather than assumed to live inside the model.

## Key Claims

- Abduction (plausible explanation) is distinct from deduction and induction
- LLM generation is most plausibly abductive inference, not deduction
- Type-token: weights are the type, an inference run is a token
- Continuity is a state file read at session start, not a model property

## Related

- [Hallucination](/concepts/hallucination.md) — reframed as a defeated hypothesis
- [agent identity](/concepts/agent-identity.md) — identity as an engineered frame
- [Karl Popper](/entities/karl-popper.md) — adjacent philosophy of conjecture and refutation
- [LLMs Don't Reason — They Hypothesize](/sources/llms-dont-reason-they-hypothesize.md) — primary source
- [You Are Not Talking to an Individual](/sources/you-are-not-talking-to-an-individual.md) — primary source
