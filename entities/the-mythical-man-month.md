---
title: "The Mythical Man-Month"
type: "Entity"
description: "Fred Brooks's 1975 book on software project management, source of Brooks's law: adding people to a late project makes it later."
created: '2026-10-17'
updated: '2026-10-17'
tags: [software-engineering, project-management, book]
sources:
  - "/sources/biological-coordination-patterns-applied-to-multi-agent-software-delivery.md"
  - "/sources/the-single-agent-ceiling-why-one-ai-cant-hold-your-whole-delivery-lifecycle.md"
---

# The Mythical Man-Month

Fred Brooks's 1975 book on the management of software projects, best known for Brooks's law: adding manpower to a late project makes it later, because communication and coordination costs grow faster than the work they add. In this corpus it is invoked as the standing caution against assuming that more agents, like more people, scale delivery linearly.

## Overview

The book's core insight — that coordination overhead, not raw capacity, bounds a project — reappears in multi-agent AI delivery. One post notes that coordination overhead grows faster than agent count, explicitly echoing Brooks's law, which is why [multi-agent orchestration](/concepts/multi-agent-coordination.md) needs specialization, inhibition, and checkpoint synchronization rather than more workers. The same logic underlies the [single-agent ceiling](/concepts/single-agent-ceiling.md): neither one agent nor a large undifferentiated fleet holds every competing delivery concern.

## Key Claims

- Coordination overhead grows faster than agent count, echoing Brooks's law
- Specialization is interface definition, not just role assignment
- Scope inhibition generalizes file locking to prevent conflicting parallel work
- Orchestration architecture matters more than model quality

## Related

- [Coordination Overhead](/concepts/coordination-overhead.md) — the book's central constraint, restated for agents
- [Single-Agent Ceiling](/concepts/single-agent-ceiling.md) — the modern limit Brooks's law anticipates
- [Fred Brooks](/entities/fred-brooks.md) — the book's author
- [Biological Coordination Patterns Applied to Multi-Agent Software Delivery](/sources/biological-coordination-patterns-applied-to-multi-agent-software-delivery.md) — primary source
