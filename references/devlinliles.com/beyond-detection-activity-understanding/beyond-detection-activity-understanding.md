---
type: Reference
title: "Beyond Detection: Activity Understanding"
resource: "https://www.devlinliles.com/beyond-detection-activity-understanding/"
author: "Devlin Liles"
published: '2026-09-03'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Object detection answers one question: what is in this frame. A person, a car, a hard hat, a face. That question is now cheap to answer. Earlier posts in this arc covered detection running directly on camera hardware, recognition models identifying specific people and plates, and re-identification tracking the same actor across cameras that never shared a field of view. All of that is real, deployed, and increasingly commoditized.

The question everyone actually wants answered is different. It's what is happening. Did the loading sequence run in the right order. Did that interaction between two people look like a normal handoff or something else. Is this a workflow completing correctly or one falling apart in real time. That's a much harder question, and I want to be direct about how much harder, because the gap between "we detect objects" and "we understand what's happening" is where a lot of vendor claims quietly overstate what the technology does today.

## What activity parsing actually is

The research field working on this problem calls it activity parsing: temporally segmenting and classifying activities, sub-activities, and atomic actions in video, combined with instance-level understanding of the specific actors and objects involved and how their actions relate to each other. Read that definition twice, because every clause in it is doing work that object detection doesn't have to do.

Object detection is a single-frame problem. You run a model on a frame, it draws boxes, done. Activity parsing has to hold state across time, decide where one activity ends and the next begins, and track which specific actor did which specific action to which specific object, not just that "a person" and "an object" appeared somewhere in the scene. Then it has to reason about the relationships between multiple actors and objects at once, because most real activities aren't one actor performing one action in isolation. They're two or three actors coordinating, handing something off, or reacting to each other.

The clearest concrete example of this research direction is MOMA, Multi-Object Multi-Actor Activity Parsing, a benchmark and dataset that came out of Stanford, along with its follow-up, MOMA-LRG, Language-Refined Graphs. MOMA represents complex human activities as activity graphs and can translate those graphs into natural-language descriptions of what's happening in a scene. The representation it introduces is called an action hypergraph: a spatial-temporal graph where an edge can capture a higher-order relationship among several actors and objects at once, not just a relationship between two of them.

That last distinction matters more than it sounds like it should. A standard graph edge connects two nodes. A hypergraph edge can connect three, four, or more nodes in a single relationship. If three people are jointly loading a pallet, a pairwise graph forces you to describe that as three separate two-person relationships and lose the fact that it's one coordinated action. A hypergraph can represent the whole group action as a single structure. That's the right representation for the problem. It's also a research representation, tested against a benchmark dataset, not something you install on a Jetson board next to your object detector.

## The honest maturity gap

Here's where I want to slow down, because this is exactly the kind of claim that gets oversold in a sales deck. Object detection is a shipped commodity. Frigate-class tooling runs it on cheap hardware in production today, across thousands of deployments, and I covered that in an earlier post in this arc. PPE and safety compliance detection has multiple commercial vendors competing on it right now. Recognition and re-identification are real products with real accuracy numbers you can benchmark against.

Activity parsing isn't at that stage. MOMA and MOMA-LRG are research artifacts: a benchmark, a dataset, and a graph representation that researchers use to measure progress on the problem. They are not a plug-and-play product you buy and point at a camera feed. The gap between "detect an object" and "parse a multi-actor activity and describe what's happening, in language, across time" is still substantially a research problem. It is closing, the way every hard CV problem eventually closes, but it hasn't closed yet, and anyone telling you otherwise is selling you something.

This is where I'd push back hard on a specific category of vendor claim. When someone says their platform does "workflow understanding" or "activity recognition," ask exactly one question before you believe any of it: what task is this actually solving. There are two very different answers, and they get marketed with the same words.

The first answer is a sequence of pre-defined states, detected individually and chained together with logic you wrote. Person detected in zone A, then object detected leaving zone B, then vehicle detected at the exit, in that order, within some time window. That's achievable today. It's essentially a state machine, driven by a chain of individual object detections you already have from earlier stages of your pipeline. It works well, it's explainable, and you can debug it when it's wrong, because every state transition maps to a specific detection event you can inspect.

The second answer is open-ended multi-actor activity parsing, with no pre-defined script: the system watches a scene and infers what kind of activity is unfolding among however many actors are present, using whatever relationships apply. That's the MOMA-style research frontier. If a vendor's claim only holds up under the first definition but gets marketed with language that implies the second, you're going to build a project plan around a capability that doesn't exist yet. Get uncomfortably specific before you believe an activity-understanding claim. Ask what benchmark, what dataset, what actor count, what's the failure mode when the scene doesn't match the expected script.

## What to build today

None of this means workflow-level checks are out of reach right now. They're not. You just have to build them at the right layer, using the primitives this arc has already covered, without waiting on an end-to-end model that understands activity the way MOMA's benchmark defines it.

Two patterns cover most of what teams actually need. The first is sequence verification: confirming a multi-step procedure happened in the right order. A loading dock sequence where a vehicle has to arrive, a gate has to open, a person has to badge in, and cargo has to move in that specific order. A safety checklist where each step has to be completed before the next one starts. You already have the building blocks for this from earlier posts: object detection tells you when each step's trigger condition fires, and a rules layer on top decides whether the sequence matches the expected order and flags it when it doesn't. That's a state machine, not an activity-understanding model, and it's exactly as reliable as the individual detections feeding it.

The second is anomalous interaction flagging: using re-identification to keep track of two specific actors across a scene, then applying a rule that flags when their interaction doesn't match an expected pattern. Two people who've never appeared together before spending an extended period at a restricted access point. A tracked actor's movement pattern deviating sharply from their historical baseline. These are still built from detection and re-identification outputs feeding a rules layer, not a single model that watches the interaction and understands it the way a human observer would.

The direct recommendation: build your workflow-level checks now, as a rules and state-machine layer sitting on top of the detection and re-identification primitives you've already got from earlier stages of this pipeline. Don't wait for an end-to-end activity-understanding model to mature, and don't over-trust a vendor claim that implies you already have one. The rules layer is less elegant than "the AI understands the workflow." It's also something you can build, test, and debug this quarter, with technology that already works.

The research direction is real and worth tracking. MOMA-LRG's move toward natural-language descriptions of activity graphs points at where this eventually goes: systems that can narrate a scene the way a human security operator would, across arbitrary numbers of actors, without a pre-scripted state machine underneath. When that capability ships as a product with benchmarked accuracy you can evaluate, it'll be worth another post. Until then, the state machine on top of detection and re-identification is the honest answer to "how do we verify this workflow," and it's the one I'd build.
