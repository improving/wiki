---
type: Reference
title: "A Person and a Pipeline Are Asking the Same Question"
resource: "https://www.devlinliles.com/a-person-and-a-pipeline-are-asking-the-same-question/"
author: "Devlin Liles"
published: '2026-08-24'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every organization that has moved past a single AI pilot runs into the same inventory problem: a growing pile of prompts, agents, and model versions spread across teams, with no reliable way for a person or a system to find the right one on demand. Left alone, that gap turns into duplicated work at best and an agent invoking something stale or unauthorized at worst. The problem shows up in two places, and most organizations only build for one of them.

Ask a person which agent handles invoice reconciliation. Then ask a workflow engine the same question in machine terms: give me the current, healthy, authorized version of the invoice-reconciliation skill. Those two answers should be identical. In most organizations building an AI asset library right now, they come from two different systems, and nobody has checked whether the systems agree.

That gap starts as a reasonable-sounding requirement. Give people and chat interfaces a way to find the right prompt, agent, or model by describing what they need in plain language. Give platform services and automated workflows a way to resolve and invoke the right asset at runtime, dynamically, inside a pipeline. Written down as two bullets, this reads like two projects: a search UX problem and a systems problem. Staff it that way and the org chart will agree completely. One team builds a chat interface over a metadata store. Another team builds a service registry for the orchestrator. Different backlogs, different demo days.

They are the same question, asked by two different actors on two different clocks. A person typing "which agent handles invoice reconciliation" into a search box is doing capability resolution on a human clock: seconds, exploratory, forgiving of an imperfect match because a person will read the result and decide. A workflow engine asking for the current, healthy, authorized version of that skill is doing capability resolution on a machine clock: milliseconds, exact, with no one in the loop to catch a stale or unauthorized answer before it executes. Same underlying operation. Different tolerance for being wrong.

Treat those as two systems and drift follows, and drift here isn't a hypothetical failure mode. It's the default outcome of how this work usually gets staffed. The team that owns the chat interface maintains its own description of what an asset does, tagged and embedded for semantic search. The team that owns the runtime registry maintains its own record of what's deployed, versioned and health-checked for invocation. Nobody owns the fact that these are supposed to be the same fact, described twice. Six months in, the chat UI recommends a prompt version that engineering deprecated last sprint, or the orchestrator is quietly running a model the compliance catalog says was retired. The two truths didn't diverge because anyone made a mistake. They diverged because there were two truths to begin with.

Building a better UI and a better registry, then wiring them together after the fact, only hides that problem for a while. The fix starts earlier, in recognizing that both systems are reading the same underlying object: an asset's identity, its capability description, its version, its owner, its current health and authorization status. The chat interface and the orchestrator are two lenses over that one object, not two products that happen to cover related ground. Design the object once, expose it through a semantic index for people and a resolver for machines, and the two systems can't drift apart because there's only one place the truth lives.

That's where this kind of build actually needs rigor. Vendor selection for the catalog and framework selection for orchestration are the easy, reversible decisions. The harder question is whether the team building the search experience and the team building the runtime invocation layer are working off one shared capability contract, or maintaining two independently owned descriptions of the same thing that will look identical on day one and diverge by the second release.

Two older fields already fought through pieces of this problem, from opposite directions, long before AI assets needed discovering. Classic knowledge management spent two decades learning how to make a catalog something a person, and eventually a model, could actually query. Distributed systems spent the same two decades learning how to make a name resolve to something that's actually healthy, current, and authorized to be called. Neither field was built with AI assets in mind. Both of them, it turns out, were building toward exactly this problem.
