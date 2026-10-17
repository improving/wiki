---
type: Reference
title: "Eighteen Percent, Two Models Ago"
resource: "https://www.devlinliles.com/eighteen-percent-two-models-ago/"
author: "Devlin Liles"
published: '2026-10-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built a system called DrugQA to answer pharmacist-facing questions about drug interactions, and I shipped it with an abstention gate: a mechanism that teaches the model to say "I don't know" instead of guessing whenever its own confidence doesn't clear a defined bar. One number built that gate, and it wasn't a comfortable one. On a 50-question held-out set of genuinely ambiguous interaction questions, the launch-era model gave a confidently wrong answer 18% of the time. That 18% is the entire justification for the gate's added latency, its occasional over-abstention, and the escalation routing that kicks in whenever the model won't commit.

The gate ran unchanged for two model generations after that. Nobody went back and re-measured the number. The underlying model had been swapped, upgraded, quietly replaced by a newer version from the same vendor, more than once, and the gate kept running exactly as configured, because nothing in the system ever asked whether 18% was still true.

I went and checked what that actually costs, concretely. The dashboard I inherited showed one figure: "18% (measured at launch)." Next to it sat a staleness counter that climbed with no ceiling, and a field labeled "current rate: unknown" that had never once filled itself in. The only way to get a current number was a manual endpoint that existed in the code but that nothing on earth required anyone to actually call. A system can carry a mechanism for checking its own assumptions and still never check them, if calling that mechanism depends on someone remembering to.

## The pattern

The fix is one recurring job, not a rebuild. I added a scheduler that fires the identical 50-question eval on a fixed cadence, re-running it against whichever model is actually deployed right now, and writes each run's model version, measured rate, and timestamp to a history table. Every scheduled run gets compared against the frozen 18% baseline, and the gap between them, baseline minus current measured rate, gets computed and stored alongside it.

Two dashboards can show the same frozen 18%. Only one of them plots a live line next to it: the current measured rate, tracked over time, against a shrinking necessity gap. As the deployed model improves, I'd expect that gap to narrow. No single point on that line matters much by itself. What matters is that the line exists at all, updating on a schedule I never have to remember to trigger, instead of a static number that was true once and got treated as gospel forever after.

The mechanism itself is almost insultingly simple once it's built: the same eval, the same failure definition, a fresh number, every time the job runs. No smarter model, no new metric, no rewrite of the gate. Just a decision that re-testing the assumption gets its own recurring line item on the calendar, the same way building the gate got one at launch.

## Design considerations

This pattern is only ever as good as the eval it re-runs. A 50-question set that was genuinely representative of ambiguous interaction cases at launch can drift out of representativeness as the underlying drug database changes underneath it: new interactions get documented, old guidance gets revised, and the held-out set stops covering the cases that actually matter today. Re-running a stale eval on a perfect schedule still produces a stale answer. I don't have a clean fix for this baked into the mechanism itself. It needs a second, slower-moving check on whether the eval set is still asking the right questions, which is a different job than the one this pattern solves.

The cadence itself is a real calibration question, not a detail to wave past. Too frequent and the job burns compute and review time re-confirming what the last run already showed. Too infrequent and a model swap can sit unmeasured for weeks, defeating the purpose almost as thoroughly as never re-measuring at all. I settled on a weekly run for DrugQA because that matched how often the underlying model actually changed in practice, and I'd tune that cadence differently for a system where the model or the domain moved faster.

There's also a boundary I want to be clear-eyed about: this pattern tells me whether a specific guarded failure rate has changed. It says nothing about whether the gate's original design, the confidence threshold, the abstention behavior itself, is still the right shape for a model with a genuinely different error profile than the one it was calibrated against. A model that fails less often but fails differently can clear this test cleanly while still needing a redesigned gate rather than a lower one. Necessity and correctness are two different questions, and this pattern only answers the first one.

What I keep coming back to is how little this costs to build relative to what it replaces. The alternative is an assumption nobody ever checks, sitting under a system that keeps charging users latency and escalation overhead for protection that might have shrunk months ago, or might not have shrunk at all. A number that updates costs one scheduled job. A number that never gets updated costs whatever the wrong side of that unexamined guess turns out to be.
