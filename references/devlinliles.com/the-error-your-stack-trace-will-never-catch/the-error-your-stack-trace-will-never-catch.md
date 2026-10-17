---
type: Reference
title: "The Error Your Stack Trace Will Never Catch"
resource: "https://www.devlinliles.com/the-error-your-stack-trace-will-never-catch/"
author: "Devlin Liles"
published: '2026-08-19'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Software engineers are trained to think about errors in terms of exceptions. The process threw. The API returned a 500. The database connection timed out. These are the errors that interrupt execution and produce a log entry. They are also the easiest agentic errors to handle, because you can see them.

The error that kills agentic systems in production is harder. The agent completes successfully. The logs are clean. The tool calls returned 200. And the output is wrong, in a direction that takes three workflow steps and one frustrated user to discover. Technically successful execution toward the wrong goal. No exception thrown. No obvious signal.

Agentic error handling is a different discipline. The classification is different, the detection problem is harder, and the safeguards operate at a different layer.

## Five error types, not one

The field has converged on a five-type taxonomy for agentic errors, borrowed and adapted from the Augment Code agentic pattern catalog.

**REG (Regression):** behavior that worked before has stopped, usually correlated with a recent deployment, prompt change, or model update. The signal is comparative: this used to work, now it doesn't. Detection requires a baseline. Without one, regressions look like new bugs.

**BUG:** a new defect with no prior correct behavior to compare against. The hardest to detect automatically because there is no regression signal, only the quality of the output itself.

**SEC (Security)** is in a category of its own when it comes to urgency. It doesn't matter how few users are affected: a prompt injection, tool misuse (an agent being manipulated into calling a privileged tool with attacker-controlled arguments), or unauthorized data access through a retrieval layer is a P1 regardless of blast radius. The urgency classification overrides the impact count.

**INF (Infrastructure):** compute, network, or storage failure. Often transient. Standard retry-with-backoff handles most INF errors, with the critical constraint that retries must have a hard upper bound or they become infinite loops.

**DAT (Data)** is the most insidious entry in the taxonomy. Consider a retrieval layer returning stale embeddings from a cached index: the agent receives the data, finds it plausible, proceeds, and produces output that is consistently wrong across many sessions. Nothing fails. The system reports success. The error is silent until someone compares the output to ground truth and notices the drift. A data error in an agent's memory layer is not a crash you discover in the logs. It is a bias you discover in the outcomes.

Classifying an error by type determines the response: urgency, blast radius, and whether the system can recover automatically or needs human intervention. P1 through P4 priority is the product of blast radius (how many users or systems are affected) and urgency (whether a workaround exists). The same error classification framework that works in software engineering applies here, with the addition of semantic drift as a category that software engineering frameworks don't address.

## Semantic drift: the error with no exception

Semantic drift is the divergence between what the agent is currently doing and what it was originally asked to do, as a session progresses. It is a gradual accumulation of small decisions that collectively take the output in the wrong direction, each step individually defensible, the aggregate quietly off-target. No crash. No wrong status code. Just a session that ends somewhere the user didn't intend.

Infrastructure failures are caught immediately. Exceptions are caught at the call site. Semantic drift is caught last, often only when a human reviews the final output and realizes it doesn't resemble the original goal. The detection latency chart above illustrates this pattern. This latency is the real cost: the more steps the agent takes after it starts drifting, the more work has to be unwound.

The current state of the art for semantic drift detection is similarity scoring between current output and the original goal specification. When that score drops below a threshold, the system flags the session for review. This is imperfect. Similarity scoring misses drift that is semantically close but contextually wrong. It is also better than nothing, which is the alternative most systems currently implement.

## Pre-execution gates

The highest-leverage error handling happens before execution begins. Three pre-execution gates belong in every production agentic system.

Test sufficiency analysis runs before executing code changes and verifies that existing tests cover the risk tier of the changed files. Schema changes require integration-tier tests. Store method changes require database-backed tests. This check is the most common prevention for the "tests pass, production breaks" failure mode: the agent produces code, the tests pass, the deployment fails because the tests weren't testing the right things.

Scope validation checks that the task definition falls within the approved scope boundary before execution begins. This ties back to definition (Post 3 in this series): agents expand scope; a pre-execution gate prevents that expansion from happening silently.

Pre-flight checks are the shortest gate and the most embarrassing to skip. Validate the environment before any execution: credentials present, required services reachable, configuration complete. These are the easiest failures to prevent and the ones that reliably surface mid-run when skipped.

## Runtime safeguards

Circuit breakers exist for one reason: to stop a bad run from becoming a catastrophic one. The mechanism is a sliding error-rate window. When the rate crosses a defined threshold, execution halts. The calibration is the real work. Too tight and you interrupt sessions that were recovering from transient failures. Too loose and you let a runaway consume the token budget before the brake engages. Start with a threshold that would have caught your last production incident, then tune from there.

Timeout enforcement is the control that service engineers implement by default and agentic engineers frequently skip. Every tool call and every agent step needs a hard time limit. A step that exceeds its maximum time budget is treated as a failure. The assumption that a model will complete in "reasonable time" without a bound is how hung sessions accumulate.

Token budget enforcement closes the loop. Set per-session and per-task cost limits, and halt execution before a runaway agent exceeds the ceiling. A session that has consumed 10x its estimated token ceiling, say 50K tokens on a task scoped for 5K, is a signal something has gone wrong. Letting it continue is not patience; it is cost-funded confusion.

## Blast radius in multi-agent systems

Blast radius in a single-agent system is bounded: the failure affects that agent's task and its downstream consumers. Multi-agent systems change this calculation in a specific way. A failure in a shared tool, a shared memory layer, or a shared infrastructure component can cascade silently across many concurrent sessions. The agent that fails doesn't know it's affecting others; the agents being affected don't know they're consuming corrupted inputs. The failure is distributed; the signal is not.

Blast radius analysis maps the direct failure to all downstream agents, services, and users it touches. The map is what makes triage tractable: knowing the blast radius tells you whether this is a P1 (stop the world) or a P4 (fix it in the next sprint). Building that map requires understanding the dependency graph of your multi-agent system before something goes wrong.

---

*Sources: Augment Code agentic design pattern catalog (2026) — error taxonomy and blast radius; Vellum agentic workflows guide; LangSmith documentation (tracing and error detection); Helicone documentation (request-level monitoring); Opik documentation (open-source LLM error tracking).*
