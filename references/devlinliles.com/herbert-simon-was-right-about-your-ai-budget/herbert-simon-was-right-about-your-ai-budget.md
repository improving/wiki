---
type: Reference
title: "Herbert Simon Was Right About Your AI Budget"
resource: "https://www.devlinliles.com/herbert-simon-was-right-about-your-ai-budget/"
author: "Devlin Liles"
published: '2026-08-01'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every reasoning model ships with a "thinking budget" setting. Most teams either ignore it entirely or set it to maximum and call it a day. Both choices are wrong, and an economist who died in 2001 explains why.

Herbert Simon won the Nobel Prize in Economics in 1978 for a concept he introduced decades earlier: bounded rationality. Classical economic theory assumed that agents optimize. They consider all available information, compute the globally best choice, and act on it. Simon pointed out that no real agent, human or otherwise, actually does this. Real agents have limited information, limited time, and limited computational resources. They don't optimize. They *satisfice*: they search until they find a solution that's good enough given their constraints, then stop.

Simon's insight was empirical, not cynical. He wasn't saying agents are lazy. He was saying the optimization model is a fiction. The cognitive machinery to compute globally optimal decisions doesn't exist in biological systems and is rarely worth building in engineered ones. What actually happens, in firms, in human cognition, and in any resource-constrained system, is that agents establish an aspiration level (a threshold that counts as "good enough") and stop searching when they clear it.

The thinking budget in a reasoning model is a Simon-style satisficing dial, whether the people who designed it called it that or not.

A reasoning model generates intermediate chain-of-thought tokens before producing a final answer. Those tokens consume compute, add latency, and cost money. The budget caps how many tokens the model can spend in that intermediate reasoning phase. The design premise is that constrained reasoning is still useful: a model that thinks for 1,000 tokens will outperform a model that thinks for 0 tokens, even if a model that thinks for 10,000 tokens would be even better.

That premise holds up to a point. Research from 2025 on token-budget-aware reasoning — specifically the TALE-EP work published at ACL 2025 (arXiv:2412.18547) — found that accuracy improvements follow a curve of diminishing returns. Low token budgets produce meaningful lift over no reasoning at all. Past a task-specific ceiling, additional tokens add almost nothing to accuracy while multiplying cost. The TALE-EP approach achieved roughly 80% average accuracy while cutting output token costs by 67% compared to unconstrained chain-of-thought, which is a concrete signal of how much compute the standard approach wastes.

The accuracy plateau is not a model limitation. It's satisficing in action. The problem has been adequately solved. Additional thinking tokens are not finding new solutions. They're traversing ground the model has already covered, generating increasingly redundant intermediate steps. Simon's aspiration level has been met. The agent should stop.

What teams actually do instead is fund the continuation. They pay for all those redundant tokens, at inference time, at scale, across every request. The bill grows; the answer quality doesn't.

The practical governance question this creates is: how is the aspiration level set correctly? Simon's answer would be that it can't be computed analytically. It's calibrated empirically, through experience with the task domain — running enough problems to understand where the accuracy ceiling sits for a specific workload, setting the budget just above that threshold, and building a review process to check whether the threshold has drifted as the workload evolves.

For AI deployments, that translates into running evals at multiple budget tiers before committing. Measuring accuracy at 256, 512, 1024, 2048, and 4096 thinking tokens on a representative sample of real tasks, finding the elbow of the curve, and setting the budget there. Building a quarterly review to verify the elbow hasn't moved is the maintenance discipline the calibration requires.

There's a second Simon implication that teams miss. Bounded rationality says intelligent agents need heuristics: rules of thumb that work well enough in the common case without requiring full search. The thinking budget itself is a heuristic. It's an approximation of the right amount of deliberation. But it's a global approximation, the same budget applied to every request regardless of difficulty.

The better architecture — one that takes Simon seriously — is dynamic budget allocation. Classifying request difficulty before routing, giving easy requests a small budget or no reasoning mode, and giving hard requests more: research on this approach shows that dynamic allocation can match or exceed the accuracy of a fixed-large budget at substantially lower average cost. That's satisficing more precisely, not optimizing.

This is not an academic concern. I work with organizations running hundreds of thousands of AI requests per day. The difference between a thoughtlessly-maxed thinking budget and a calibrated one is real money. Often the difference between a profitable AI deployment and one that the finance team wants to shut down. Simon spent his career arguing that the optimization ideal causes organizations to make worse decisions than satisficing. The same principle applies to the AI deployments those organizations are now running.

"How much thinking is enough?" has no mathematical answer. It's a judgment call about when the cost of another reasoning step exceeds its expected contribution to the answer. Simon called that the aspiration level. That's what a budget policy is, in practice: an operationalized aspiration level for deliberation cost.
