---
type: Reference
title: "Cost-Adjusted Capacity: When Tokens Stop Converting to Mergeable PRs"
resource: "https://www.devlinliles.com/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs/"
author: "Devlin Liles"
published: '2026-07-17'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most AI coding budgets optimize the wrong variable. They track token spend and model tier as if buying a bigger model and feeding it more tokens reliably produces more shipped software. The evidence says otherwise, and the gap between what benchmarks measure and what actually merges is large enough to model explicitly. This is that model: a calculated framework for cost-adjusted capacity that combines METR's task-completion time horizons with current frontier pricing, and that locates the precise point where additional spend stops converting into mergeable pull requests.

I am going to show the mathematics in full. Every constant is sourced or stated, every derivation is reproducible, and the conclusion is uncomfortable for anyone whose AI strategy is "use the most capable model we can afford."

|Benchmark|Claude Opus 4.6|Claude Sonnet 4.6|What It Measures| |SWE-bench Verified|80.80%|79.60%|Real-world software engineering| |ARC-AGI-2|68.80%|60.40%|Abstract reasoning| |Terminal-Bench 2.0|65.40%|59.00%|Agentic terminal coding| |OSWorld-Verified|72.70%|72.50%|Desktop automation|

## Two datasets, one question

The question is simple to state and hard to answer: for a coding task of a given difficulty, what does it cost to get a *mergeable* pull request out of an AI model, and at what point does spending more stop helping?

Answering it requires two bodies of evidence.

The first is capability as a function of task difficulty. METR's time-horizon work is the cleanest measurement available. METR fits a logistic curve to each model's success rate across more than a hundred software, machine learning, and cybersecurity tasks, where task difficulty is measured by how long a skilled human takes to complete the task. The headline output is the **50% time horizon**: the human-task duration at which the model succeeds half the time. Frontier 50% horizons have doubled roughly every seven months since 2019, accelerating to about a 4.3-month doubling since 2023. As of the May 2026 measurement set, Claude 3.7 Sonnet sits near 59 minutes, GPT-5 near 137 minutes (about two hours seventeen minutes), and Claude Opus 4.5 near 320 minutes. (METR, *Task-Completion Time Horizons of Frontier AI Models*, updated May 8, 2026; METR, *Measuring AI Ability to Complete Long Tasks*, March 2025.)

The second is the gap between passing tests and being mergeable. This is where the capability number lies to you. METR's holistic evaluation found Claude 3.7 Sonnet passed maintainer tests on 38% of real tasks, yet on manual review *none* of the 15 reviewed pull requests were mergeable as-is; fixing them to mergeable averaged 42 minutes, roughly a third of total PR time, lost to test coverage, formatting, documentation, and code-quality gaps (METR, *Towards reconciling slowdown with time horizons*, August 2025). METR's March 2026 follow-up quantified it as a horizon distortion: roughly half of test-passing SWE-bench Verified PRs from mid-2024 through late-2025 agents would not be merged by maintainers, and Claude Sonnet 4.5 showed about a 50-minute time horizon by the automated grader but only about 8 minutes by maintainers. That is a 6.25x overstatement in task length.

Those two datasets, joined, produce a cost-adjusted capacity model.

## The capability curve, stated as math

METR's logistic fit predicts success probability as a function of human task duration t. At t = h₅₀ the expression returns exactly 0.5, by construction. The steepness k comes from METR's empirical finding that the 80% horizon is about five times shorter than the 50% horizon, giving k = 0.861. So the working capability model for any model is P(t) = 1 / (1 + (t/h₅₀)^0.861).

## The mergeability haircut

The automated grader and the human maintainer are measuring two different curves. METR's Sonnet 4.5 result pins the distance: a 50-minute grader horizon against an 8-minute maintainer horizon, a mergeability factor D = 6.25. On long tasks the grader overstates mergeable capability by nearly fivefold.

## The cost model

Token cost per task uses a fixed convention: a substantial agentic task accumulates about 2 million cumulative input tokens across its turns, with a 90% prompt-cache hit rate, where cache reads price at roughly 10% of the standard input rate. The effective input multiplier is therefore 0.19.

Current standard API rates, mid-2026: Haiku 4.5 at $1/$5 per million tokens, Sonnet 4.6 at $3/$15, Opus 4.8 at $5/$25. Token spend is between 6% and 11% of the cost of a mergeable PR. The verification tax is everything else.

## Where tokens stop converting

The conversion threshold is the task length where mergeable probability falls below 25%. For Sonnet 4.5 that threshold is a task a human would take about 30 minutes to do. Past it, the mergeable curve flattens into a long, shallow tail, and additional generation tokens buy almost no additional mergeable output.

The capability lever vs. the verification lever: doubling Sonnet's horizon buys a 2.0% improvement in mergeable throughput cost. Halving the verification fraction through better tests, faster feedback, automated linting, and tighter review buys 46%. The ratio is better than twenty to one in favor of fixing the system over upgrading the model.

## What this implies for routing

The first routing decision is not which tier — it is how large a task you hand the model. Decompose work until each unit sits left of the roughly 30-minute conversion wall, then ask which model runs it. Once decomposed, Haiku should run most of the execution. The premium model earns its price in decomposition, orchestration, and verification reasoning.

---

*Sources: METR time-horizon datasets (May 2026); METR holistic evaluation (August 2025, March 2026); Scale SWE-bench Pro; Google Cloud DORA 2025; GitHub Copilot RCTs; Anthropic model documentation and pricing.*
