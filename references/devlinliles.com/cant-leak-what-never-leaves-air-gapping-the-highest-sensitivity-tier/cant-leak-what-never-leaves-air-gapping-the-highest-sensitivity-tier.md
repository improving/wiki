---
type: Reference
title: "Can&#x27;t Leak What Never Leaves - Air-Gapping the Highest-Sensitivity Tier"
resource: "https://www.devlinliles.com/cant-leak-what-never-leaves-air-gapping-the-highest-sensitivity-tier/"
author: "Devlin Liles"
published: '2026-10-05'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# Can't Leak What Never Leaves - Air-Gapping the Highest-Sensitivity Tier

## The problem

I built a research assistant for a fictional law firm, one I called CaseLens, and gave it two kinds of work associates actually do: general contract-law research pulled from public case law and statutes, and analysis of privileged material tied to an active matter, raw deposition transcripts and client communications, the narrowest and most sensitive slice of anything the firm touches.

The first version I built already had something most naive single-endpoint systems don't bother with: an in-flight scrubber. Both query types went to the same external hosted model, but deposition text passed through a regex-based scrubbing pass before the call left the boundary. I tuned that scrubber to the obvious patterns, standard SSN format, phone numbers. Then I seeded three synthetic deposition transcripts with realistic variations the scrubber had never seen: account numbers written in an unlabeled format, a client referred to only by a nickname defined earlier in the same transcript. I tracked one metric, the number of privileged-tier tokens that crossed the trust boundary to the external endpoint, and it stayed consistently above zero across all three transcripts.

That's a sharper failure than "nobody built a filter." A filter existed. It just wasn't good enough, and it failed the way scrubbers tend to fail: pattern-complete on the formats someone thought to test, blind to the ones nobody wrote a rule for. Every deposition transcript carries its own vocabulary, its own way of referring to people and numbers, and a regex tuned on one transcript's patterns has no reason to catch the next transcript's. A scrubber can be perfectly correct on the day it's tested and still miss the exact case that shows up the following week.

## The pattern

The fix I landed on doesn't try to build a better scrubber. It removes the need for one entirely, for the narrowest, highest-stakes slice of traffic. A tier classifier identifies which queries are sourced from privileged deposition material and routes that specific slice to a model running entirely inside the firm's own network, with no outbound call at all. General case-law research still goes to the external hosted model as before. Nothing needs to be scrubbed on the privileged path, because nothing on that path ever leaves the boundary to be scrubbed.

The metric reads zero by construction for the privileged tier once this is in place, not because the scrubbing improved but because there's no longer a call to scrub. I can't leak what never leaves the building. That's a stronger guarantee than any filter can offer, because a filter's guarantee is only as good as its last test case, and a boundary that's never crossed doesn't have a last test case to fail.

This isn't a hypothetical deployment pattern confined to a compliance slide anymore. Deloitte reports nearly $100 billion invested in sovereign AI compute in 2026 alone, and the sovereign AI infrastructure market itself is estimated at $24.8 billion in 2026, growing toward the high tens of billions by year end. On-premises deployment is the fastest-growing mode by investment value specifically because, as one industry source frames it, any cloud dependency, even a sovereign-certified cloud, gets treated as unacceptable for the most sensitive government and enterprise workloads. I read that as real evidence the highest tier is a funded, real deployment target rather than an idea nobody's actually building.

## Design considerations

The same limitation that sits under a pre-call classifier sits under this pattern too, and I'd rather name it directly than let the structural guarantee's strength paper over it. Everything depends on the tier classifier assigning the query correctly in the first place. A privileged query the classifier fails to recognize as privileged has no scrubber to catch it on the way out, because in this design there's no scrubber running on the general path either. It goes straight to the hosted model like any general query would. The structural guarantee is real and total for correctly tagged traffic. It says nothing about mistagged traffic, and the earlier scrubber-based version already demonstrated how easy mistagging is to produce once a transcript uses a nickname or an unlabeled account format nobody anticipated.

Cost and latency are the other side of the ledger, and they're real enough to plan around rather than dismiss. Running a model entirely inside a network boundary means provisioning and maintaining that infrastructure regardless of how rarely the privileged tier actually gets queried. If privileged queries make up five percent of total traffic, the firm still carries the full weight of an on-prem model available at all times, because the whole point is that the option has to exist before a privileged query ever arrives, not be spun up after the fact.

The calibration question that actually matters is where the tier boundary sits. Draw it too narrow and content that should be air-gapped slips through as "general" traffic, recreating the exact scrubber-blind-spot failure this pattern exists to eliminate. Draw it too wide and you're running expensive on-prem infrastructure for traffic that never needed the guarantee, general research that happened to get swept into the privileged bucket out of caution. I'd rather set that boundary from a real inventory of what data actually carries privilege in a given practice, deposition transcripts, client communications tied to an active matter, rather than from a vague sense that "sensitive stuff" should probably get the strongest treatment available. Vague boundaries produce either the leak or the overspend. A named, specific inventory produces neither.
