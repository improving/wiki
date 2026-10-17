---
type: Reference
title: "The Context Window Is Not a Filing Cabinet"
resource: "https://www.devlinliles.com/the-context-window-is-not-a-filing-cabinet/"
author: "Devlin Liles"
published: '2026-08-21'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Here is what most teams do with the context window: they fill it up. Every prior message, every retrieved document, every system prompt update, every intermediate result piled in until either the model complains about length or performance degrades enough that someone investigates. The assumption is that more context is better context. It is not.

Context management is the operational discipline of ensuring the agent's working window contains exactly the right information for the current step, no more and no less. It is the twelfth domain and the one that gets the least dedicated attention, probably because it doesn't produce dramatic failures. Context problems produce gradual, hard-to-attribute performance degradation. The agent was good last month. It's worse now. No one changed the model, no one changed the prompts. What changed was that the context got messier.

## The three problems in the window

**Context window saturation** is what happens when the window fills with irrelevant prior steps. There is not enough room for new information. Performance degrades before the hard limit is reached: LLMs begin losing coherence in the latter portions of very long contexts before they hit their nominal token ceiling. Saturation looks like a capacity problem, but it is a selection problem. The window is full of things that don't matter for the current step.

**Context pollution** is subtler and more damaging. Old, contradicted, or irrelevant information in the active window misleads the agent even when there is technically enough room. The agent believes two contradictory things about the same entity. It applies a constraint that was relevant three steps ago and irrelevant now. It recalls a preference the user changed but the context hasn't been updated to reflect. Pollution looks like model error. It is a context hygiene problem.

**Retrieval latency** is the operational cost of pulling relevant context from memory stores at runtime. Poorly designed retrieval creates bottlenecks in real-time workflows. The multi-hop version is the worst case: the agent needs fact A to retrieve fact B to retrieve fact C. Three retrieval round trips, each dependent on the previous, slow and fragile at every hop.

## The patterns worth knowing

**Sliding window** is the simplest approach: keep only the last N messages in the active context and discard older ones. It works well when recent context is what matters and early context can safely be dropped. The place it breaks down is exactly where you'd expect. Tasks that reference early context, a constraint established in step two or a decision made in step five, produce wrong answers in step twenty because the relevant history scrolled out. Simple to implement; appropriate for short-horizon tasks; unreliable for anything with a long dependency chain.

RAG is the pattern most teams reach for when the context problem gets serious. **Retrieval-Augmented Generation** stores context in an external vector database and retrieves the most relevant chunks at query time. The design is elegant: you aren't forced to choose between having context available and paying to load it upfront. The problem is that retrieval quality determines context quality, and retrieval quality is hard to get right. A poorly tuned retrieval system surfaces the wrong chunks with high confidence. The agent reasons from that incorrect retrieved context without knowing the context is wrong. RAG shifts the failure mode from "window too full" to "window filled with the wrong things," which is often harder to debug because the agent still appears to be reasoning.

**Summarization compression** takes a different approach to the same problem. Older conversation history gets periodically summarized into a compact representation, and the summary replaces the raw history in the window. High-level context survives at lower token cost. The tradeoff is that summaries are lossy by design, and the details most likely to get dropped are the ones that will matter later. For long-running sessions where perfect recall isn't required, this is often the right call.

**Context injection at step boundaries** loads only the context relevant to a given step at the moment that step begins. The catch is that this requires knowing in advance what each step needs, which is a planning discipline, not just an execution one. Teams that invest in hierarchical planning (Post 2 in this series) find context injection tractable because the planning structure already defines what each step requires. Skip the planning investment and context injection becomes guesswork.

**Bounded execution** is an architectural choice, not a runtime mechanism. Sessions are designed to fit within context limits. When a session ends, the next one starts with the relevant context injected fresh. Context growth gets addressed by scoping the work, not by managing the overflow. For workflows where sessions naturally compose, this is the cleanest solution available.

## Where retrieval actually breaks down

Most context management problems are retrieval problems. The context is wrong because the retrieval mechanism isn't surfacing the right information, not because the information doesn't exist.

LlamaIndex gives you the most complete retrieval pipeline out of the box: chunk management, context injection, and hierarchical summarization without stitching together separate libraries. For teams building knowledge-heavy agents, anything that reasons over large document corpora or long session histories, LlamaIndex is the right starting point, with Pinecone or Weaviate as the managed vector store backend.

Cohere Rerank is worth calling out specifically. It is a re-ranking layer that runs over retrieved chunks and scores them for relevance before injection. A retrieval step that returns the top-20 most similar chunks often contains noise. A reranking step that scores those 20 for contextual relevance and injects only the top-5 produces meaningfully better context quality.

## What context discipline actually looks like

The teams that manage context well share one practice: they are explicit about what each step needs before they build the retrieval mechanism. "Retrieve everything relevant" produces the saturation problem. "Retrieve the last three decisions made about this entity" or "retrieve the acceptance criteria for the current task" produces a retrievable, bounded query. Specificity is the practice. Everything else follows from it.

The mental model that helps: treat the context window as a whiteboard, not a filing cabinet. A whiteboard holds useful information for the current problem, and you erase it when the problem changes. A filing cabinet accumulates everything and makes you search through it to find what you need. The context window performs like a whiteboard when it's managed deliberately, and like an overfull filing cabinet when it isn't.

Context management is where the rest of this series stops being theoretical. A memory system with no opinion on what belongs in the active window is incomplete. A planning hierarchy that doesn't specify what each step actually needs is going to produce bloated, unfocused context, and you'll see it as quality degradation before you identify it as a context problem. Evaluation closes the loop: it tells you whether the strategy you chose is holding up or slowly falling apart. That's the actual work.

---

*Sources: LlamaIndex documentation (RAG orchestration, retrieval pipelines, context injection); LangChain documentation (memory and retrieval primitives); Cohere Rerank documentation; Vellum agentic workflows guide; Augment Code agentic design pattern catalog (2026); Chroma documentation (local vector store); Pinecone documentation (managed vector database); Weaviate documentation (hybrid search).*
