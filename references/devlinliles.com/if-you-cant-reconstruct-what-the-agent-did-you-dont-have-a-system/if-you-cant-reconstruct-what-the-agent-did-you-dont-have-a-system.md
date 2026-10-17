---
type: Reference
title: "If You Can&#x27;t Reconstruct What the Agent Did, You Don&#x27;t Have a System"
resource: "https://www.devlinliles.com/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system/"
author: "Devlin Liles"
published: '2026-08-20'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# If You Can't Reconstruct What the Agent Did, You Don't Have a System

The standard for understanding what happened in a software system is the audit log. In regulated industries it's a compliance requirement. In any production system, it's what you reach for when something breaks and you need to know why.

Agentic systems need the same capability, and they require it at a different layer. A traditional audit log captures API calls and database writes. An agentic audit log needs to capture something more specific: what the agent saw, what it decided, why it decided it, and what it did as a result. The chain of reasoning, not just the chain of effects.

The $1.97B market in 2025 growing to $2.69B in 2026 is a secondary signal. The primary one: teams I talk to regularly are shipping agents into production and discovering, after the fact, that they cannot reconstruct what the agent actually did. The mid-30s percent year-over-year growth rate tells you that production deployments are outpacing the infrastructure to observe them.

## The standard that's winning

The emerging standard for agent tracing is OpenTelemetry GenAI semantic conventions, known as semconv. It defines four span operation types for agent observability: `create_agent`, `invoke_agent`, `invoke_workflow`, and `execute_tool`. Every agent action maps to one of these span types, with a parent span, timestamps, and structured metadata.

Datadog adopted these conventions natively from version 1.37, released in December 2025. For teams already running on Datadog for infrastructure observability, agent tracing can flow into the same backend as the rest of your observability data, without a separate tool or custom exporters.

OTel-compliant traces are the bet to make. The reason is interoperability: OTel traces can flow into any supporting backend without vendor lock-in. You can switch from Datadog to Langfuse to Arize Phoenix without changing your instrumentation. Teams that instrument with proprietary formats are betting that the vendor they pick today is the one they'll use forever. That's a bet I wouldn't take.

## What good auditing actually captures

Distributed tracing applies the same model as microservice observability: every agent action is a span with a parent span, making it possible to reconstruct the full execution tree. When an agent spawns a subagent, that subagent's spans are children of the parent span. The tree structure is the genealogy of the session.

Session genealogy is the tracking of parent-to-child session expansion as tasks decompose. It answers the specific question: "This subagent was spawned by this coordinator to execute this specific step." That data is what makes it possible to trace a bad output back to the specific delegation decision that produced it.

Context snapshots are point-in-time captures of what the agent's working context contained at each decision point. This is what makes replay possible. If you want to understand why the agent made a specific decision, you need to see exactly what it saw when it made it. Without context snapshots, you have the decision but not the reasoning inputs. With them, you can reconstruct the scene.

Tool call audit is the raw evidence layer: every external tool invocation, with what arguments, and what was returned. Separate from what the agent said it was going to do. The tool call record is what you check when the agent claims to have performed an action and the downstream system shows no evidence of it.

## The tool landscape

None of these tools does the same thing, and picking the wrong one mostly means you'll replace it in a year. Start with what you already have.

On Datadog? It handles agent observability natively from v1.37, no second tool required. On LangChain or LangGraph? LangSmith is the obvious first move: the integration is tight, the mental overhead is low, and you'll be productive in an afternoon.

Outside those stacks, the split is between control and compliance. Langfuse is the right call if you need full data ownership and want to self-host: open-source, no vendor dependency, strong production traction. Fiddler serves a different constraint entirely. If you're in a regulated industry where audit trails need to be formally defensible for an examiner, Fiddler is purpose-built for that evidence standard.

Arize Phoenix and Traceloop/OpenLLMetry are both OTel-native and worth evaluating if you want instrumentation that won't lock you to a vendor backend. Arize brings a machine learning observability pedigree; Traceloop is framework-agnostic by design. Either one is a reasonable bet if interoperability is the priority. Braintrust is the one to look at if you want evals and observability in a single platform and are willing to pay for the integration.

The selection principle: match the tool to your current stack and your compliance requirements first. Don't buy a second observability platform if your existing one can do the job.

## Immutability is not optional for compliance

Append-only session logs that cannot be modified after the fact are the tamper-evidence requirement for regulated industries. That distinction matters: an audit log that can be edited is not an audit log. It is a document. SOC 2 evidence, HIPAA audit trails, and financial service compliance frameworks all require that audit records be demonstrably unaltered.

For code-writing agents, diff-level change tracking is a record of exactly which files were changed, in what order, and by which session. Git provides this naturally for file-based workflows. Teams building code-writing agents that skip git-based worktrees are missing the most complete and tamper-evident change record available.

## The capability gap most teams have

Most teams that deploy agents in production have logging. They have request logs, error logs, and in some cases token usage logs. What they don't have is the ability to reconstruct the full decision trace for a specific session: what context the agent had, what it decided, and why, at each step.

That reconstruction capability is what separates observability from logging. Logging tells you that something happened. Observability tells you why. For agentic systems, where the "why" is a reasoning chain rather than a call stack, the gap between the two is larger than in traditional software. Closing it is the precondition for evaluation, continuous improvement, and every governance capability covered in the next post in this series.

---

*Sources: Confident AI observability comparison (2026); Braintrust LLM observability buyer's guide (2026) — market size figures ($1.97B 2025, $2.69B 2026 est., ~mid-30s% CAGR); OpenTelemetry GenAI semantic conventions (semconv); Datadog GenAI monitoring documentation (v1.37, Dec 2025); Langfuse documentation; Arize Phoenix documentation; LangSmith documentation; Traceloop / OpenLLMetry documentation.*
