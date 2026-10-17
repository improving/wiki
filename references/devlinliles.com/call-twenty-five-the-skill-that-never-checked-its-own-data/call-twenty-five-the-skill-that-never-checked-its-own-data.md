---
type: Reference
title: "Call Twenty-Five - The Skill That Never Checked Its Own Data"
resource: "https://www.devlinliles.com/call-twenty-five-the-skill-that-never-checked-its-own-data/"
author: "Devlin Liles"
published: '2026-10-05'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

A financial-reporting agent runs a skill called generate-quarterly-variance-summary. It pulls from a data mart, does the arithmetic policy requires, and hands back a formatted number. The skill itself has never had a bug in it. That's what makes the failure I want to walk through here so uncomfortable: nothing about the skill was ever wrong.

## The problem

I built a scenario around this skill running fifty sequential report-generation calls in a row. A nightly ETL job that feeds the underlying data mart fails silently partway through that run, at call twenty-five. From that point forward, the mart is frozen. Nothing about the skill's own logic changes, and nothing about its output changes either. It keeps executing exactly as before and keeps handing back the same confidently formatted variance numbers, computed now from data that stopped updating twenty-five calls earlier.

Every one of those twenty-five post-failure calls looked, from the outside, identical to a healthy one. Same formatting. Same tone of confidence. Same absence of any flag, warning, or footnote suggesting the ground underneath had shifted. I measured a hundred percent silent staleness rate across those calls, meaning every single one handed back a number computed on frozen data with zero indication anything was wrong. A person reading any one of those twenty-five reports in isolation had no way to know it was stale, because the skill that produced it didn't know either.

I keep coming back to that detail. The skill was never wrong about how to calculate a variance. It inherited its trustworthiness entirely from a data source it never checked, and that inheritance stayed invisible the entire time, because nothing in the skill's own logic was built to notice when the thing it depended on stopped being current.

## The pattern

The fix doesn't touch the skill's calculation logic at all. It adds one step before the skill is allowed to act on anything: the skill's registry entry names the specific data source it depends on, and before returning output, it checks that source's own governance record. Two fields do the work: when the source was last verified, and whether its lineage certification is still current.

When the source has missed its freshness service-level agreement or lost its lineage certification, the skill refuses to hand back a confident number. Instead it returns a flagged response, something like "ungrounded, source stale," and points back to the last known-good governed output instead of silently computing on frozen data. Replayed against the same call-twenty-five failure, every one of the twenty-five affected calls gets correctly flagged at the exact moment the source went bad, and the last trustworthy result stays available on request rather than disappearing behind a wall of refusal.

What I like about this mechanism is how little it asks of the skill itself. The skill doesn't need to get smarter about detecting anomalies in its own output, which is a much harder problem and one prone to false confidence of its own. It just has to stop extending trust automatically to a source that already stopped earning it. The check is closer to a handshake than a judgment call: does the thing I depend on say it's still good, and if it doesn't, I say so too instead of pretending otherwise.

## Design considerations

The obvious calibration question is where the freshness SLA gets set and who owns the answer. Too strict, and a source with a routine five-minute sync delay starts tripping the flag constantly, training everyone downstream to ignore the warning the same way an oversensitive smoke detector trains a household to ignore the alarm. Too loose, and the check technically exists but never fires before the staleness has already caused real damage. That number isn't something a skill's author should set unilaterally. It belongs to whoever owns the data source's own governance record, because they're the one positioned to know how often it legitimately lags and by how much.

The last-known-good fallback is doing more work than it looks like at first glance, and it's the detail I'd defend hardest if someone wanted to simplify this pattern down. A grounding check that only refuses, with nothing to hand back in place of the refused number, creates its own failure mode: a financial-reporting workflow that goes dark the moment a single upstream job hiccups, with no visibility into whether the last real answer is even still reachable. Serving the last known-good result alongside the stale flag means a downstream user gets a real answer, clearly labeled as not current, instead of a wall. That distinction between refusing and degrading gracefully is where most of the design judgment in this pattern actually lives.

The limitation I'd flag loudest is what this check doesn't cover. It watches whether the declared external data source has gone stale. It says nothing about whether the skill's own procedural content, its logic, its description of a system that may have quietly changed underneath it, has drifted out of date on its own terms. A skill that correctly flags every stale-source call can still be running against a business rule that changed last quarter and was never updated in the skill itself, and this check has no way to catch that, because it was never built to watch the skill's own content, only what the skill depends on externally. That's a genuinely separate problem, closer to continuous evaluation of the skill's own procedural accuracy than to anything a governance-record lookup can answer, and I haven't seen a mechanism yet that closes that gap as cleanly as this one closes the data-freshness half of it.
