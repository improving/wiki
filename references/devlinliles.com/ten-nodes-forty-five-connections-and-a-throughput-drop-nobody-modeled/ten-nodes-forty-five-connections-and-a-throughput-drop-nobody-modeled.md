---
type: Reference
title: "Ten Nodes, Forty-Five Connections, and a Throughput Drop Nobody Modeled"
resource: "https://www.devlinliles.com/ten-nodes-forty-five-connections-and-a-throughput-drop-nobody-modeled/"
author: "Devlin Liles"
published: '2026-10-13'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built a five-agent content pipeline for a marketing production workflow: a research agent, a draft agent, a brand-check agent, an SEO agent, and a publish agent, each handing a piece of content to the next. Scaling that up looked like the obvious move: put a human overseer on every agent so nothing runs unsupervised. Five agents, five overseers, ten nodes total in the workflow.

I modeled the connection graph for that setup and it comes out to as many as 45 possible connection pairs among those ten nodes. That's the formula for connections among n nodes, n times n minus one, divided by two, and it turns real the moment you actually staff a team this way. Every one of those 45 potential pairs is a status meeting that might need to happen, a handoff clarification somebody has to chase down, an edit two people made independently that now conflicts and needs resolving. None of that shows up as a line item anywhere. It shows up as time.

I ran twenty synthetic content briefs through this naive topology, one overseer per agent, everybody theoretically able to talk to everybody else, and measured throughput per coordination-hour, pieces of content completed per unit of simulated coordination time. It came in below what the same team produced back when it was running a single agent with no multi-agent coordination overhead at all. Headcount went up. Agent count went up. Throughput went down. Nobody added a bad hire or a bad agent to make that happen. The team just scaled headcount by intuition, one overseer per agent felt like the responsible thing to do, without ever modeling what that topology actually cost in connections.

## The pattern

The fix is a sizing calculator that runs before the team scales, not after. It takes a proposed topology, human count, agent count, and the connections implied between them, and computes the actual connection-point count and a projected coordination-overhead cost against it. Instead of one overseer per agent, the calculator recommends a smaller, deliberately bounded human team: fewer overseers, each one responsible for a bounded cluster of agents rather than a one-to-one assignment, at an agent-to-human ratio chosen specifically to keep total connection points under a target ceiling.

For the same five-agent pipeline, that means two overseers covering clustered responsibilities instead of five people each shadowing a single agent. Running the same twenty briefs through the bounded topology brought throughput back up to at or above the single-agent-era baseline. Nothing about the agents changed. What changed is that the team stopped paying for connections nobody was using productively.

The idea runs against a pretty deep instinct, which is that more people watching more things is inherently safer. Coordination cost doesn't scale with headcount. It scales with connection points, and connection points grow quadratically while headcount grows linearly, which means a team that doubles its people can easily quadruple its coordination burden without anyone noticing until throughput is already falling. Bounding the team size deliberately, and setting the ratio on purpose rather than defaulting to one-per-agent, is the whole mechanism. It's a sizing decision made with the actual math in front of you instead of a comfort-driven headcount decision made without it.

## Design considerations

Bounding connection points concentrates responsibility, and that tradeoff is real, not a footnote to wave away. An overseer covering a cluster of three agents instead of one becomes a single point of failure for that entire cluster's oversight. If that person misses something, there's no second overseer sitting next to them who was independently watching the same work. The math that makes coordination cheaper is exactly the same math that makes any one overseer's blind spot more expensive when it happens. The calculator has nothing to say about whether that concentration is an acceptable risk for the specific stakes of the work being coordinated, and pretending it does would be dishonest about what the tool actually measures.

The ceiling itself is a judgment call, not something the model derives on its own. I set a target connection-point count and the calculator optimizes toward it, but choosing that target requires knowing something about how much coordination overhead this specific workflow can tolerate before quality actually suffers, and that's domain knowledge the connection-point math doesn't contain. A content pipeline where a bad post gets caught and fixed cheaply can tolerate a higher ceiling than a workflow where an unsupervised mistake reaches a customer directly.

This pattern also assumes the coordination overhead you're modeling is the real bottleneck, and that assumption doesn't always hold. If the actual slowdown is coming from somewhere else entirely, a slow tool, an approval queue outside the team's control, a dependency on another department, bounding connection points inside this five-agent pipeline won't move the number that's actually stuck. I'd model the topology specifically when status meetings, handoff clarifications, and conflicting edits are visibly where the time is going, and I'd look elsewhere first if they aren't.

The other honest limit is that this sizing decision is a one-time calculation applied to a static topology, and real teams don't stay static. An agent gets added, a cluster's scope quietly grows past what its overseer can reasonably track, and the bounded topology that fit at launch stops fitting six months later with nobody re-running the numbers to notice. Bounding coordination cost once is a good decision. Treating that decision as permanent is how a well-sized team drifts back into the exact unmodeled sprawl the calculator was built to prevent in the first place.
