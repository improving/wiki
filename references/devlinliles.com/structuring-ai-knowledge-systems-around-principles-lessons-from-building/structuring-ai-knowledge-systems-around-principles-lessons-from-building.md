---
type: Reference
title: "Structuring AI Knowledge Systems Around Principles: Lessons from Building a Learning Engine"
resource: "https://www.devlinliles.com/structuring-ai-knowledge-systems-around-principles-lessons-from-building/"
author: "Devlin Liles"
published: '2026-07-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most AI knowledge retrieval systems are built on a search-index model: documents are chunked, embedded, and retrieved by semantic similarity when a query arrives. This is a well-established and often appropriate architecture. It performs well when the task is finding the most relevant document from a corpus, and the engineering path to a working system is clear.

It performs less well when the task is reasoning: constructing an answer by applying general principles to a specific case. The search-index model treats all knowledge as equivalent and retrieves by similarity. Textbooks, by contrast, are organized hierarchically: foundational principles first, then the concepts those principles govern, then the processes that apply them, then specific examples. That sequencing is more than pedagogical convention. It reflects the logical dependency structure of the knowledge itself.

The tension is one of the oldest in AI. Case-based reasoning systems of the 1980s answered by analogy to stored cases; rule-based systems answered from encoded principles; each failed where the other was strong. Embedding retrieval is case-based reasoning with better similarity math, and it inherits the same weakness on novel cases.

When building Helix, a general-purpose learning system for math and scientific subjects, we found that the retrieval-first approach produced a system that could find relevant passages but had difficulty with inference, reasoning from principles to novel cases. Moving to a principles-first knowledge structure changed the failure mode from "retrieves the wrong document" to "reaches the boundary of its principles," which turned out to be a more useful and honest way to fail.

## The Hierarchy and Why It Matters for Inference

In the Helix knowledge model, every subject domain is organized into four levels:

**Principles** are the foundational truths of a domain: general, abstract, and broadly applicable. Newton's second law (F = ma) is a principle. It does not describe a specific situation; it constrains what is possible across all situations involving force, mass, and acceleration.

**Concepts** are the entities and categories that principles operate on. "Force," "mass," and "acceleration" are concepts associated with the principle above. They derive meaning from the principles that govern them.

**Processes** are repeatable sequences of steps that apply concepts according to principles to accomplish something. Computing the net force on an object given its components is a process.

**Functions** are specific executable implementations of processes in particular contexts, the most concrete level, tied to specific values and conditions.

The inference value of this hierarchy is that a system that holds a principle can answer questions that fall within the principle's scope even without a matched example. It generates the answer from the rule, with no need to retrieve a memory. A system that only has examples must find a similar one; if no similar example exists, retrieval fails or returns something misleading.

In practice, across the 10 subject domains and 192 learning phases we tested Helix against (spanning mathematics, physics, chemistry, biology, and engineering), the principles-first structure produced correct inferences on novel problems at a substantially higher rate than retrieval-only approaches. The gap was largest on problems that were phrased differently from training examples but were logically equivalent, which is exactly the distribution shift that retrieval struggles with.

## Dependency-Ordered Curriculum

The second structural decision that shaped Helix was enforcing learning order by logical dependency.

You cannot reason about electromagnetism without a working model of calculus. You cannot understand thermodynamic entropy without first understanding energy, work, and heat. These prerequisites are logical dependencies: the later knowledge is defined in terms of concepts established by the earlier knowledge. Ingesting later material before earlier material produces a knowledge graph where the edges are present but the nodes are not semantically grounded.

In Helix, before any domain is ingested, its foundational dependencies are mapped explicitly and checked against what has already been learned. A physics domain that depends on differential calculus is not ingested until the calculus principles are established. This sounds simple, but it requires treating the curriculum as a dependency graph, and it means ingestion order is determined by logical structure even when something later in the sequence looks more interesting or immediately useful.

The practical consequence is that the knowledge graph is coherent: every principle at a higher level of abstraction is grounded in the principles at lower levels, and inference can proceed through the dependency chain without stopping at the first gap.

## Relearning at Phase Granularity

One of the more counterintuitive decisions in Helix was the choice to relearn at phase granularity in place of targeted corrections to individual knowledge entries.

When a user identifies an incorrect piece of knowledge (the system gave an answer that was wrong, or drew an inference that did not hold), the instinct is to find the specific incorrect entry and correct it. This surgical approach is efficient in terms of what gets touched, but it does not account for the fact that the incorrect entry was likely used as context when extracting subsequent entries. Correcting the entry in isolation leaves the downstream entries that were built in the presence of the error intact.

Relearning the entire phase that produced the error re-extracts all entries in that phase from corrected source material, using correct context throughout. The phase's contribution to the downstream knowledge graph is rebuilt from scratch. This is more expensive, since it re-processes more than strictly necessary, but it produces a coherent result. The surgical alternative leaves a graph with an internal seam where corrected nodes sit next to nodes that were built assuming the old, incorrect value.

The implication is that the granularity of human correction should be coarser than the granularity of individual facts: identify the source material that was wrong, correct it, and trigger re-ingestion of the affected phase. This is a different interaction model than typical knowledge management systems, but it respects the dependency structure that makes inference possible.

## Where This Architecture Applies Beyond Learning Systems

The principles-first hierarchy and dependency-ordered ingestion are patterns that apply to AI knowledge systems well beyond dedicated learning engines.

Any AI system that needs to reason about a structured domain (legal analysis, medical differential diagnosis, financial modeling, engineering analysis) can benefit from a knowledge representation that captures the logical structure of the domain in addition to its surface content. The retrieval-first model works well when the task is information lookup. When the task involves applying domain logic to novel situations, the logical structure of the knowledge matters.

The tradeoff is construction cost. Building a principles-first knowledge graph requires understanding the dependency structure of the domain, which is a significant knowledge engineering investment. For domains where that investment has already been made (scientific subjects with well-established curriculum sequences, legal domains with clear precedential hierarchies), the structure is largely available and the work is extraction and encoding. For less structured domains, the dependency mapping is itself a significant part of the work.

Whether the investment is warranted depends on whether the task requires inference or retrieval. For inference-heavy tasks in structured domains, we found the architecture pays off in answer quality and in the honesty of failure modes. For retrieval-heavy tasks in unstructured domains, the simpler embedding approach is often the more practical choice.
