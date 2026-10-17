---
type: Reference
title: "Eval-Driven Development: The Discipline Agent Teams Are Missing"
resource: "https://www.devlinliles.com/eval-driven-development-the-discipline-agent-teams-are-missing/"
author: "Devlin Liles"
published: '2026-07-20'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Fifty-seven percent of organizations have AI agents running in production right now. McKinsey QuantumBlack tracked this in their latest global AI survey, and the number surprised almost everyone. What didn't surprise anyone paying attention: quality is the number-one barrier to deploying more of them.

Most of those teams built their agents the same way. They prototyped something that worked in demos, pushed it to production, and then discovered that "working in a demo" and "working reliably across thousands of real users" are two completely different statements. Quality degraded. Confidence evaporated. Leadership started asking hard questions nobody had good answers to.

The teams that don't have this problem aren't smarter. They just adopted a discipline that the rest of the field hasn't caught up to yet. They write evals before they write agents.

## The problem isn't the model

When an agent behaves badly, the instinct is to blame the model. Swap GPT-4o for Claude. Upgrade the context window. Try a different temperature. Usually none of it helps, because the model isn't the problem.

The problem is that nobody defined what "correct" meant before they started building.

Software engineers learned this lesson in the early 2000s with test-driven development. Write the test first. Make the contract explicit before you're emotionally invested in the implementation. TDD worked because the contract was deterministic: the function either returned the right value or it didn't.

Agents break that assumption. Outputs vary across runs, model versions, prompts, and tool states. You can hallucinate in ways that pass every surface check. The demo looks great. The system prompt hasn't changed. And somehow the agent is doing something subtly wrong that you can't articulate. It just "feels worse this week." That's not quality management. That's vibes.

## What evals actually are

An eval is an automated test suite for AI behavior. You define what "working" looks like, you capture it in a dataset of inputs and expected outputs (or expected properties), and you run that dataset against every build. The eval is the specification. Writing it first forces the same discipline TDD imposed: you cannot build until you know what done looks like.

A single-turn eval is relatively straightforward. Did the model say something true? Did it format the response correctly? Agentic evals are harder, because the thing you're evaluating isn't a response — it's a sequence of decisions. Was each tool call necessary? Were the parameters correct? Did the agent handle an error in step 4 in a way that didn't corrupt everything that followed?

This is trajectory evaluation. AgentBench, published at ICLR 2024, was the first benchmark to systematically evaluate large language models as agents across eight distinct environments. It found a measurable gap between commercial and open-source models in multi-step tasks — a gap that simply wasn't visible in single-turn benchmarks. The gap is in the trajectory, not the response.

If every step of a 10-step agent chain has 95% reliability (which sounds excellent), the whole chain succeeds about 60% of the time. At 20 steps, you're below 36%. Small differences at step 3 cascade into wildly different decisions at step 7.

## Three tiers of evals, and why order matters

The practical implementation has three tiers, and you run them in sequence: string comparisons are free. Don't pay for LLM judgment on failures a regex could catch.

**Deterministic evals** come first. Is the output valid JSON? Did the agent call the right tool? Is the required field present? These are fast, cheap, and catch the obvious failures.

**Model-graded evals** come second. You use a separate LLM as a judge to evaluate subjective qualities: was the reasoning coherent? Was the tone appropriate for the context? Did the agent's plan make sense given the instructions? DeepEval's metrics cover Task Completion, Tool Correctness, Goal Accuracy, Step Efficiency, and Plan Adherence. Tool failures alone break down into misclassification, parameter mapping errors, error-handling failures, and sequencing errors. The taxonomy matters because different failure modes require different fixes.

**Human-in-the-loop review** comes last. Reserve it for the highest-value, hardest-to-automate failure modes. It's expensive, so you deploy it surgically.

The Anthropic engineering team published in January 2026 on how the Claude Code team built their eval suite. They started with 20 to 50 tasks drawn from real failures, not synthetic examples. Real things the system got wrong. They iterated rapidly on that small set, then expanded the dataset as new failure modes emerged. The principle: let production failures drive your eval coverage.

## The organizational capability nobody's building

Eval-first development is an organizational capability, not just a technical one. Teams with evals can swap models in days — they have automated proof the new model is safe to ship. Teams locked out of that proof are stuck with whatever they first deployed, because there's no mechanism for demonstrating change is safe.

The implementation doesn't need to be complicated. Run a dataset nightly. Post results to a Slack channel. Block deploys on regression. That's the nightly eval bot pattern, and it's achievable in a week. Tooling exists: Braintrust works well across providers; DeepEval has the lowest friction for Python teams; LangSmith integrates cleanly if you're inside LangChain or LangGraph.

The 57% of organizations with agents in production built those agents. The quality barrier they're hitting now isn't a model problem. It's an engineering discipline problem — the same one software teams hit before TDD became standard practice. The discipline has a name. It has a toolchain. It's available right now.

The teams that adopt it aren't betting on better models. They're building the infrastructure to know when any model is good enough.
