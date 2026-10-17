---
type: Reference
title: "When Your Agent Books &#x27;Paris,&#x27; Is It Thinking About a City?"
resource: "https://www.devlinliles.com/when-your-agent-books-paris-is-it-thinking-about-a-city/"
author: "Devlin Liles"
published: '2026-08-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

There's a question embedded in every agentic AI system that most teams never make explicit. When the agent produces the token "Paris" while booking a flight, is its internal representation about the city of Paris — the place in France, with an airport, a time zone, visa requirements, connection logistics — or is it about the statistical neighborhood of the token "Paris" in its training data?

That distinction is not academic. It determines whether the agent books a flight to Charles de Gaulle or confidently produces a plausible-looking itinerary to a city that doesn't exist in the booking system.

Franz Brentano identified intentionality as the defining feature of mental states in 1874. Mental states are directed. They are about things. When you think about Paris, your thought has Paris as its object. It refers to something in the world. Brentano called this "aboutness," and he argued it was what distinguished mental phenomena from physical ones. A rock doesn't point at anything. A thought does.

The question of whether AI systems have genuine intentionality is what the entire grounding research agenda is trying to answer. The short answer: sometimes, in narrow domains, under controlled conditions. Not reliably. Not in the way an agent booking flights needs it to be.

In a retrieval or question-answering context, shallow intentionality is often good enough. A model generating a summary of a document has a representation of "Paris" that's sufficiently aligned with the real city that the output is useful. The task doesn't require precise world-reference. It requires coherent text about the topic the user asked about.

Agentic contexts are different. When an agent executes actions in real systems — booking flights, creating tickets, querying databases, sending communications, calling APIs — its representations have to reliably track actual world state. "Paris" has to refer to a specific airport code, a time zone offset, a set of available flights in the booking system. The representation has to be about the thing in a way that supports correct action, not just fluent text generation.

Recent research distinguishes genuine intentionality from "quasi-intentionality": a functional mimicry of aboutness that reproduces some logical features of genuine reference without grounding significance in real-world relations. Quasi-intentionality is sufficient for generating coherent text. It's not sufficient for reliable action in a real system.

The grounding research agenda — RAG systems, tool use, structured knowledge retrieval, world models — is an attempt to give model representations genuine intentionality, or at least a closer functional approximation of it. You can't fix the intentionality problem purely at the model level. You fix it architecturally, by building systems that verify representations against real-world state before acting on them. RAG retrieval connects the model's generation process to a current knowledge base. Tool verification goes further: before acting on a representation, the agent calls a tool to confirm that the representation matches real system state.

Brentano's insight maps to a specific checklist for agentic system design. Every consequential action an agent takes requires a grounding step that connects the relevant representation to current world state. Not a training-time representation of what the database contains, but an actual query against the database as it exists now. For low-stakes, reversible actions, shallow intentionality is often sufficient. For consequential, irreversible actions — booking resources, sending communications, modifying records, executing transactions — the grounding requirement is higher.

The failure mode to watch for is confident action on stale representations. An agent that says "I've confirmed the flight is available" when it's reasoning from training-time knowledge about typical flight availability is exhibiting quasi-intentionality at its most dangerous. It sounds like it checked. It didn't check. It produced text that describes what checking would yield, based on statistical patterns.

The best agentic systems treat representations as time-stamped. If the agent doesn't know when it last verified that a fact is true, it treats the fact as unverified. That's the engineering implementation of what Brentano was pointing at: the difference between a representation that's genuinely about the current world and one that's about a statistical approximation of what the world usually looks like.
