---
type: Reference
title: "The Box That Already Shipped - Rollback by Reversibility Type"
resource: "https://www.devlinliles.com/the-box-that-already-shipped-rollback-by-reversibility-type/"
author: "Devlin Liles"
published: '2026-10-16'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built an internal IT helpdesk agent, running against the same kind of Intune and Entra ID stack we use at Improving, to provision a laptop for a new hire. Three things happen in sequence when it runs: it writes a line to a provisioning audit log, it toggles the device's Intune compliance policy assignment, and it triggers a hardware shipment request to a fulfillment vendor. I seeded fifty runs of this flow, each one built to fail partway through, and each failure triggered a rollback attempt.

The only rollback mechanism I gave this version was one function, applied identically no matter what it was undoing. For the audit log write, that's fine. Deleting a line from a file is a complete, honest undo. For the Intune policy toggle, the same function called the same API in reverse and reported success, except the underlying system has realistic propagation delay, so the policy sometimes had not actually reverted by the time the agent claimed victory. For the shipment, there is no reverse call that means anything. A physical box, once packed and handed to a carrier, does not come back because a function returned a success code. The generic undo handler called a cancel-shipment endpoint anyway, read back whatever status it got, and reported rollback successful regardless of whether the warehouse said the box had already left the building.

I put a dashboard next to this run that showed what the agent reported alongside what the underlying system actually recorded, colored red on any mismatch. Across the fifty sessions, more than four in ten rollback attempts reported success on an action that had not actually been reversed, and nearly all of those false positives clustered in exactly the two categories where a one-size-fits-all undo function had no business declaring victory. A system that cannot tell the difference between deleting a log line and recalling a shipped box will, sooner or later, tell someone the box came back.

## The pattern

The fix is to decide, before anything runs, what kind of action each step actually is. I tag every action in the plan at design time with a reversibility class. File-state actions, like the audit log write, are cheap and safe to undo directly, so the handler just does it. Stateful-external actions, like the Intune policy toggle, can be undone, but the claim of success has to be earned rather than assumed. The handler calls the reverse operation and then polls the external system's actual state, and it only reports success once that state confirms the reversal happened, not the moment the reverse call returns. True-side-effect actions, like the shipment, get no rollback attempt at all, because none exists. Instead the handler surfaces a flag: cannot auto-reverse, human compensation required, with concrete next steps attached, like contacting fulfillment to attempt an intercept or issuing a return-to-sender once the box arrives.

The tag lives on the action itself, set when I write the step, not inferred by looking at what happened after a failure. That ordering is the entire point. By the time a failure occurs, there is nothing left to figure out about what kind of action just broke, because the answer was already decided when the plan was built. The rollback handler reads the tag and branches to one of three strategies instead of running one function against everything.

Running the same fifty sessions through this version dropped the false rollback-success rate from over forty percent to under five, and the handful of remaining true-side-effect cases never reported a false success even once. Every one of them showed up honestly as requiring a human, which is a smaller, truer claim than the uniform version was making.

## Design considerations

A reversibility tag is still a judgment call made by whoever writes the action, and the pattern is only as trustworthy as that judgment. Nothing stops someone from mis-tagging a true-side-effect action as stateful-external. If that happens, the handler will still attempt a reverse-and-poll cycle against something that cannot actually be reversed, and depending on how the underlying system responds to a call it was never designed to receive, that can produce exactly the false-success report this pattern exists to eliminate. Tagging deserves the same review a schema or a database migration gets, not a one-time pass nobody revisits.

The true-side-effect tier is where the pattern's honesty runs into its own ceiling. Surfacing cannot auto-reverse, human compensation required is a real improvement over a false claim of success, and it still hands an impossible undo to a person instead of performing it. I think that is the correct outcome, because pretending otherwise is worse, but it means this pattern reduces how often a human gets lied to without reducing how often a human has to clean something up by hand.

There is a second way to implement the first two tiers that changes the mechanics without changing the intent. Instead of a static per-action tag dispatching to a handler, you can capture a snapshot of a resource's state before any destructive action runs, then restore from that snapshot if the action later turns out to have been wrong. Same design goal, preserve the ability to undo and never falsely claim an undo succeeded, different implementation. It works cleanly for file state and for external systems where a snapshot is meaningful. It changes nothing about the true-side-effect tier. A shipped box is not a database row, and no snapshot of any system state brings it back once it has left the building.

The pattern also assumes the catalog of actions is known ahead of time, which is true for a fixed provisioning flow like mine and less true for an agent that composes new tool calls dynamically as it works. If the set of possible actions is not fixed in advance, tagging has to happen at the level of the tool itself rather than the specific call, and you lose some of the precision that made this pattern work as cleanly as it did on fifty sessions I could fully enumerate ahead of time.
