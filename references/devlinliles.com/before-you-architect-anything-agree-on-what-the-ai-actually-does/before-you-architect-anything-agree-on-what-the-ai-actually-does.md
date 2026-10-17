---
type: Reference
title: "Before You Architect Anything, Agree on What the AI Actually Does"
resource: "https://www.devlinliles.com/before-you-architect-anything-agree-on-what-the-ai-actually-does/"
author: "Devlin Liles"
published: '2026-07-14'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most arguments about enterprise AI are arguments about words. Someone says "we need an agent," someone else hears "chatbot," a third person is picturing a fraud model, and everyone nods. Three weeks later the architecture review reveals that nobody was building the same thing. The failure was not technical. It was taxonomic. The team never agreed on what the system actually does before deciding how to build it.

I have come to believe that a shared classification language is the cheapest, highest-leverage artifact an AI practice can own. Not because taxonomies are intellectually satisfying, though they are, but because they force the right conversation to happen first. Classify before you architect. Name the mechanism before you draw the boxes. This post is about a two-part scheme I have been using: a taxonomy that says what a model does, and an ontology that says how it is built and run. They answer different questions, and keeping them separate is most of the value.

## Mechanism first, intent second

Start with mechanism, not marketing. The taxonomy I work from has two tiers. The first tier classifies AI by what the model actually produces, and it has exactly three core families.

Predictive AI produces a forecast, probability, or label tied to a future or unobserved event. Classification, regression, time-series forecasting, anomaly detection, survival modeling, and causal inference all live here. The deliverable is a number about something you have not seen yet.

Generative AI produces a new artifact, text, code, image, audio, video, structured data, or it takes a goal-directed action. This is the most varied family and the one that absorbs the most attention. It splits into conversational, content generation, agentic, and multimodal generation. The agentic branch matters more than the others for governance, because it further splits by autonomy: informative agents that only gather and synthesize, guided agents that draft and propose but wait for a human gate, and autonomous agents that act without a per-step human approval. That single distinction, how much the system touches the world on its own, shapes risk more than any other choice inside generative AI.

Perceptive AI interprets input, pixels, waveforms, scanned documents, sensor streams, structured records, and surfaces the structured signal inside it. Computer vision, natural language understanding, speech, sensor interpretation, and pattern recognition in structured data. The deliverable is a description of what is in the data, not a forecast about a new observation.

The boundary between Perceptive and Predictive trips people up, and the resolution is intent, not data type. If the deliverable is "here are the patterns in this data," tag it Perceptive. If the deliverable is "for this new observation, here is the score," tag it Predictive. Anomaly work sits right on that line: learning what normal looks like in history is perceptive, scoring a new incoming transaction is predictive. Same math, different jobs.

This three-family split is not idiosyncratic. Industry analysts now routinely separate predictive, generative, and agentic AI, and the academic literature has been busy drawing conceptual lines between agents and agentic systems. Gartner reported a 1,445% jump in multi-agent system inquiries between early 2024 and mid-2025, which tells you the vocabulary problem is getting worse, not better, as the systems get more compositional.

## The second tier is where enterprises actually live

Here is the part people skip. The three families are mechanisms. Most enterprise value does not come from a raw mechanism. It comes from wrapping a mechanism in the structure required to act on its output. That is the second tier: applied decision patterns.

There are three. Prescriptive systems determine an optimal action or schedule under constraints, usually a predictive model feeding an optimizer or a learned policy. Recommendation systems surface a ranked list of candidates conditioned on context, almost always a predictive scoring layer feeding a ranker. Decision intelligence produces a bounded decision combining a learned model with explicit rules and economic weighting, which is what you reach for in regulated decisioning where policy is not optional.

The thing to internalize is that these are not separate kinds of AI. They are architectures layered on top of the core families. A SKU-level demand forecast feeding a mixed-integer replenishment optimizer is hierarchical forecasting plus prescriptive optimization. A claims engine is binary classification under a hybrid ML-plus-rules decision pattern. When you tag a system "prescriptive" without naming the predictive family underneath it, you have described the wrapper and ignored the engine that determines most of the operational footprint. That omission is where bad architecture decisions hide.

Generative AI is a core family rather than an applied pattern, and the reason is instructive. Its deliverable is the artifact itself or a goal-directed action, not a decision selected from candidates. That distinction keeps you from mislabeling a RAG-backed assistant as its own special category. It is conversational AI grounded by retrieval. The retrieval is an architecture choice, not a new species of intelligence.

## The ontology: orthogonal tags for how it runs

The taxonomy tells you what a system does. It tells you almost nothing about whether you can actually build and operate it. For that you need a second, orthogonal scheme. I call it the ontology, and it is a set of dimensions where every solution gets one value from each.

The dimensions cover deployment topology, latency profile, autonomy level, reasoning pattern, data sensitivity, model provenance, business domain, industry vertical, human interaction model, risk profile, evaluation approach, failure mode tolerance, input and output modality, and lifecycle stage. The point of the ontology is that it is deliberately independent of the taxonomy. A conversational agent, a time-series forecaster, and a claims adjudication system can all carry the tags edge, real-time, high-risk, regulated. The ontology is what makes the taxonomy actionable, because it surfaces the architecture and compliance constraints early, while they are still cheap to change.

Two of these dimensions deserve more attention than the rest. Autonomy level is the single largest determinant of risk, change management, and required observability. It runs from advisory through suggested, approval-gated, autonomous-audited, and fully autonomous within policy, and it maps directly onto the agentic sub-branches. Latency profile drives deployment topology, model size, retrieval strategy, and whether you can use a large foundation model at all. Sub-100ms under load almost always forces edge deployment and distilled models. Batch tolerance opens the entire design space. Answer those two tags honestly and most of the rest of the architecture falls out.

If this dimensional approach feels familiar, it should. The NIST AI Risk Management Framework organizes trustworthiness around characteristics like validity, security, accountability, explainability, and fairness, and the OECD's classification framework spans people and planet, economic context, data and input, the model, and task and output. Both are doing the same structural thing: refusing to let "what the AI does" stand in for "how it must be governed." My ontology is narrower and more engineering-flavored, but it lives in the same tradition, and it maps cleanly onto NIST and OECD when a client needs the governance crosswalk.

## Three questions that do the real work

You do not need to memorize the scheme to use it. You need three questions, asked during discovery, before any architecture conversation.

What is the deliverable? A prediction, a structured signal, a new artifact, a decision, or a ranked list. The first three name the core family. The last two name an applied pattern layered on top.

What does the applied pattern depend on? If the deliverable is a decision or a ranked list, name the core family supplying the score or signal underneath. The wrapper is not the system.

Who acts on the output, and how fast? This pins autonomy level and latency profile, the two tags that drive most of the architecture. A human-in-the-loop drafting tool with a thirty-second budget is a fundamentally different system from an autonomous sub-100ms service, even when both ship a generative model.

Sharp answers route to the right capability and the right governance. Fuzzy answers are not a signal to start building. They are a signal that the engagement is not ready to be built.

A few anti-patterns are worth naming because they recur. Treating generative AI as the only family that matters, when many of the highest-value systems are still predictive feeding a prescriptive pattern. Defaulting to full autonomy when most production agents should be guided. Skipping the risk and failure-mode tags, which are the cheapest to fill out and the most expensive to get wrong. And confusing taxonomy with architecture, the RAG-assistant trap again.

None of this is the hard part of AI. The hard part comes next, when you have to prove the system created value rather than merely ran. But you cannot measure value cleanly if you cannot say precisely what the thing is. Classification is not the destination. It is the shared map you need before the harder argument starts, which is the one about causation, and the one I will take up next.
