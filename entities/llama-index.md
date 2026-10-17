---
title: "LlamaIndex"
type: "Entity"
description: "Framework for building LLM applications over data, cited here as an orchestration layer to isolate from business logic."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, llm, frameworks]
sources:
  - "/sources/designing-ai-systems-for-change.md"
  - "/sources/rethinking-intelligence-from-brains-to-systems.md"
---

# LlamaIndex

LlamaIndex is a framework for building LLM applications over data. In this corpus it appears as one of the orchestration frameworks an AI architecture should deliberately isolate from business logic, and as an example of the symbolic-storage tooling that modern AI systems borrow from the human playbook.

## Role in the Corpus

- The "designing AI systems for change" architecture playbook names LlamaIndex (with [LangChain](/entities/langchain.md)) as orchestration to isolate, so that model, provider, and framework changes do not accumulate [technical debt](/concepts/technical-debt.md) in the application.
- Because models age faster than the software around them, keeping business logic separate from the orchestration framework makes future migrations cheaper and less risky.
- In an essay on intelligence as a system, knowledge graphs, databases, retrieval-augmented generation, and vector databases are described as symbolic storage — the externalized memory that scales intelligence beyond a single model.

## Related

- [model-agnostic architecture](/concepts/model-agnostic-architecture.md) — the reason to isolate the framework
- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — the pattern LlamaIndex implements
- [LangChain](/entities/langchain.md) — the sibling orchestration framework
- [dispatcher pattern](/concepts/dispatcher-pattern.md) — the shared access layer that decouples app from provider
