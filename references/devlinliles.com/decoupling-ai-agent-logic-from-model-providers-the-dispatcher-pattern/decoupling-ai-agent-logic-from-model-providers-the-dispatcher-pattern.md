---
type: Reference
title: "Decoupling AI Agent Logic from Model Providers: The Dispatcher Pattern"
resource: "https://www.devlinliles.com/decoupling-ai-agent-logic-from-model-providers-the-dispatcher-pattern/"
author: "Devlin Liles"
published: '2026-07-03'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most production software systems draw an explicit boundary between application logic and data storage. The application does not know which database host it is talking to; it talks to an abstraction layer that routes to the appropriate host. This boundary exists because the choice of database host changes more often than the application logic does, and coupling them creates migration costs that accumulate over time. The principle is David Parnas's information hiding from 1972: isolate the decisions most likely to change behind an interface that does not.

AI model selection has a similar property. Model providers update their APIs, release new versions, deprecate old ones, adjust pricing, and experience availability events. The model landscape changes on a timescale of months. Application-level agent logic changes more slowly. Coupling agent logic directly to a specific model provider creates the same category of accumulated migration cost that database coupling creates, just on a faster timeline.

The dispatcher pattern is the standard response: a routing layer that accepts task requests from agent code and selects the appropriate model based on task characteristics, returning results in a common format regardless of which model handled the request. Agent code does not know which model ran; it knows what the task was and what the result contained.

## What Coupling to a Model Actually Means

"Coupling to a model" is easier to recognize in its symptoms than to define abstractly. In practice it looks like:

Model names appearing as string constants in application code. When the model name changes (as it does with every major version), these constants need to be updated throughout the codebase. With one model, this is a simple find-and-replace. With five models serving different purposes, it is a more significant change.

Prompts formatted for one model's instruction style. Different model families respond differently to instruction phrasing. A prompt tuned for one model may produce degraded results on another not because the task is harder but because the instruction framing is suboptimal for the new model's training. When models change, prompts need retuning, a cost that grows with the number of distinct prompts in the system.

Response parsing written against one model's output format. Models vary in how they structure outputs, how they handle edge cases, and how they represent uncertainty. Parsing code calibrated to one model's behavior may fail silently on another's, producing incorrect parses that look like successful ones.

Retry and error handling logic calibrated to one model's error responses. Rate limiting, context length errors, content policy responses, and API failures all have model-specific formats. Error handling that knows about one model's error format will mishandle another's.

Each of these coupling points is a migration cost that materializes when the model changes. The dispatcher pattern moves all of them out of agent logic and into the dispatch layer, where they can be managed and updated independently.

## The Routing Layer

The dispatcher accepts a task request with two inputs: the task content and a task classification. The classification describes the task along dimensions that are relevant to model selection: reasoning depth required, context window size, output format requirements, latency sensitivity, and cost tolerance.

A routing table maps task classifications to model selections. Simple classifications with well-defined outputs route to smaller, faster, lower-cost models. Complex classifications requiring synthesis over large contexts route to larger, higher-capability models. The routing table is a configuration artifact, not code; it can be updated without a deployment.

The routing table's value is that it makes model selection an explicit, documented decision. When a team wants to move a task type to a different model (for cost reasons, quality reasons, or because a new model is available), the change is a routing table update, not a code change. The decision is visible, reversible, and does not require touching agent logic.

## The Prompt Adapter

Model independence requires more than routing. A task request that routes to a different model needs its prompt to be appropriate for that model's instruction style.

The prompt adapter layer sits between the routing decision and the model API call. Each model in the routing table has an associated adapter that transforms the canonical prompt format, a common internal representation, into the format appropriate for that model. The adapter handles instruction prefix conventions, system prompt structure, tool specification format, and any other model-specific prompt characteristics.

Agent code constructs prompts in the canonical format. The adapter transforms them. The model receives the format it was trained to respond to.

The adapter approach requires understanding each model's prompt conventions, which is a real investment. But it is a one-time investment per model rather than a recurring cost across all prompts. When a new model is added to the routing table, its adapter is written once. All existing prompts then automatically route correctly to that model without modification.

## Output Normalization

Models produce outputs in different formats. Even structurally identical requests ("produce a JSON object with these fields") may produce different outputs across models: different key naming, different handling of null values, different wrapper structure. Normalization handles this at the dispatch layer.

Each model adapter handles not just prompt transformation but also output transformation: converting the model's response into a common internal format that agent code expects. Agent code receives a consistent structure regardless of which model handled the request.

Output normalization requires knowing the output format of each model for each task type, which is also a per-model investment. In practice, the normalization requirements are often limited to a small number of output patterns (structured JSON, free text, code, tool calls) and the adapter for each model is straightforward once the format is known.

## Model Independence Is Not Model Indifference

A common misunderstanding of the dispatcher pattern is that it implies treating all models as equivalent. The pattern does not mean models are interchangeable; it means the choice of model is a routing decision rather than a coupling decision.

The routing table explicitly captures quality and cost characteristics of each model for each task type. A model that is fast and cheap for simple classification tasks is routed there because it performs well there, not because it is assumed to be equivalent to a more capable model. The dispatcher knows which model is appropriate for which task; it simply abstracts that knowledge into configuration rather than code.

This makes the routing table a continuously improving artifact. As evaluation data accumulates from the evaluation harness described in "Building an Evaluation Harness for Prompt Engineering," the routing table is updated to reflect which models perform best on which task types at which cost. The optimization is data-driven rather than intuition-driven.

## Operational Considerations

Provider resilience is an operational benefit of the dispatcher pattern that is often underestimated. When a model provider experiences degradation (elevated latency, increased error rates, brief unavailability), a dispatcher with multiple providers as routing targets can respond dynamically. The routing table can be updated to route away from the affected provider, or the dispatcher can implement automatic failover based on real-time provider health checks.

Without a dispatcher, provider degradation requires either accepting degraded service or an emergency code change to route to a different provider. With a dispatcher, it is a configuration update.

The implementation investment for a basic dispatcher is modest: a few days of development for the routing table, a few more for the prompt adapters and output normalizers for the initial set of models. The ongoing maintenance is proportional to the number of models in the routing table and the frequency of model updates. For teams with more than one or two models in use, or in environments where model updates are frequent, the dispatcher typically pays for itself in the first few model transitions.

For teams running a single model with no plans to change it, the additional abstraction may not be warranted. The dispatcher pattern addresses a coupling problem that only matters when the coupling is exercised, which is when the model changes. If the model is not changing, the coupling cost is not materializing. The pattern is most valuable in environments where model selection is an ongoing decision rather than a one-time choice.
