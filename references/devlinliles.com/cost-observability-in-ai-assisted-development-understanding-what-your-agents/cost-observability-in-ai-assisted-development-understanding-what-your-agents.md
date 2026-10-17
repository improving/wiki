---
type: Reference
title: "Cost Observability in AI-Assisted Development: Understanding What Your Agents Spend"
resource: "https://www.devlinliles.com/cost-observability-in-ai-assisted-development-understanding-what-your-agents/"
author: "Devlin Liles"
published: '2026-07-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

API token costs in AI-assisted development systems have an unusual property: they scale with context complexity more than output volume. A task that requires synthesizing a large input context costs substantially more than a narrow-scope task with similar output length. This makes the cost behavior of AI agents harder to predict than traditional compute costs, and more dependent on how tasks are specified than on how many tasks are run.

This matters because without measurement, the cost of an agent-based development workflow is difficult to estimate or optimize. The total bill is visible at the provider level (most AI APIs publish usage dashboards), but the per-task, per-agent-role, and per-activity-category breakdown that would allow meaningful optimization is not surfaced automatically. That breakdown requires instrumentation.

## Why Token Cost Behavior Is Non-Obvious

A useful analogy is cloud compute before reserved instances and rightsizing became standard practice. Early cloud adoption often involved running all workloads on the same instance type because the alternatives required measurement infrastructure that teams had not yet built. As that infrastructure developed, a significant fraction of cloud spend turned out to be concentrated in a small fraction of workloads, and significant savings were available simply from matching instance size to actual requirements.

AI token costs have a similar structure. A task that requires reading 20 files of context before generating output consumes 10 to 20 times the tokens of a task that operates on a narrow scope. A task using a large, high-capability model on work that would produce equivalent quality with a smaller model costs 4 to 10 times as much, depending on the provider's pricing tiers. Without measurement, it is not possible to identify which tasks are in the expensive category or whether the expense is justified by the work they are doing.

Actual cost distributions in production AI development systems tend to be skewed: a small fraction of tasks, typically those involving large context windows and complex synthesis, account for a disproportionate share of total spend. These are often exactly the tasks where high-capability models are appropriate. But adjacent task types, similar in surface complexity, often turn out to be adequately handled by less expensive configurations.

## The Dimensions Worth Instrumenting

**Per-task cost** is the foundation. Every agent session (implement this story, review this PR, analyze this failure) has an associated token count. Capturing that token count alongside task metadata (type, size, assignee agent role, outcome) creates the dataset needed for all higher-level analysis.

**Per-agent-role cost** reveals whether different roles in the agent system are consuming resources proportionate to their function. An implementation agent working on feature code is expected to consume more tokens than a documentation agent summarizing a completed story. If role costs are inverted from expectations, it is usually a signal that something in the role's configuration (context provided, task scope, model tier assigned) is misaligned with the work the role is doing.

**Per-model-tier cost** is where optimization typically lives. The same task run on different model tiers has very different cost profiles. Whether the quality difference between tiers justifies the cost difference depends on the task type, which is why per-task measurement is the prerequisite for model-tier optimization. Without knowing which tasks ran on which models and what quality they produced, the tier assignment question cannot be answered empirically.

**Per-activity-category cost** connects spend to business outcomes. Categorizing agent work as feature implementation, defect remediation, technical debt reduction, or test generation makes it possible to compute cost-per-unit-outcome for each category: cost per story point implemented, cost per defect found, cost per test generated. These are the metrics that make a business case for investment or justify a configuration change.

## Budget Enforcement as a Diagnostic Tool

Attaching token budgets to individual agent sessions and enforcing them has two distinct values: direct cost control and diagnostic signal.

The direct cost control value is intuitive: a session that is allocated a budget and exhausted it before completing surfaces that fact explicitly, allowing a decision about whether to extend or conclude. This prevents runaway sessions from consuming resources without producing useful output.

The diagnostic value is less obvious but often more interesting. Sessions that consistently exhaust their budgets on tasks that appear comparable in scope to sessions that complete comfortably are revealing something: the task specification is underspecified and the agent is searching through a large space, the context provided is broader than it needs to be, or the model tier is mismatched to the task and producing inefficient intermediate reasoning.

Budget hits are a signal that something in the task configuration deserves examination, beyond being a cost management event. Teams that review budget hit patterns periodically often discover configuration improvements that reduce both cost and session failure rate simultaneously.

## Building a Recommendation Layer

After cost data has accumulated for a few weeks of operation, patterns emerge that are worth surfacing to the team. Which task types consistently run more efficiently on lower model tiers? Which agent roles are consuming disproportionate tokens relative to their output? Which activity categories have cost-per-outcome ratios that have trended upward over recent sprints?

These observations are inputs to configuration decisions, never automatic actions. The recommendation reads as evidence: this task type may be adequately served by a different configuration, and that is worth evaluating. The evaluation then runs through the quality measurement infrastructure (described in the companion post on evaluation harnesses) to confirm that the lower-cost configuration maintains acceptable quality before the routing change is committed.

## What Observability Makes Possible

The primary value of cost observability is making the AI development investment legible: understanding what the system is spending, what it is spending it on, and whether the outcomes justify the spend. Cost reduction is often a significant secondary outcome.

An AI agent system that is well-instrumented can answer questions that matter to engineering leadership and finance stakeholders: what is the cost per feature shipped, how does that trend over time, what would the cost be at twice the current agent count, and where does the system create value relative to its cost. Without instrumentation, those questions are answered with estimates and guesses that erode confidence in the investment.

Cost observability is also the prerequisite for the model selection optimization described elsewhere in this series. The right model tier for each task type can only be determined empirically, and empirical determination requires measurement. The cost dimension and the quality dimension are both necessary inputs to the routing decision; neither alone is sufficient.
