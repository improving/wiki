---
type: Reference
title: "One Clause at a Time - Previewing Every Edit Before It Commits"
resource: "https://www.devlinliles.com/one-clause-at-a-time-previewing-every-edit-before-it-commits/"
author: "Devlin Liles"
published: '2026-10-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built a contract-redlining agent for legal-ops that reviewed vendor-contract clauses and proposed edits: tightening a liability cap here, adding a termination-for-convenience clause there. The first version I shipped auto-applied every proposed edit directly to the working document. There was no preview step of any kind. The user found out what the agent had changed by opening the contract after the edit had already landed, which is backwards in a way that only becomes obvious after watching it happen a few times.

I ran it against fifteen synthetic contract clauses, and I deliberately seeded five of them with a plausible-but-wrong edit: a defined term misread, a liability figure applied to the wrong section. All five went straight into the document exactly like the correct ten did, because the agent had no mechanism that distinguished confident-and-right from confident-and-wrong before committing. A later manual pass eventually caught all five, but only after the fact, after the wrong language had already been live in the working document for however long it took someone to notice.

What struck me watching legal-ops react to this was what happened to their trust in the other ten edits, the ones the agent got completely right, once the five bad ones surfaced. Once a team catches an agent auto-applying wrong edits even a handful of times, it stops trusting the output as a category. The distrust spreads past the specific clauses that were actually wrong and settles over everything the agent touches. There was never a moment where a human could catch a mistake before it became a mistake that had already happened, and that absence is what did the damage. Being wrong five times out of fifteen is a correctable error rate. Being wrong five times out of fifteen with zero visibility before the fact is a trust problem that outlives the fix.

## The pattern

The fix was to stop letting any proposed edit write directly to the document at all. Every proposed edit now surfaces as a clause-level diff, the exact before-and-after language, shown to the user before anything commits. The agent still does the same work of reading the clause and drafting the change. What changed is that drafting and committing are no longer the same action. Committing requires an explicit approve or reject from the person who owns the document.

Run the same fifteen clauses through that version and all five of the injected-wrong edits get caught and rejected at the preview stage. None of them ever reach the working document. The post-hoc correction rate, the thing I was measuring before, drops to zero. A wrong edit no longer gets the chance to become a fact anyone has to walk back once nothing commits without a look first. The correct ten clauses still move through in roughly the same time it took before, because approving a correct diff is fast. The five wrong ones now cost a rejection instead of a correction, and a rejection is cheap precisely because nothing happened yet.

The deeper idea here is that trust in an autonomous system isn't a single decision made once, at the moment it goes live. It's earned one visible action at a time, and the only way to earn it that way is to make each action visible before it's final. An agent that commits first and explains later is asking for trust on faith. An agent that shows its exact next move before anything commits is offering something a team can actually verify, and verification is what rebuilds trust after an auto-applied mistake.

## Design considerations

This pattern solves a narrower problem than it might look like, and it's easy to conflate it with something adjacent. It decides whether a specific proposed action is correct before that action becomes real. It says nothing about volume, and volume is exactly where the pattern's own success creates a new problem: review fatigue. A preview step only does its job if someone actually reads it, and a human who has approved two hundred correct-looking diffs in a row is exactly the person most likely to reflexively approve the two hundred and first without reading it closely. I've watched this happen. The mechanism that earns trust through repetition is the same mechanism that, given enough repetition, teaches people to stop paying attention. This pattern makes a wrong edit visible before it commits. It has no way to guarantee that visibility gets used.

There's also a real cost to interrupting every single action for approval, and that cost doesn't disappear just because the pattern is working. Fifteen clauses is a small enough batch that per-clause approval barely registers as friction. A contract-redlining agent running against a few hundred clauses a week is a different proposition, and at that volume the preview step itself becomes the bottleneck the agent was supposed to relieve. The pattern doesn't say when to graduate from per-action approval to something coarser, like batching low-risk clause types together or sampling a subset for review instead of reading every one. That calibration question sits entirely outside what this pattern solves, and skipping it means trading one failure mode, silent bad edits, for a different one, a review queue nobody can keep up with.

The clearest sign this pattern is working is boring, and I mean that as a compliment. It looks like a steady stream of quick approvals punctuated by the occasional rejection that clearly explains itself. The moment it starts looking like ceremony, a box getting checked without anyone reading what's inside it, the pattern has stopped doing the thing it exists to do, even though every log entry still says the approval happened.
