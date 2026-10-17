---
type: Reference
title: "Seven Out of Ten Stopped Meaning What It Used To"
resource: "https://www.devlinliles.com/seven-out-of-ten-stopped-meaning-what-it-used-to/"
author: "Devlin Liles"
published: '2026-10-10'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I watched a marketing-copy pipeline auto-approve AI-generated ad copy for publication whenever an LLM judge scored it seven out of ten or higher on being on-brand and high quality. Anything under seven went to a human review queue. That threshold had never been checked against an actual human's opinion before it went live. It just felt like a reasonable cutoff on a ten-point scale, the way most thresholds get chosen.

I ran a hundred and twenty samples of ad copy against five independent human raters and built a consensus score for each one, the kind of ground truth the judge should have been checked against from day one. Measured against that consensus, the judge's agreement was already mediocre before anything else went wrong: a Cohen's kappa under 0.5, which is the statistical way of saying the judge and the humans were often looking at the same copy and reaching different verdicts. That's the quiet failure mode nobody notices, because the judge still returns a number, the number still crosses or misses the seven, and the pipeline still moves.

Then the underlying judge model got swapped, the kind of routine vendor upgrade that happens on its own release schedule and rarely gets announced as a big event. Nobody recalibrated anything afterward, because nobody had built calibration into the pipeline as a step that had to happen. Agreement with the human raters got measurably worse. The new model was scoring on a subtly different internal scale, and the seven-out-of-ten threshold that had been tuned, loosely, against the old model's scale now meant something else entirely against the new one. Misapproved copy, the ad copy a human rater would have rejected but the judge waved through anyway, climbed past fifteen percent. No alert fired, because nothing in the system was watching for that gap. The dashboard kept showing approvals happening. It just wasn't showing what those approvals were actually worth anymore.

## The pattern

The fix here has nothing to do with picking a smarter judge model. It's a rule that no judge gets to serve auto-approve decisions until its scoring has actually been checked against what humans think, and that check has to run again every time the judge changes underneath the pipeline.

The mechanism has two parts. First, a calibration pass fits a mapping from the judge's raw score to the human-consensus score, an isotonic regression against the same rated set I described above, so the seven-out-of-ten cutoff means the same thing in practice that it was supposed to mean on paper. Second, a calibration gate blocks any judge model, new or old, from approving anything until its measured agreement against the human set clears a real threshold, kappa at or above 0.65 in the version I built. The judge-model swap that broke the original pipeline now triggers that same calibration pass automatically before the new model gets to approve a single piece of copy. A new judge version never inherits the old version's calibration mapping. There's no reason to assume it scores on the same internal scale just because it happens to be replacing the model that did.

Run that fixed version against the same swap and the numbers hold. Agreement stays above the threshold before and after the model change, and misapproved copy drops to somewhere near the floor the five human raters already disagree with each other at, which is the natural ceiling no automated judge can beat, because that's the noise already baked into human judgment itself.

What I found interesting once I looked at how production teams are actually running this in 2026 is that the swap-triggered recalibration I'd built wasn't the whole picture. Teams are now running the calibration job on a scheduled cadence even when no swap has been detected, because a vendor can update the judge model silently, no version bump, no changelog entry, nothing that would trip a swap-detection check. Calibration drift, in the language the field is using for it, is a moving target rather than a one-time fix. That's a real gap in how I'd originally scoped this: recalibrate on swap assumes the swap always announces itself, and current practice has already run into cases where it doesn't.

## Design considerations

Calibration is only ever as good as the gold set it's calibrated against, and that's a limitation baked into the whole approach rather than a bug in any particular implementation of it. Five raters and a hundred and twenty samples is a small, narrow panel, and a judge tuned to agree with exactly those five people risks learning their particular blind spots as if those blind spots were quality itself. If all five raters share a soft spot for a certain tone, or a shared blind spot for a certain kind of subtle brand violation, the calibrated judge inherits that shared error and gets certified as correct for reproducing it faithfully. A calibrated judge matches its graders. That's the whole claim calibration is entitled to make, and it says nothing about whether the graders were right to begin with. Scaling the rater panel, or rotating in fresh raters periodically, is the only real defense against that, and it costs real money every time.

The cadence question is where I spend most of my actual calibration effort now. Recalibrating only on a detected swap is cheap but blind to silent drift. Recalibrating on a fixed schedule regardless of whether anything changed costs more in review time but catches the vendor updates nobody announced. I've settled on running the scheduled check monthly for anything auto-approving customer-facing output, and treating any kappa drop below the threshold, swap or no swap, as the same kind of incident. The cost of that discipline is real reviewer time spent re-rating a portion of the gold set on a schedule, month after month, whether or not anything visibly breaks in between.

The other place this pattern has a hard edge is scale of the auto-approve decision itself. A calibration gate makes sense when the judge is standing in for a specific, bounded quality question, on-brand, meets a length constraint, avoids a banned claim, because that's a question a small human panel can actually adjudicate consistently. It gets shakier the more the judge is being asked to render a broad, holistic verdict that different human raters would reasonably disagree about even among themselves. In that situation, a low measured kappa might not mean the judge is broken. It might mean the underlying question doesn't have a single right answer for five different people to converge on, and no amount of calibration fixes a target that was never actually fixed to begin with.
