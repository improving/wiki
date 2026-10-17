---
type: Reference
title: "The Attribution Budget - Why Telemetry Never Answers Why"
resource: "https://www.devlinliles.com/the-attribution-budget-why-telemetry-never-answers-why/"
author: "Devlin Liles"
published: '2026-10-14'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I watched this play out on an agentic data-pipeline-repair system I built, an agent chain that diagnoses and patches seeded ETL failures, schema drift, null-handling bugs, timeout misconfigurations. I shipped genuinely complete, well-structured telemetry, one span per node, and treated that as sufficient for post-incident work. A patch applied to fix one job caused a downstream data-quality incident in another job two days later, and the engineer I assigned had to manually read raw structured logs and reconstruct causality by hand.

Across a ten-incident set with documented ground-truth causes, attribution coverage, the share of incidents where a definitive cause ever gets produced within a capped review budget, landed under fifty percent, even though the telemetry backing it was genuinely complete. The gap traced back to a single assumption baked into the project plan: that solid telemetry would produce attribution automatically, as a side effect of good logging.

## The problem

Teams that build good telemetry tend to assume the hard part is done. Complete, well-structured spans feel like observability, and in a real sense they are: they answer exactly what a trace is supposed to answer, which node ran, with what inputs, in what order, at what cost. Computing a causal judgment about which node's output was responsible for a downstream failure is a separate task. It requires a different mechanism, one that has to be built on purpose, with its own inputs, its own scoring logic, and its own output: a verdict.

I've seen this mistake specifically because I made it myself on this project. The telemetry was genuinely good. My engineer still had to spend real time manually reading spans, correlating timestamps across two separate jobs, and reconstructing by hand what should have been a lookup. Coverage under fifty percent within a capped review budget means more than half the incidents in my own ten-incident set never got a definitive answer at all in the time allotted. The data was there in every case. What was missing was a mechanism to turn that data into a verdict.

## The pattern

I stopped treating attribution as something the telemetry system would eventually produce as a side effect, and built it as its own component instead: its own data model, its own eval set, its own line item in the project plan. This service ingests the same telemetry spans as input, plus the known outcome signal, and produces a ranked causal judgment as output. It reuses trace propagation and per-node scoring as building blocks I'd already built for other purposes.

On the identical ten-incident set, this got attribution coverage to ninety percent or better, with mean time-to-attribution dropping to near-instant. I also log `attribution_service_build_cost`, a documented estimate of the engineering effort the component took, on purpose, so the central claim, that attribution is its own budget line, has a real number attached to it that anyone can check on a dashboard. Nobody has to take my word for it in a planning meeting.

The hard evidence behind treating this as a serious, separately budgeted build comes from outside anything I built myself. The Who&When benchmark, built specifically to measure automated failure attribution in multi-agent systems, found that even frontier reasoning models and the best purpose-built attribution methods correctly name the responsible agent only about 53.5 percent of the time, and the responsible step barely 14.2 percent of the time. Even a team that budgets attribution correctly, as its own serious engineering effort with its own eval set, is still working against a genuinely hard, actively benchmarked research problem. Funding the line item correctly is a starting condition. The underlying problem stays hard regardless.

## Design considerations

Budgeting the build correctly buys exactly one thing: you've stopped pretending telemetry would clear the accuracy bar for free. Whether the resulting mechanism actually clears that bar is a separate, harder question, one budgeting alone can't answer. That distinction matters when I'm setting expectations with anyone paying for this work. A separately built attribution service that reaches ninety percent coverage on my own ten-incident set is still a system built against a problem where the best published methods top out around half for agent-level attribution and well under a fifth for step-level attribution on harder benchmarks. My own numbers reflect a bounded, synthetic eval set with documented ground truth. I don't assume they'd hold at the same level against the messier failure modes a much larger production system would eventually surface.

The organizational cost is the part teams underestimate most, and it isn't really an engineering cost at all. Getting a project plan to include attribution as its own line item, with its own data model and its own eval set, means someone has to argue for that budget against a backdrop where the telemetry dashboard already looks like it's doing the job, right up until the first incident where two days pass between a patch and its downstream consequence and nobody can say why without hours of manual log archaeology. Making that argument before the incident happens is harder than making it after, and I've found it's almost always made after, which means the first real incident becomes the expensive lesson that should have been a line item from the start.

There's also a reuse question worth being deliberate about. Building attribution as a separate service can still draw on everything already built around it. The trace propagation and per-node scoring mechanisms I'd already put in place elsewhere became inputs this service consumes. Treating attribution as its own build means giving it explicit ownership and an explicit budget line, while still consuming the mechanisms already built elsewhere in the system. A dedicated attribution component that reinvents trace correlation or per-node scoring from scratch is paying twice for the same capability and calling the second payment rigor.
