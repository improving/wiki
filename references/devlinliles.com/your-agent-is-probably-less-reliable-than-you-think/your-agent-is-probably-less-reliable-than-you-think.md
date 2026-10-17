---
type: Reference
title: "Your Agent Is Probably Less Reliable Than You Think"
resource: "https://www.devlinliles.com/your-agent-is-probably-less-reliable-than-you-think/"
author: "Devlin Liles"
published: '2026-08-03'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The most dangerous assumption in agentic AI isn't that the model will hallucinate. It's that good component performance means good system performance. It doesn't. And there's a 1940s rocket engineer who proved why.

Robert Lusser was a German aerospace engineer who formalized what became known as Lusser's Law while working with Wernher von Braun in Huntsville after the war. The law: the reliability of a system with components in series is the product of each component's reliability. Multiply the probabilities, don't average them. A chain of components at 95% reliability each isn't a 95% reliable system. It's 0.95 to the power of the number of components. By step 10, you're at 59.9%. By step 14, you've crossed the coin-flip line. Von Neumann applied the same principle to computing in his 1956 paper "Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components." Neither man was thinking about AI agents. But both were describing your production deployment.

An autonomous agent that performs at 98% per step sounds impressive. At 20 sequential steps, a moderately ambitious workflow, the overall reliability is 67%. That means roughly one in three executions fails. If your team is reviewing those failures manually, you've built an expensive rework loop. If they aren't reviewing them, the failed outputs are somewhere downstream in your business.

The math is unforgiving and it doesn't care about model quality. Improve per-step accuracy to 99% and a 20-step chain still succeeds only 82% of the time. The curve bends slowly at the top. The only ways to actually raise system reliability are to shorten the chain, parallelize what you can, or add checkpoints that catch and recover from failures.

This isn't about AI being bad. It's about reliability being a system property, not a component property. Lusser knew it. We keep forgetting it.

The research on agentic pipelines confirms the pattern. Work from the ICML 2025 multi-agent resilience track studied what happens when an inspector agent is placed after each primary agent with an explicit adversarial mandate. Not a checker that verifies syntax; an adversarial reviewer whose job is to find errors. Results showed high recovery rates for errors caught before propagation, with closed-loop adversarial checking neutralizing a substantial fraction of faults that would otherwise compound through the pipeline. The inspector pattern doesn't raise per-step accuracy. It breaks the chain so errors don't propagate.

A second finding from 2025 is subtler and more troubling. Research on long-horizon task execution found that when an LLM's context window contains its own previous errors, it becomes measurably more likely to produce further errors. The model reads its earlier output and treats the established pattern as correct, even when it isn't. Errors don't just survive in the pipeline; they recruit the model to defend them.

The implications for agentic system design follow from the math.

The first is that trust in an autonomous agent requires evaluating the pipeline, not just the model. Vendor benchmarks report per-task accuracy. That number is not the system's reliability. Before any multi-step automation goes live, the compounded reliability at expected chain length needs to be calculated. When that number is uncomfortable, the right response is shortening the chain or adding gates before deployment — not after the first production incident.

The second is about where to place quality gates. The compounding error literature is clear that early gates have disproportionate impact. An error caught at step 2 doesn't propagate through steps 3 through 10. Gates don't need to be human review; they can be structural checks, output schema validation, LLM-as-judge evaluation, or automated test execution. But they need to be real interruption points, not logging steps.

The third is about task decomposition design. Long chains are not just riskier because the math compounds. They're riskier because they create ambiguity about where failures originated. Shorter chains with explicit handoffs create clearer accountability and faster debugging.

The philosophical point underneath this is that reliability is a collective property. No individual component gets credit for system success, and no individual component fully absorbs blame for system failure. The architecture is responsible. When an agentic workflow fails in production, asking "which model made the error?" is almost always the wrong question. Asking "where was the gate that should have caught it?" is almost always the right one.
