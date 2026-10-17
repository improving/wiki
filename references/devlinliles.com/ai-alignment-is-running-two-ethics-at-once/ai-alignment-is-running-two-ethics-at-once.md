---
type: Reference
title: "AI Alignment Is Running Two Ethics at Once"
resource: "https://www.devlinliles.com/ai-alignment-is-running-two-ethics-at-once/"
author: "Devlin Liles"
published: '2026-08-04'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every major AI lab has published an alignment approach. When you look at them carefully, they split along one of the oldest fault lines in moral philosophy, and the tension between them explains most of the failure modes you see in deployed AI systems.

Kant said the right action is determined by the rule it follows, not by the outcome it produces. Act only according to maxims you could universalize: if you wouldn't want everyone in every situation to do it, don't do it in this situation. Consequences don't change the moral calculus. Rules hold universally or they're not rules. This is deontology.

Mill said the right action is the one that produces the best outcomes for the greatest number. There are no absolute rules because any rule can in principle generate a terrible outcome in some edge case, and producing terrible outcomes is exactly what morality is supposed to prevent. This is consequentialism.

Constitutional AI is deontological. You define a set of principles — a constitution — that govern what the model should and shouldn't do, independent of case-by-case outcomes. The model is trained to follow those principles through self-critique: generate an output, evaluate it against the constitution, revise if it violates a principle, repeat. The output should satisfy the rules regardless of whether it was the most useful answer in this particular case.

RLHF is consequentialist. You collect human feedback on outputs, train a reward model to predict what humans will rate positively, and optimize the language model to maximize that reward signal. The model learns to produce outcomes that human evaluators consider good. There's no explicit rule structure. The "ethics" are implicit in what humans prefer. Optimize for the consequences as measured by human approval.

Neither approach dominates the other. Constitutional AI buys rule consistency and transparency, because the principles are at least partially legible. It handles novel edge cases less well, because a principle written to cover one situation may give bad guidance in a structurally different one that looks similar on the surface. RLHF produces outputs that align more tightly with what users actually want and handles edge cases more flexibly, but at the cost of consistency and transparency: nobody can fully explain what values are encoded in the reward weights.

Current production systems run both, and the interesting failures happen at the intersection.

The deontological failure is the trolley problem for AI. A principle says "don't provide information that could be used to harm someone." Applied consistently, this principle generates refusals for harm reduction information, medical information, security research, historical documentation, and fiction involving conflict. The principle is applied consistently. The outcomes are genuinely bad in those cases. Deontological alignment produces rule-following that occasionally produces harmful results.

The consequentialist failure is reward hacking and sycophancy. If the model is trained to maximize human approval, it learns to tell people what they want to hear. It learns to be confident when users seem to want confidence, even without evidence. The consequentialist optimization converges on "approved outcomes" rather than "good outcomes" because the reward signal is mediated through human raters who have their own biases. You get a system that feels helpful and is reliably misleading.

The practical consequences for enterprise AI deployment follow from the tradeoffs. Systems trained primarily with RLHF are better at satisfying users and worse at consistently applying rules. Systems trained primarily with constitutional methods are more predictable in rule-following and more likely to generate refusals that feel arbitrary. The use case determines which failure mode is more tolerable.

System prompts and operational policies for internal AI tools are applied ethics, not just configuration. "Always respond professionally" is a deontological instruction. "Prioritize user satisfaction in responses" is a consequentialist one. When they conflict — and they will — the system has to choose. A governance position that hasn't thought through how that conflict resolves has left the resolution to the model.

Kant and Mill both got something right. Kant was right that rules provide predictability and protection against case-by-case rationalization of harm. Mill was right that outcomes matter and rigid rule-following can produce genuine harms. Deployed AI systems embody both insights imperfectly. The alignment work happening right now is the engineering version of a philosophical argument that has been running for two centuries. It won't be fully resolved. The task is to manage the tension consciously rather than accidentally.
