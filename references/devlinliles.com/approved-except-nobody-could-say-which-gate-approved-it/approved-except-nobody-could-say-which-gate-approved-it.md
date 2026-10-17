---
type: Reference
title: "Approved, Except Nobody Could Say Which Gate Approved It"
resource: "https://www.devlinliles.com/approved-except-nobody-could-say-which-gate-approved-it/"
author: "Devlin Liles"
published: '2026-10-03'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built a loan-application orchestration for a consumer-lending back office, chaining three quality gates before any application reached funding: income verification, credit check, fraud check. Standard sequence, nothing exotic about the design. The dashboard sitting on top of it, though, showed exactly one thing per application: a single green "approved" or red "declined."

That single collapsed status felt fine right up until it wasn't. I ran thirty synthetic loan applications through the orchestration, six of them carrying an injected fraud-check failure that should have blocked funding outright. All six got funded anyway. When I went looking for which gate had actually let a bad loan through, the answer wasn't in the system anywhere. The orchestration never stored or surfaced per-gate results. Only the final rollup existed. I measured a gate attribution loss rate, the share of wrongly approved applications where the responsible gate couldn't be identified from stored data, and it came back at 100 percent on the six bad loans. The orchestration had simply never recorded which gate ran on a given application. There was nothing to look up, because nothing had been written down to look up.

Here's the part that makes this failure mode dangerous, and it goes past mere annoyance. Nothing about the underlying gates was necessarily broken. Income verification might have run correctly. Credit check might have run correctly. Fraud check might have failed on exactly the case it was supposed to catch, and the orchestration still would have shown "approved," because the aggregate logic only asked whether the application cleared the pipeline, never which specific step it cleared or failed on the way through. A single wrongly passing gate is completely invisible inside an overall green result, and nobody can diagnose it or trust it without re-running the entire pipeline by hand and hoping the failure reproduces.

## The pattern

The fix persists and surfaces each gate's individual pass-or-fail result, along with its evidence snippet, the specific check that fired, for every single application. A fraud-check failure now shows up explicitly as "fraud-check: FAILED," regardless of what income verification or credit check did on the same application. The aggregate result still gets computed and displayed, sitting alongside the per-gate detail now visible next to it.

Running the same thirty applications through the trace-emitting version, gate attribution loss goes from 100 percent to zero on the six previously invisible bad loans. Every application's per-gate trace is now inspectable directly. The single checkmark used to tell you the outcome and nothing else; the trace tells you how the system arrived at it.

What this buys is inspectability at the moment a decision is made. The record already exists before anyone notices something went wrong, so there's nothing left to reconstruct after the fact. The distinction matters. A team that has to re-run a whole pipeline by hand to figure out which gate failed on a bad loan is doing forensic work under pressure, usually after the money's already gone out the door. A team with per-gate traces sitting there from the start is reading a record that was already complete the moment the application finished processing.

I want to be precise about the size of the claim here, because it's easy to overstate. This is a lighter-weight pattern than a full causal-attribution system that replays a decision back through every upstream input it touched. Gate-Trace Visibility surfaces per-gate pass-or-fail with evidence at the moment a decision gets made. It stops well short of a replayable, suppression-tested trace back through everything that fed into each gate's own reasoning. Think of it as the audit-shaped pattern sized for a specific, smaller scale: which named gate fired, on what evidence, right now. The deeper, harder claim, tracing a decision back through every input that shaped it, is a separate piece of work this pattern leaves alone.

## Design considerations

The gate's honesty depends entirely on what each individual gate is actually checking, and this pattern has nothing to say about that question. Surfacing "fraud-check: FAILED" is only useful if the fraud-check gate itself is checking something meaningful. A gate that's testing the wrong thing, or testing against a narrow, unrepresentative slice of the real input space, will surface its wrong answer just as clearly as a well-built gate surfaces a right one. Visibility exposes what a gate decided. Whether that gate was asking the right question in the first place is a separate audit this pattern leaves untouched, and conflating the two is how a team ends up trusting a beautifully instrumented gate that was still testing the wrong thing the whole time.

There's a real cost to persisting per-gate results at volume, and I'd rather state it plainly than leave it implied. Three gates times however many applications a lending desk processes in a day adds up fast, and every one of those records needs somewhere to live and some retention policy governing how long it stays queryable. For a back office processing thousands of applications daily, that's a real infrastructure decision, with its own storage and retention cost sitting on top of the aggregate result you were already computing.

The place this pattern earns its keep most clearly is exactly the scenario I built here: a multi-gate sequence where a single failure needs to be attributable to one specific step, fast, without anyone needing to reconstruct what happened after the fact. A single-gate system has no use for this pattern, because there's only ever one thing that could have failed and the aggregate result already tells you which. The value scales with the number of gates in the chain and with how expensive it is to leave a wrongly passing one undiagnosed. A three-gate loan pipeline funding real money justified building this; a one-gate internal sanity check sits well below that bar.
