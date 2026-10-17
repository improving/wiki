---
type: Reference
title: "Too Dangerous to Centralize, Too Dangerous to Distribute"
resource: "https://www.devlinliles.com/too-dangerous-to-centralize-too-dangerous-to-distribute/"
author: "Devlin Liles"
published: '2026-09-25'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Mark Zuckerberg published a 6,500-word essay this month arguing that advanced AI is too dangerous to leave in the hands of a small group of people, and pledging that Meta will keep releasing open models to prove it. Four days earlier, Meta had open-sourced Muse Glimmer, a 30-billion-parameter model small enough to run on a laptop GPU. Anthropic, meanwhile, is reportedly heading toward an October IPO at a valuation some investors think understates where the company is headed, built substantially on the argument that frontier AI is too dangerous to hand out without careful control over who gets access to what.

Too dangerous to centralize. Too dangerous to distribute. Same month, same underlying technology, opposite conclusions, and both companies are right on schedule with the business case that needed each conclusion to be true.

Meta's version arrives after a year of trailing OpenAI, Anthropic, and Google on frontier benchmarks. A lab that isn't winning the capability race has an obvious reason to reframe the race itself: openness becomes the differentiator when raw capability isn't one, and every open release buys developer goodwill that a closed lab further ahead doesn't have to spend effort earning. None of that makes Zuckerberg's argument insincere. Concentrated control of transformative technology is a real question worth a real position. It does mean the position landed at the exact moment Meta most needed developers to have a reason to build on its models instead of a competitor's.

Anthropic's version runs the same play from the other side. A safety-first posture, careful access controls, and a measured rollout of dangerous capabilities are also the story that best supports a valuation resting partly on being the frontier lab that took the risk seriously. Gavin Baker made the bull case directly on this month's All-In: Anthropic is on pace to close the year around a hundred billion dollars in annualized revenue, a tenfold jump for a third straight year, and at that growth rate the reported two-trillion-dollar figure reads to him as the floor, not the ceiling. Baker runs a hedge fund with plausible exposure to exactly this trade. A bullish valuation call from an investor who benefits if the market agrees with him is a position dressed in the language of analysis, made months before any roadshow sets a real price.

I ran a version of this same argument in early August, over a different pair of dueling letters, one pushing for less AI regulation, one pushing for more. Neither had a signatory list that looked remotely neutral, and the pattern holds again here with a different cast: whenever a lab or its allies stake out a philosophical position on how dangerous AI is, the position tends to arrive exactly when that company's business needs it to be true. The philosophy is still worth reading. The technical strategy has to come from somewhere else.

The decision an enterprise actually faces, open-weight versus closed-frontier, single-vendor versus multi-vendor, is the same decision I'd walk a client through when comparing any two AI platforms: build an evaluation baseline against the organization's actual workload, then check what each option's governance architecture can and can't enforce at the boundary the organization cares about. The choice follows from that fit, with neither company's mission statement anywhere in the scoring.

Swap in "we need developer adoption to stay relevant" for Meta's stated principle, or "we need to justify a premium multiple heading into a liquidity event" for Anthropic's, and the argument reads identically either way. The philosophy and the business plan are the same document, written twice, in two different vocabularies.

That has real consequences at every level this touches. For the individual architect or technical decision-maker sitting in a vendor selection meeting, treating either company's stated mission as evidence is a category error, no different from letting a benchmark a vendor wrote itself decide which model ships to production. For the company making that selection, a stack chosen because its provider's philosophy felt right is a stack chosen for a reason that has nothing to do with whether it fits the organization's actual governance and workload needs, and that mismatch shows up later, usually at the worst time. For the industry, the louder this specific argument gets, framed as safety versus openness, the less it will actually resolve, because both sides are reciting the position their business model requires and neither has an incentive to stop before a framework neither of them has a stake in actually exists.
