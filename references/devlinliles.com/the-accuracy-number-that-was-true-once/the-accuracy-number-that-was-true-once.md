---
type: Reference
title: "The Accuracy Number That Was True Once"
resource: "https://www.devlinliles.com/the-accuracy-number-that-was-true-once/"
author: "Devlin Liles"
published: '2026-10-13'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I watched an internal knowledge-base Q&A agent launch against a RAG index built over the company's own policy documents, HR and IT material, the kind of thing employees ask about constantly. At launch, the team ran a one-time evaluation, fifty seeded question-answer pairs, and recorded 91 percent accuracy. That was the last time anyone measured it.

Ninety days later I went back and simulated what had actually happened underneath that number in the meantime. The policy corpus had been updated six times over that stretch, ordinary maintenance, new policies added, old ones superseded, exactly the kind of churn every real policy library goes through. The questions employees were actually asking had drifted too, toward topics the original fifty-pair eval set never covered because those topics didn't exist yet at launch. Real accuracy against a rolling sample of the kind of queries people were actually sending declined by at least fifteen points over those ninety days. Stale policy chunks kept getting cited after the policy behind them had already been superseded. New policy areas had zero coverage in the eval set that supposedly vouched for the whole system.

None of that showed up anywhere a stakeholder would see it. The only number anyone displayed was the launch-day 91 percent, because nothing in the system ever reran the evaluation, and nothing distinguished a snapshot taken on day one from a fact that was still supposedly true on day ninety. A number recorded once and repeated forever stops measuring anything by month three. It settles into a rumor carrying a decimal point, and it reads exactly like evidence until somebody actually checks.

## The pattern

The fix keeps the same corpus and the same query drift happening underneath the surface, because that drift is real and it's not something you can eliminate. What changes is replacing the one-time launch eval with a runner that re-scores the system on a fixed cadence, every ten days in the version I built, using two things together instead of one thing measured once. The first is a held-out question set that gets re-anchored to whichever policy chunk is currently live, so the eval tracks the corpus as it actually stands rather than quietly testing against content that already got superseded weeks ago. The second is a rolling sample of realistic, production-style queries pulled from how people are actually asking questions right now, not from how they were asking on launch day.

A drift-alert check compares each new checkpoint against a rolling baseline and fires the moment accuracy drops by a configured amount. Run that against the same ninety-day corpus and query drift from the failure case, and the alert catches the real decline within thirty simulated days of it starting. The frozen version showed 91 percent flat for the entire ninety days. This version caught the same underlying decline by day thirty, sixty days earlier than anyone would have otherwise found out, and found it as a trend on a dashboard instead of as a complaint from an employee who got a wrong answer about a policy that no longer existed.

The part of this I keep coming back to is what the loop is actually built to check. The model and the prompt stay pinned, identical the whole way through, so this was never a test of whether the model changed. The loop watches whether the world underneath a pinned, unchanged system has moved, because a system can get worse at its job without a single line of its own configuration changing, purely because the corpus and the query distribution it was built against don't hold still. Catching that requires treating accuracy as a live trend you watch continuously, not a fact you establish once and then trust indefinitely.

When I looked at how this is actually being run in production in 2026, the shape held up as the default rather than something aspirational. Teams are sampling expensive judge-based scoring on a slice of live traffic, something like five to ten percent, running cheap heuristic checks across all of it, and reserving a calibrated judge or an actual human review for whatever narrow slice is failing those heuristics, usually one to five percent of total volume. That's the identical logic underneath what I built for the policy agent, a trend instead of a frozen number, arrived at independently by people solving the cost side of running evaluation continuously rather than the design side of building the loop in the first place.

## Design considerations

A loop only catches drift at the interval it's actually built to check, and against whatever label source feeds it. My policy-Q&A version checks every ten simulated days, and a slower decline, or one that dips and partially recovers between two checkpoints, can slip through a schedule that isn't tuned to catch that particular shape of drift. Tightening the interval catches more, but it also multiplies the compute and review cost of running the eval, so the real calibration question is how much lag between a real decline starting and the alert firing an organization can actually tolerate for a given system, not some universal cadence that works for everything.

The label source is the part I trust the least by default, because it's a design choice made inside the loop rather than something the pattern hands you already solved. Judge scores, cheap heuristics, and implicit behavioral signals pulled from real usage, a user rephrasing the same question three times, an immediate escalation to a person, are all valid label sources, and each one carries its own bias into the trend line. A heuristic that only checks whether an answer cites a document at all will happily certify an answer that cites a stale, superseded document as correct, because citing something is all it knows how to check for. Get the label source wrong and the resulting trend line tracks the wrong thing with total confidence, which is arguably worse than having no trend line at all, because a wrong trend still looks like rigor from the outside.

This pattern also assumes there's a real, moving ground truth to re-anchor against, a live corpus, a real query stream. A system built against something genuinely static, a fixed historical archive nobody adds to, doesn't have drift in the sense this loop is built to catch, and running a continuous re-scoring loop against a target that truly never changes just spends compute to confirm the same launch-day number over and over. The value here is entirely a function of how much the underlying world actually moves, and knowing that in advance is what tells me whether to build this at all.
