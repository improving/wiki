---
title: "Ten Nodes, Forty-Five Connections, and a Throughput Drop Nobody Modeled"
type: "Source Summary"
description: "Staffing one human overseer per agent created 45 connection pairs and dropped throughput below the single-agent baseline; bounding the team fixed it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/ten-nodes-forty-five-connections-and-a-throughput-drop-nobody-modeled/ten-nodes-forty-five-connections-and-a-throughput-drop-nobody-modeled.md"
---

# Ten Nodes, Forty-Five Connections, and a Throughput Drop Nobody Modeled — Summary

**Original source**: `references/devlinliles.com/ten-nodes-forty-five-connections-and-a-throughput-drop-nobody-modeled/ten-nodes-forty-five-connections-and-a-throughput-drop-nobody-modeled.md`

## Summary

Devlin Liles modeled a five-agent content pipeline where every agent got its own human overseer, producing ten nodes and as many as 45 potential connection pairs. Running twenty synthetic briefs through that naive topology, throughput per coordination-hour fell below the earlier single-agent baseline even as headcount rose. The proposed fix is a pre-scaling sizing calculator that bounds the human team and computes connection-point coordination cost against a deliberately chosen ceiling.

## Key Claims

- Connections among n nodes follow n×(n−1)/2, so ten nodes yield as many as 45 pairs.
- Coordination cost scales with connection points (quadratic), not headcount (linear); doubling people can quadruple coordination burden.
- The one-overseer-per-agent topology produced throughput below the single-agent baseline on the same twenty briefs.
- Two overseers covering clustered agents restored throughput to at or above the single-agent baseline with no change to the agents.
- Bounding connection points concentrates oversight, making each overseer a single point of failure for their cluster.

## Relevance

Informs [coordination overhead](/concepts/coordination-overhead.md) and [multi-agent coordination](/concepts/multi-agent-coordination.md).

## Quality

Practitioner blog post by Devlin Liles. Strengths: a concrete arithmetic frame (n(n−1)/2) and an honest account of the tradeoff. Caveats: figures come from a twenty-brief synthetic simulation, not production data.

## Entities Mentioned

- None.

## Concepts Covered

- [Coordination Overhead](/concepts/coordination-overhead.md) — coordination cost grows with connection points, not headcount
- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — overseer-per-agent topology versus a bounded cluster topology

## Related Sources

- [Check It Before It Crosses - Verifying a Claim Before the Next Agent Trusts It](/sources/check-it-before-it-crosses-verifying-a-claim-before-the-next-agent-trusts-it.md)
