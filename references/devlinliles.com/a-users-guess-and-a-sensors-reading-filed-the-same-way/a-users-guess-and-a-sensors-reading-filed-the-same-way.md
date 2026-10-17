---
type: Reference
title: "A User&#x27;s Guess and a Sensor&#x27;s Reading, Filed the Same Way"
resource: "https://www.devlinliles.com/a-users-guess-and-a-sensors-reading-filed-the-same-way/"
author: "Devlin Liles"
published: '2026-10-02'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# A User's Guess and a Sensor's Reading, Filed the Same Way

I built a remediation agent for an IT helpdesk that ingests facts from three sources of wildly different reliability. An end user types something like "my laptop feels slow, I think it's out of disk space." A device telemetry feed reports structured, verified sensor readings: actual disk usage, actual process activity. An admin confirmation records a human IT tech verifying that a specific fix actually worked.

## The problem

In the first version I built, all three of those sources wrote to the same fact table, with no column recording where a fact came from or whether anyone had checked it. The remediation step read that table and acted. It didn't distinguish a user's guess from a sensor's reading from a technician's confirmation, because there was nothing in the schema for it to read that distinction off of.

Across a hundred-case sample I ran, roughly a third of user self-reports turned out to be wrong about the actual cause. Disk space was fine. The real problem was a runaway background process eating CPU, which feels a lot like "I'm out of space" from the user's chair and nothing like it from the machine's own readings. Because the fact table couldn't tell a guess from a confirmed reading, the agent ran a disk-cleanup remediation on the guess just as readily as it would have on a genuinely low-disk device. Some of those cleanups ran on machines where the telemetry, sitting right there in the same table, unused, didn't indicate a disk problem at all.

Storing a user's honest but mistaken guess is fine. Users are allowed to be wrong about what's slowing their machine down; that's what a helpdesk is for. What actually breaks things is that the system has no way to act on that guess any differently than it would act on a confirmed sensor reading. A guess and a measurement go into the same slot and come out carrying the same authority, and the remediation step downstream has no way of knowing it should be more careful with one than the other.

## The pattern

The fix is to tag every fact with its source and its verification status the moment it gets written, not backfilled later once someone notices a pattern of bad remediations. Source records where a fact came from: user-reported, telemetry, admin-verified. Verification status records how much anyone has actually checked it: unverified, corroborated, verified. Both get set at write time, as part of the same transaction that stores the fact itself.

The remediation step then reads that status before it decides what to do. An unverified user self-report can still trigger something. It can prompt a follow-up diagnostic question, or kick off a telemetry check to see whether the guess holds up. What it can't do is directly trigger a remediation that only a corroborated or admin-verified fact should authorize. That's the gate: risk-appropriate action tied to how well-founded a fact actually is, applied in place of uniform action applied to everything sitting in the table.

Corroboration is what lets an unverified fact earn its way up. If telemetry independently confirms a user's report, disk usage really is high, the fact's status upgrades from unverified to corroborated, and the remediation that was blocked a moment ago becomes available. The user's report wasn't the problem. The system simply waited for a second, more reliable source to back it up before treating the claim as action-worthy.

I track a second number alongside the obvious one, because the obvious one alone can be misleading. The obvious metric is remediation-appropriateness: does the action taken match the actual root cause. The second is an over-caution rate, the share of verified-source cases that get needlessly routed to a diagnostic step instead of straight to remediation. A gate that blocks everything looks great on the first metric and terrible on the second, which is the tell that it's just maximally conservative rather than doing the harder job of separating good facts from bad ones. The gate only earns its keep when verified facts keep moving fast and unverified ones get slowed down, not when everything gets slowed down equally.

## Design considerations

The sharpest limit here is about what "verified" can even mean, and it has nothing to do with whether the pattern is implemented correctly. Provenance tagging trusts a fact based on where it arrived from and whether it's been confirmed. That trust holds exactly as long as the channel a fact arrives through is really the legitimate channel it claims to be. A support ticket that reads like an ordinary user report and a support ticket engineered to look like one are indistinguishable to a system that only checks whether the message came in through the ticket channel. The moment an attacker can make a planted fact arrive looking first-party, the tag reads verified for exactly the wrong reason, and the gate meant to catch bad guesses opens right up for a fabricated one. That's a harder problem than anything this pattern solves on its own.

Corroboration has its own soft spot. The design assumes a second source is genuinely independent of the first, but two systems can look like separate sources while actually drawing from the same underlying feed. If the telemetry pipeline and the ticketing system both ultimately read from one misconfigured sensor, corroboration between them just means the same wrong number is agreeing with itself twice. I check for that now by tracing each source back to where its data actually originates before I count it as independent, but it's a manual check, and it's easy to skip when a system is under time pressure to ship.

The source taxonomy itself has to match the real reliability differences in whatever domain this runs in, and that's a calibration question with no universal answer. Three tiers worked for the helpdesk case because the reliability gap between a user's impression, a sensor reading, and a technician's confirmation is real and large. A domain with several sources of comparable reliability needs a finer-grained scheme, and a domain where everything entering the fact table has already been vetted before it arrives doesn't need this pattern at all. Building a three-tier gate on top of a system where every input is already verified is just added latency with no safety gain behind it.

The last calibration point is that how conservative the gate should be is a business decision, not an engineering one, and it changes with what a wrong action costs in each direction. A remediation that's cheap and reversible, restarting a background process, clearing a temp folder, can tolerate a looser gate, because acting on a wrong guess costs little. A remediation that's expensive or hard to undo needs a tighter one, even if that means more legitimate cases get routed through an extra diagnostic step first. There's a threshold that matches what a wrong action actually costs in the system it's protecting, and that number has to come from whoever owns that cost, not from whoever happened to write the gating code.
