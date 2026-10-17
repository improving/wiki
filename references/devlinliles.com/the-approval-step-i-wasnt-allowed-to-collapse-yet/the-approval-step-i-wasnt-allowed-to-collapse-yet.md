---
type: Reference
title: "The Approval Step I Wasn't Allowed to Collapse Yet"
resource: "https://www.devlinliles.com/the-approval-step-i-wasnt-allowed-to-collapse-yet/"
author: "Devlin Liles"
published: '2026-10-14'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built an onboarding workflow for new-hire access provisioning that had to survive a redesign, and I want to walk through what happened when I gave in to the obvious speed win. The existing human process was sequential: a manager signs off that a new hire needs access to certain systems, then a separate compliance reviewer signs off independently, checking for things a manager wouldn't necessarily know to look at, like contractor access rules or a restricted-system flag on a role that looks ordinary on paper. Two people, two checkpoints, each looking at a different question.

I had the workflow running at a stage where the individual steps had already proven stable on their own, and the redesign question that came up next was whether to wire those two sign-offs together into a single combined approval. The pitch for doing it wrote itself: infer compliance clearance from the manager's own sign-off context, skip the second human loop entirely, cut provisioning time by however long that second review used to take. It looked like exactly the kind of consolidation a workflow chases once it has earned some trust.

I built a test set of thirty-five synthetic new-hire cases to check the idea before shipping it, and I made sure ten of them had a compliance-only exception baked in, the kind of case where the manager's sign-off looks completely normal and the compliance flag is the only thing that would have caught the problem. Run the collapsed approval against those thirty-five cases and the violation rate on the flagged ten came in above seventy percent. The combined step had no way to see what the second human reviewer used to see, because nothing about a manager's sign-off context actually encodes contractor restrictions or system-level compliance flags. The collapsed workflow provisioned access in violation of policy on the majority of exactly the cases it was never equipped to catch.

## The pattern

What I ended up building instead was a fidelity checker that sits in front of any proposed workflow redesign and compares it against a documented map of the current human process. The map records what each checkpoint in the existing process actually checks for, not just that a checkpoint exists. When a proposed redesign collapses or reorders those checkpoints, the checker blocks it, unless the team can produce logged evidence that the combined step matches human-level accuracy on the specific thing the collapsed checkpoint used to catch.

For the onboarding case, that meant the two sign-offs stayed separate, wired as two distinct calls in sequence rather than one inferred step, all the way through the stage where the redesign was first proposed. The workflow was allowed to get faster in every way that didn't touch what each checkpoint independently verified. Only once the team had a body of evidence, logged and reviewed, that a combined step caught the same compliance-only exceptions the separate reviewer used to catch, did the fidelity checker unlock the collapse. Run the same thirty-five cases through that gated version and the violation rate on the flagged ten drops to near zero, because the compliance question is still being asked by something that has actually earned the right to answer it.

The rule underneath this is simple to state and easy to skip under a deadline. Hold a workflow to the shape of the process it's replacing until the evidence says a shortcut preserves what that shape was protecting. A human process that looks slow from the outside is very often slow because it's checking more than one thing, and a redesign that measures speed without first identifying what each step protects is measuring the wrong variable.

## Design considerations

This pattern costs something real, and I don't want to describe it as a free efficiency win with a safety net attached. Holding two sign-offs apart when there's fair confidence they could be inferred from each other means leaving a known speed gain on the table for as long as it takes to earn the evidence that justifies collapsing them. That's a deliberate trade of velocity for verified fidelity, and a team under a real deadline feels that cost immediately, long before it feels the benefit of having avoided the compliance violation nobody has hit yet.

The whole mechanism also depends on something that's easy to assume exists and often doesn't: an accurate, current map of what the human process actually checks at each step. I built the fidelity checker against a documented process map, and the checker is only as honest as that map. If nobody ever wrote down precisely what the compliance reviewer was actually looking for, distinct from the manager's sign-off, the checker ends up comparing a proposed redesign against a description of the process that was already wrong before the redesign existed. Getting that map right takes sitting with the people who do the checking today and asking what they'd catch that the other checkpoint wouldn't, which is a slower and more human step than most teams expect a governance mechanism to require.

There's a real question about how long to hold the line. I don't think fidelity to the existing human process should be permanent policy forever. It's a ceiling that should lift once a team has genuinely earned the evidence, not a wall meant to freeze the workflow in its current form indefinitely. The failure mode on the other side of this pattern is a team that builds the fidelity checker, treats it as done, and never actually goes and earns the evidence that would let it advance. A gate that never opens is just a different kind of missed opportunity, only this one comes wearing the label of caution instead of the label of speed.

The organizations that eventually redesign a workflow around what the technology can actually verify are the ones who see returns that outpace everyone still bolting automation onto an unchanged process, the old process left standing exactly as it was. Earning the right to diverge and actually diverging once that right is earned are two different disciplines. This pattern only ever covers the first one.
