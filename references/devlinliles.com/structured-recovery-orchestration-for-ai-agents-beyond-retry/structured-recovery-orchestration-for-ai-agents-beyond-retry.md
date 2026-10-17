---
type: Reference
title: "Structured Recovery Orchestration for AI Agents: Beyond Retry"
resource: "https://www.devlinliles.com/structured-recovery-orchestration-for-ai-agents-beyond-retry/"
author: "Devlin Liles"
published: '2026-07-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

AI agent failures fall into two categories with meaningfully different recovery requirements. The first category is transient failure: network errors, rate limit responses, brief model degradation. These are well-handled by standard retry logic with exponential backoff. The second category is structural failure: an ambiguous task specification, stale context, a constraint violation the agent was not told about, a missing dependency the task assumed. Retry logic applied to a structural failure produces the same incorrect outcome, or a different incorrect outcome, without addressing the underlying cause.

The split is old. Jim Gray's 1985 paper on why computers stop drew the same line between Heisenbugs, transient faults that vanish on retry, and Bohrbugs, deterministic faults that survive it. Retry is a Heisenbug tool. Most agent failures that matter are Bohrbugs.

The distinction matters because at low agent counts, a developer can inspect each failure and make a judgment about which category it belongs to. At higher agent counts, that per-failure inspection is not practical. A system that handles both categories appropriately needs to make that classification programmatically and route each failure type to the right response.

What follows is one approach to building that classification and routing system, a seven-phase pipeline that we developed and refined over several months of operating AI agents at scale. It is not the only approach, and teams will adapt it to their context, but the phases represent a set of concerns that any recovery architecture needs to address.

## Phase One: Evidence Collection

Before anything else, a failed agent session needs to produce a structured record of what happened. This sounds obvious, but it is easy to underinvest in, especially early in a project when failures are rare and a developer can inspect the logs manually.

The evidence bundle for a failure includes: the task specification the agent received, the input context provided at session start, the full agent output including any intermediate steps, the error signal or unexpected behavior that triggered failure classification, the state of the system at the time of failure, and the sequence of actions the agent took before the failure occurred.

This bundle is what distinguishes recovery from retry. Retry sends the same input back to the agent. Recovery uses the evidence to understand why the input produced a failure and what needs to change.

## Phase Two: Root Cause Classification

The evidence bundle is passed to a diagnostic process that classifies the failure type. In our implementation, this is an LLM-based analysis, though rule-based classifiers work well for the more common failure modes and can supplement or replace the LLM analysis for those cases.

The classification produces a failure type from a defined taxonomy: transient (route to retry), structural-ambiguity (route to task clarification), structural-constraint (route to constraint injection), scope-violation (route to boundary enforcement), dependency-missing (route to dependency resolution), or unknown (route to human review). The classification also includes a confidence score.

Using an LLM for diagnostic analysis may seem counterintuitive, asking a model to analyze its own failure, but the diagnostic context differs from the task context in the way that matters. The diagnostic model is given the evidence bundle and asked a narrow question about failure classification. It is not continuing the original task or generating code. In practice, we found diagnostic accuracy to be reasonably high for the common structural failure types, though it degrades for failures that are themselves caused by unusual model behavior.

## Phase Three: Confidence-Gated Routing

The diagnostic confidence score determines the next step. At or above a defined threshold, the system routes to automatic recovery. Below that threshold, the failure escalates to human review.

The threshold is a parameter that should be tuned based on the cost of a wrong automatic recovery in the specific context. For tasks where an incorrect recovery attempt creates significant rework, a lower threshold and more human escalation is appropriate. For tasks where a wrong recovery is cheap to detect and reverse, a higher threshold reduces the human load.

We typically start around 80% confidence for automatic recovery and adjust based on observed recovery quality over the first few weeks of operation. The threshold can also be tuned per task type, allowing lower thresholds for high-stakes task categories and higher thresholds for routine ones.

## Phase Four: Human Collaboration

When the confidence gate routes a failure to human review, the handoff should be structured, and a raw alert does not qualify. A developer who receives the full evidence bundle, the diagnostic classification, the confidence score, and a proposed recovery action is in a position to make a good decision quickly. A developer who receives a notification that "agent 7 failed on task 42" is not.

The goal is to make human review a decision-making step. The system has already done the diagnostic work; the human is approving, modifying, or rejecting the proposed path forward. This makes human involvement useful in proportion to how much diagnostic work the system has done upstream.

## Phase Five: Guidance Synthesis

Whether the recovery path was determined automatically or via human review, the next phase translates the diagnosis into concrete guidance for the agent session. This is a structured context addition (specific constraints, clarifications, and explicit instructions) prepended to the agent's context when it re-enters the task.

The guidance is a structured set of additions to the original task context that addresses the specific failure cause, which is more precise than rewording the prompt. A structural-ambiguity failure might add clarifying definitions. A constraint violation might add explicit boundary statements. A missing dependency failure might add dependency resolution steps.

The agent that re-enters with good guidance is starting from a better-specified position than it had originally. The recovery improves the task specification itself.

## Phase Six: Instrumented Re-Entry

The agent re-enters the task with the guidance prepended, and the re-entry session is instrumented identically to the original. This ensures that if the recovery attempt itself fails, it produces the same quality of evidence bundle that the original failure produced, which enables a second pass through the diagnostic pipeline. A secondary failure that arrives as a black box has wasted the whole apparatus.

There is a practical limit here: a task that fails twice, even with different guidance, is a signal that the recovery pipeline is not resolving the underlying issue. At that point, escalation to human review is appropriate regardless of the diagnostic confidence, because the automated recovery path has exhausted two attempts without success.

## Phase Seven: Prevention Learning

Successful recoveries produce something valuable: a labeled example of a failure type and its resolution path. These examples are written to a shared store that the system can retrieve before future agent sessions start.

When a new session is about to begin on a task that resembles previous failures (similar task type, similar codebase area, similar scope), the relevant recovery history surfaces as context before the agent starts. The goal is to convert recoveries into constraints: make the common failure modes explicit in the task context so they are less likely to manifest.

Prevention learning accumulates value over time. Early in a project, the store is empty and every failure is novel. As the store grows, a larger fraction of potential failures are anticipated and addressed before they occur. The recovery pipeline is most expensive when the system is new and least expensive when it is mature.

## When This Level of Complexity Is Warranted

A seven-phase recovery pipeline is significant infrastructure. For a project running two or three agents with a developer actively monitoring, it is almost certainly over-engineering; manual triage and retry is adequate at that scale.

The case for structured recovery becomes compelling around 10 or more parallel agents, particularly in automated pipelines where humans monitor periodically at best. At that point, the volume of failures (largely proportional to agent throughput) exceeds what humans can triage without the diagnostic scaffolding. The pipeline pays for itself by converting human triage time into automated routing.

There is also a softer benefit: structured recovery produces a record of failure patterns that is useful for improving task specification, agent configuration, and codebase constraint documentation over time. Even if the automated routing were imperfect, the evidence collection and classification create a dataset that would otherwise not exist.
