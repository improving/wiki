---
type: Reference
title: "95 Trillion Tokens of Real Agent Traffic Looked Nothing Like the Benchmark"
resource: "https://www.devlinliles.com/95-trillion-tokens-of-real-agent-traffic-looked-nothing-like-the-benchmark/"
author: "Devlin Liles"
published: '2026-09-28'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Ask whoever sold you your agent serving stack how they measured cache hit rate. Then ask them to split that number by turn boundary before you buy the pitch.

Most of what gets quoted in a vendor deck comes from a single-turn benchmark, because that is the workload the serving layer was originally built to handle: one prompt in, one completion out, cache warm the whole time because there is only one turn and one boundary, so nothing ever has the chance to fall out of it.

That is a clean assumption to build a demo around, and a bad one to build a fleet around. The paper behind this post pulled 95 trillion tokens of actual GitHub Copilot agent traffic and looked at what the workload actually does in production. That's a different picture than what the serving stack was designed to expect, and the shape that came back barely resembles the single-turn case.

Real agent sessions run long, and they run in turns. A coding session is a chain: read the file, propose a diff, run the tests, read the failure, propose another diff. Each turn appends to everything the model is carrying. By the tenth turn the context looks nothing like the context at the first turn, and neither does the cache serving it.

Cache hit rate curves across a session, and turn boundary is where that curve bends. Early turns in a session reuse almost everything, because the model is mostly re-reading what it just wrote. Deeper into a long session, tool output gets interleaved with reasoning, older context ages out of the window, and the reuse rate that looked strong at turn one stops describing turn fifteen.

A single-turn benchmark can't produce that curve, because it never runs more than one turn. It measures the point in a session where reuse is highest and reports that number as the throughput figure. Fold that into a serving estimate and every session that runs past its first exchange starts looking cheaper to serve than it actually is.

That gap lands hardest at exactly the scale this paper describes: 95 trillion tokens of production traffic behaving this way by default. Size infrastructure off a benchmark's average hit rate and the estimate is effectively built on the first exchange of every session, with the rest of the conversation assumed away.

What that points to is a specific question worth putting to any vendor's throughput claim: which turn was the number measured on? A hit rate earned entirely at the start of a session is a different product than one earned across a full multi-turn agent loop, even when both get printed on the same slide in the same font.
