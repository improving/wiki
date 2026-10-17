---
type: Reference
title: "Short, Bounded Pipelines - Trading a Seamless Run for a Shorter Leash on Drift"
resource: "https://www.devlinliles.com/short-bounded-pipelines-trading-a-seamless-run-for-a-shorter-leash-on-drift/"
author: "Devlin Liles"
published: '2026-10-12'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

Ask a travel-planning agent to plan a five-day trip end to end in one uninterrupted run: interpret the traveler's preferences, search flights, search hotels, search a car rental, build a daily activity itinerary, check the result against a budget cap, reconcile schedule conflicts, and produce a final booking-ready itinerary. Seven or eight steps, one long chain, no checkpoint until the very end. I ran this against twenty seeded trip requests, each with a known feasible itinerary I could check the output against, and what came back is compounding error wearing a nicer suit and calling itself autonomy.

Every individual step looks reasonable in isolation. A flight really is a real flight out of the available inventory. A hotel really is a real hotel with real availability. The problem shows up early and gets discovered late. A small misread near the start, the traveler's dates get interpreted one day off, a budget figure gets read in the wrong currency, never gets checked against anything until the final reconciliation step runs. By the time reconciliation happens, correcting that early misread means unwinding four or five downstream choices that were all built on top of it: the hotel booked for the wrong dates, the car rental that no longer lines up, the activities scheduled around a window that was never right to begin with. I track how many downstream steps had to be silently re-derived whenever an early input turned out wrong, as a direct stand-in for how expensive the eventual fix turns out to be, and that number is where the real cost of this design lives.

The instinct to build it this way is understandable, because a single uninterrupted run looks like the more capable system to whoever is watching the demo. But a longer chain with no checkpoint fails more often, and when it fails, it fails invisibly, because nothing along the way is positioned to notice a mistake before it becomes load-bearing for everything built after it. Autonomy is a good look right up until it's the reason nobody caught the problem on day one.

## The pattern

The fix is to stop treating the whole trip as one continuous run and break it into short stages, each one ending in a real checkpoint before the next stage is allowed to start. Four stages instead of one long chain: interpret preferences and confirm the dates and budget back to the traveler before anything else happens; search flights and a hotel, checked against what got confirmed in the first stage before proceeding; handle the car rental and activities, checked against the actual booked times from the second stage rather than an assumed schedule; run final reconciliation, which now only has to catch conflicts that are genuinely new, instead of unwinding three stages of accumulated drift.

State passes explicitly from one stage to the next instead of riding along implicitly inside one long chain of reasoning. That detail carries most of what makes the pattern work. When a stage hands off an explicit, checked value, the next stage can look at exactly what it received and decide whether to trust it. When state just carries forward inside a single continuous run, there's nothing to inspect between the point where an error happened and the point where it finally surfaces.

Four stages take more round trips than one seamless run, and it looks less impressively autonomous doing it. I take that trade every time, because what I get in exchange is that an error gets caught and corrected inside the stage that produced it, before it has the chance to become load-bearing for a stage built on top of it. Across the same twenty trip requests, the difference shows up directly in how often the final itinerary matches the known feasible answer without requiring rework, and in how much rework it takes on the runs where something does slip through.

There's a specific reason chain length itself, independent of any single step's accuracy, is dangerous here. Reliability degrades as a smooth function of how long a task runs; it rarely fails cleanly at one identifiable step. An agent given enough uninterrupted length starts losing track of the original objective and can fall into repetitive, unproductive loops, a failure shape that doesn't announce itself the way a single wrong field does. Bounding the pipeline into short stages is a direct structural answer to that specific finding. It caps how long any single stretch of unchecked reasoning gets to run before something actually inspects it.

## Design considerations

What this pattern buys you is narrower than it might sound. It narrows the blast radius, limiting how far an error can travel before the next checkpoint gets a chance to catch it. A stage that's itself doing several steps of work still carries its own internal risk of the exact same compounding math. Four bounded stages of two steps each still let a bad value multiply its way through; the difference is that it happens in smaller, more frequently checked doses. The pattern buys a shorter leash on how much accumulated drift a single unchecked stretch can produce, and that leash is real: an error gets caught closer to where it happened, before it multiplies further. Whether an individual stage got the right answer on its own is a separate question this pattern leaves standing.

The calibration question I keep coming back to is how short is short enough. Cut the pipeline into stages too fine and the round trips start costing more than the drift they're preventing, especially on steps that are genuinely low-risk. Leave the stages too long and the original problem comes back at a smaller scale: four long unchecked stretches instead of one. My rule of thumb is to draw the boundary at the point where a downstream decision would become expensive to unwind if an upstream input turned out wrong, which is exactly why confirming dates and budget happens before a single flight gets searched rather than after. The boundary belongs wherever the cost of discovering a mistake jumps.

A good enough model, the objection goes, eventually makes checkpoints unnecessary. I don't buy it. The finding underneath this pattern describes what happens to an objective held in an agent's working attention over a long enough stretch, regardless of how capable the model is at any single step along the way. A bigger model can still drift over twenty uninterrupted steps. It just drifts more competently while doing it, and competent drift is harder to notice than an obvious mistake.
