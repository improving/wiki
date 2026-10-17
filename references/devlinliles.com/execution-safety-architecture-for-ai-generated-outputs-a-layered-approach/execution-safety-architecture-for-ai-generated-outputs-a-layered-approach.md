---
type: Reference
title: "Execution Safety Architecture for AI-Generated Outputs: A Layered Approach"
resource: "https://www.devlinliles.com/execution-safety-architecture-for-ai-generated-outputs-a-layered-approach/"
author: "Devlin Liles"
published: '2026-07-09'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

When an AI system generates outputs that will be executed (code that runs, calculations used in decisions, formal expressions that are evaluated), the safety question shifts from the model to the execution environment. The model's output may be syntactically correct and semantically plausible but still consume unbounded memory, call external services outside the intended scope, or fail to terminate. These are properties of execution, not generation, and they are not detectable by evaluating the output before running it.

This is not a novel problem. Every runtime environment faces similar questions about what untrusted or partially trusted code is permitted to do, and the browser sandbox and the JVM security manager answered them for code arriving over the network decades ago. The specific challenge in AI-generated output contexts is that the code is generated at runtime, by a process that does not have access to the execution environment's operational constraints, at a volume that may be too high for manual review before execution.

The response is a layered safety architecture: a set of independent checks and constraints that together limit the blast radius of unexpected execution behavior. No single layer catches everything; the value is in the combination.

## Layer One: Architectural Chain Analysis

Before execution, the first question is scope: what does this output touch? An AI-generated function that reads a local variable is scoped differently from one that reads from a database, writes to an external service, and modifies shared state. The blast radius of the second is substantially larger.

Architectural chain analysis traces the dependency and effect chain of the generated output before execution. This is a static analysis step that identifies data sources read, data stores written, external calls made, and other components invoked. The analysis is compared against the expected scope of the task that generated the output.

When the analysis identifies access patterns that fall outside the expected scope (database tables the task had no reason to access, external API calls not in the task specification, files outside the designated working area), those accesses are flagged for review before execution proceeds. This does not necessarily block execution; the flag might result in human review, in a scope clarification request, or in automatic adjustment to the execution context. The key is that out-of-scope access is detected before it occurs rather than discovered after the fact.

The practical limitation of this analysis is that it depends on the code being analyzable statically. Dynamic access patterns, where a resource's name is computed at runtime, are harder to analyze before execution and may require runtime monitoring as a supplement.

## Layer Two: Static Code Analysis

Standard static analysis applies to AI-generated code in the same way it applies to human-generated code, but the failure mode distribution is different. AI-generated code is reliably different from human-generated code in specific ways: it is more likely to suppress errors without handling them, to construct strings from inputs without sanitization when training examples did not include sanitization, and to use patterns that were common in training data but have since been deprecated.

Static analysis rules calibrated to these specific patterns are more useful than a generic lint configuration for AI-generated outputs. Rules that flag error suppression patterns, input interpolation without sanitization, and use of deprecated APIs at the level of specificity appropriate to the codebase are worth investing in separately from general code quality rules.

Static analysis does not catch runtime behavior. It catches patterns that are likely to cause problems but cannot observe what the code actually does. It is fast and cheap to run, making it appropriate as an early filter before more expensive runtime checks.

## Layer Three: Execution Timeout

A timeout is the simplest and most robust protection against a specific but severe failure mode: non-terminating execution. An AI-generated recursive function that does not terminate, a loop with an incorrect termination condition, or a query that triggers a table scan on a large dataset can consume a process indefinitely without a timeout.

Timeout values should be set based on the expected execution characteristics of the task type. Short timeouts for tasks that should complete in milliseconds, longer timeouts for tasks with acknowledged computational demands. The default should be conservative: err toward shorter timeouts and adjust upward for specific task types that have demonstrated they need longer.

A timeout that fires should produce a bounded output rather than no output at all: either a partial result with a clear indication that execution was interrupted, or a failure report with the generated code attached. The partial result or failure report is what enables diagnosis of why the code exceeded the timeout.

## Layer Four: Memory Allocation Limits

Memory limits complement timeout constraints. An AI-generated function that loads an entire file into memory is well-behaved when the file is small and problematic when it is large. The model does not know file sizes at generation time; the execution environment does.

Per-execution memory limits cap the allocation available to a single AI-generated computation. When the limit is reached, execution terminates with a memory limit exception rather than consuming available system memory until the process crashes or the operating system begins swapping.

Memory limit violations are diagnostic signals as well as operational safeguards. A generated computation that consistently hits memory limits is revealing something about its approach: it is materializing data that could be streamed, accumulating state that could be released incrementally, or operating on input sizes that require a fundamentally different algorithm. The violation is the indication; the root cause determines the fix.

## Layer Five: Circuit Breaker

The circuit breaker addresses the pattern where a failing execution is retried repeatedly without addressing the root cause. The pattern comes from Michael Nygard's Release It!, where it protected distributed systems from cascading failure, and it applies to generated code for the same reason. A single failure is a data point. The same generated output failing across multiple retries is a pattern that warrants intervention rather than continued retry.

When a generated output fails more than a configured number of times within a configured window, the circuit breaker opens. Subsequent execution attempts for that output are rejected immediately with a circuit-open response rather than allowed to run and fail again. The rejection is logged with the full failure history.

This serves the immediate purpose of preventing resource consumption on a retry loop that will not succeed, and the longer-term purpose of producing a clear operational signal that human review is needed. A circuit breaker that has opened is a meaningful event. Something in the generated code or the execution environment is producing repeated failures, and it should trigger diagnosis rather than accumulating silently in logs.

The circuit breaker resets after a defined cooling period or after the execution environment receives a corrected version of the generated output. It is a pause, not a permanent block.

## Layer Six: Rate Limiting

Rate limiting governs the throughput of the execution environment as a whole. In systems where multiple AI agents can generate executable outputs concurrently, bursts of generation activity can produce corresponding bursts of execution requests. Without rate limiting, a burst can exhaust connection pools, saturate CPU, or overwhelm dependent services.

Backpressure is the appropriate mechanism: when the execution environment is at capacity, additional requests queue rather than execute immediately. The queue has a depth limit. Requests that arrive when the queue is full receive an explicit capacity response rather than timing out silently after a long wait.

Rate limiting also provides a natural throttle for cost-sensitive execution environments where execution itself carries per-operation cost (external APIs, cloud compute). Setting rate limits based on budget constraints rather than just technical capacity allows cost management to be built into the execution layer rather than handled entirely at the orchestration level.

## Combining the Layers

These six layers are independent checks. Each addresses a different failure mode, and none depends on the others being present. The value of combining them is defense in depth: each layer catches failures that the others might miss, and a failure that passes through one layer is likely to be caught by a subsequent one.

The implementation cost varies by layer. Timeouts and memory limits are typically one to two hours of configuration work. Rate limiting and circuit breakers are available as libraries in most technology stacks. Architectural chain analysis and AI-specific static rules require more custom development, days rather than hours.

Whether all six layers are warranted in a given system depends on the consequence of execution failures and the volume of generated outputs. For a low-volume system with a human reviewing each generated output before execution, several layers may be unnecessary. For a high-volume automated pipeline where human review is not practical for every execution, the full stack is worth the investment.
