---
type: Reference
title: "The Benchmark That Never Gets a Vote"
resource: "https://www.devlinliles.com/the-benchmark-that-never-gets-a-vote/"
author: "Devlin Liles"
published: '2026-10-15'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

A team I watched needed to pick a model for a support-ticket triage agent. The job was narrow on paper: read an incoming ticket, sort it into one of eight categories, billing, bug, feature request, account access, integration, performance, security, other. The team did what most teams do when a decision has to land by Friday. They pulled the model's published score on a generic public text-classification benchmark, two hundred general items with no connection to support tickets, and picked the model that topped the chart. Certification took an afternoon.

Nobody checked the set that actually mattered, so I built it myself. A hundred and fifty tickets sampled from the company's own historical queue, heavy on billing and integration edge cases because that's where their real volume sits, light on security because that's genuinely rare for them, messier and more category-ambiguous than anything in the public set because real customers type fast while irritated rather than composing a clean benchmark item. I ran the winning model against both sets side by side. Public-benchmark accuracy landed above 85 percent. Accuracy on the company's own ticket distribution came in under 65 percent.

Nobody had lied anywhere in that process. The public score was real, the model genuinely earned it, and none of it told the team what they needed to know. The question the certification checklist answered, how did this model do on a fixed public test, was a different question than the one production was about to ask, whether this model can sort this company's actual tickets reliably. The only way to see the gap between those two questions is to run both sets and put the numbers side by side, and a certification process built around a single vendor score never does that by construction. The failure here is quiet: skipping the second test is all it takes.

## The pattern

The fix has nothing to do with picking a better model. It comes down to changing which measurement gets to decide anything. I keep the same public benchmark and the same real-ticket set from the story above, and I change exactly one rule: the real-ticket set, expanded and sampled through a documented procedure that matches the company's actual category frequencies rather than whatever tickets happened to be sitting around and easy to collect, becomes the only set a release decision is allowed to touch. A release gate reads that internal set and nothing else. It returns pass or fail against a configured accuracy threshold, and there's no appeal to a better-looking number from somewhere else.

The public benchmark keeps running. It still gets logged and still shows up on the same dashboard next to the internal number, carrying a badge that reads reference only, sitting beside a second badge on the internal score that reads gating metric. The model itself is identical between the failed certification and the corrected one. The only difference is which measurement gets to speak for the decision.

The mechanism underneath that is a documented, stratified sampling procedure, built on purpose rather than assembled from a pile of convenient examples somebody grabbed from a shared drive. Stratified means the internal set is built to match the organization's real task-category frequencies on purpose: if integration tickets make up thirty percent of the actual queue, they make up something close to thirty percent of the eval set, regardless of whatever fraction happened to survive an afternoon of manual collection. That documentation matters more than it sounds like it should, because a year from now somebody is going to ask why the set looks the way it does, and "I grabbed what was around" fails an audit or a handoff to a new team member.

What this buys an organization is narrow and specific. It stops a convenient measurement from standing in for the one that actually matters. The model's own quality is unaffected, and the internal set still has to be sound on its own merits. What this guarantees is only that the release decision answers the right question, the one built to matter, rather than the one that happens to flatter.

## Design considerations

An internal set inherits a risk the public benchmark also carries: staleness, now running on a clock the organization controls, which is easy to mistake for solved. What actually makes this pattern hold up over time is something you have to build in on purpose rather than assume comes free: a documented process for refreshing the internal set as the real ticket distribution shifts. A support product's category mix a year from now won't match the mix it was stratified against today. New features generate new ticket types. Old pain points get fixed and stop generating volume. An internal set nobody revisits becomes exactly the frozen, no-longer-representative measurement this pattern exists to replace, carrying an internal label where a vendor's logo used to be. I treat the refresh cadence as a required part of the pattern itself, one that gets deprioritized the first time the roadmap gets tight unless somebody owns it explicitly.

There's a harder limit sitting underneath all of this: the pattern only works when the organization has enough real historical data to stratify against in the first place. A brand-new product with three months of ticket history doesn't have a real distribution to sample yet, and building a stratified set against a thin, unrepresentative slice of early data just launders the same convenience-sampling problem through a more rigorous-sounding process. In that situation I'd rather say plainly that the eval set is provisional and will need rebuilding once real volume exists, than pretend a hundred tickets from month one describe what month twelve will look like.

The other thing I watch for is treating stratification itself as a solved, mechanical step. Deciding which dimensions to stratify on, category, severity, customer tier, language, is a judgment call somebody makes, and a bad choice of dimensions produces a set that looks rigorous while missing the axis that actually predicts failure. I've seen a team stratify carefully by category and never notice that the real driver of model error was ticket length, because nobody thought to check. The documented procedure has to include the reasoning for why those dimensions were chosen. Sampling math alone leaves the rigor cosmetic.

Judgment about whether a model is good enough in some absolute sense still belongs to a person; this pattern doesn't touch that call. What it changes is what that judgment gets tested against: the organization's own work, measured by a number that was actually built to decide.
