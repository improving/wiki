---
type: Reference
title: "The Capabilities Nobody Predicted"
resource: "https://www.devlinliles.com/the-capabilities-nobody-predicted/"
author: "Devlin Liles"
published: '2026-08-05'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Here is a structural problem in AI investment planning: the models available for evaluation today may not predict the behavior of the models that will be deployed in 18 months. Not because they'll be evaluated poorly. Because the capabilities that matter most appear suddenly, non-linearly, and only at scales that can't practically be tested ahead of time.

This is the emergence problem. It's a fundamental challenge for anyone trying to forecast AI capability, plan adoption timelines, or build safety architecture, not a niche research debate.

Emergence, as a concept from complexity science, describes properties that appear in a system without being present in or predictable from its components. Water is wet; individual water molecules are not. The property is real, but it isn't in the parts. You can't extrapolate it from below.

This maps directly onto what researchers observed starting around 2022 in large language models. Tasks that a 10-billion-parameter model performed at near-random chance suddenly jumped to high performance in 100-billion-parameter models. In-context learning appeared, seemingly as a phase transition, at a critical scale threshold. The same pattern held for chain-of-thought reasoning, multi-step arithmetic, and a range of tasks that looked intractable at smaller scales and then weren't.

The 2022 Wei et al. paper, "Emergent Abilities of Large Language Models," documented over 100 tasks with this pattern. Small models performed at chance. Larger models performed substantially above chance. No smooth interpolation connected the two data points.

But the debate didn't end there. Schaeffer et al., in a 2023 NeurIPS paper, challenged the emergence framing directly. Their claim: apparent emergence is often an artifact of discontinuous metrics. When you measure performance with exact-match accuracy, you see a cliff. Switch to a continuous metric that gives partial credit, and the cliff flattens into a curve. On that reading, emergence might be less a property of the model and more a property of how you're measuring it.

The 2025 paper "A Non-Ergodic Framework for Understanding Emergent Capabilities" adds another dimension: emergence may be real but non-ergodic, meaning you can't average across contexts to predict behavior. The model's capability on a specific task might be stable in aggregate and still highly variable for any individual use case. That has direct implications for reliability claims.

If Schaeffer is right that emergence is primarily a measurement artifact, the lesson for practitioners is: build better evals with continuous metrics. Don't let discontinuous benchmarks create the illusion of sudden capability jumps that smooth measurement would have predicted.

If the emergence-as-phase-transition camp is right — and the evidence for at least some genuine non-linear capability gains is hard to dismiss — the lesson is different and more unsettling. Extrapolation from smaller, cheaper models is unreliable for predicting which capabilities will appear at production scale. Your pilot with a small model isn't evidence that the large model will behave proportionally. It's a lower bound, not a forecast.

The safety implication of genuine emergence is severe. Dangerous capabilities could appear without appearing in any smaller model you evaluated. The safety architecture you build on your current model may not cover the next one. This is the precise argument behind Anthropic's Responsible Scaling Policy, which explicitly acknowledges that current evals for dangerous capabilities may not be reliable predictors of future capability jumps.

For enterprise adoption planning, the practical discipline is threefold. Evaluation at scale matters when scale matters. Continuous evaluation metrics are more honest than exact-match benchmarks. And re-evaluation belongs in the model upgrade process as a formal step — when a provider offers a newer, larger model, the behavioral contract with the previous model does not transfer.

The deeper point is about epistemic humility in AI planning. When the field cannot agree on whether the biggest capability jumps in recent AI history were predictable or not, the appropriate investment posture treats your current capability map as incomplete. Emergence doesn't mean AI systems are unpredictable by nature. It means the transition points don't announce themselves. The work is building evaluation and governance structures that can catch a surprise instead of being caught by one.
