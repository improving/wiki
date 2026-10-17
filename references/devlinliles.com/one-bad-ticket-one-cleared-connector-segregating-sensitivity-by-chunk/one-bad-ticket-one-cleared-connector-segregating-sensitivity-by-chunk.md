---
type: Reference
title: "One Bad Ticket, One Cleared Connector - Segregating Sensitivity by Chunk"
resource: "https://www.devlinliles.com/one-bad-ticket-one-cleared-connector-segregating-sensitivity-by-chunk/"
author: "Devlin Liles"
published: '2026-10-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built a customer-support assistant for a fictional broadband provider, one I called HelpDesk Copilot, retrieving from three different sources: a CRM export, a public product and policy handbook, and a set of support-ticket transcripts. Each source gets its own connector, and the first version I built made exactly one permissioning decision per connector: CRM marked internal-only, handbook marked cleared for retrieval, tickets marked cleared for retrieval.

I seeded 40 fake support tickets, and a handful of them contained something an agent had pasted directly into the ticket notes months earlier: a fake SSN, a fake card-fragment pattern, written in an obviously synthetic format but structurally identical to what a real one would look like. Because the tickets connector as a whole was marked cleared, every single one of those 40 tickets got indexed and made retrievable, the sensitive handful included. Nothing in the ingestion process looked at any individual ticket's content. It looked at which connector the ticket came from, saw "cleared," and indexed it.

I ran a fixed set of 20 support queries likely to surface these tickets and measured the percentage of retrieved or cited chunks containing an embedded PII pattern, from a connector that was marked cleared at the source level. It came back above zero. One sensitive record buried inside an otherwise-cleared source leaked straight into retrieval and got quoted verbatim in a generated answer the moment a query happened to surface that particular ticket. The connector-level flag never had a way to catch what one single document, sitting inside an otherwise fine source, actually contained.

## The pattern

The fix inserts exactly one step, and it moves the unit of decision from the connector down to the individual chunk. Every retrieved chunk gets classified for embedded PII individually at ingestion, independent of which connector it came from, and a per-chunk permission filter runs after retrieval and before generation, checking each candidate chunk's own sensitivity tag rather than trusting whatever flag got assigned to its source connector. A flagged chunk gets withheld at retrieval time, even when the connector it came from is otherwise fully cleared for use.

Running the same 20-query set against this version dropped the PII-in-citation rate to 0% across all three connectors, including the tickets connector that had been the source of the leak. I also checked that the other 39 non-sensitive tickets from the same connector still retrieved and answered correctly, because the fix isn't supposed to withhold an entire connector just because one document inside it needed withholding. It held. The other tickets answer exactly as they did before. Only the specific chunks carrying an embedded PII pattern get gated, regardless of which source they came from.

This lands on the same consensus I found running through current RAG-security guidance more broadly: sensitivity should resolve per-record or per-chunk, not per-connector. Elastic Labs and Protecto.ai both published 2026 material making this same case. Here, the point is specifically about a source that's mostly fine hiding a single sensitive exception, a different failure shape than a source that's entirely off-limits from the start. A connector-level flag can correctly mark a wholly sensitive source as off-limits and still fail completely the moment a mostly-clean source contains even one document it shouldn't.

## Design considerations

The limitation here sits entirely in the classifier doing the per-chunk work, and it's a real one rather than a formality to mention in passing. The chunk classifier in this build is a regex-based pattern matcher, which is genuinely fine for catching an obviously fake SSN or card-fragment pattern in a synthetic dataset built to be exploitable. Production detector accuracy doesn't hold steady across domains the way that test suggests it might. One 2026 clinical benchmark found F1 dropping from roughly 0.81 on general text to 0.41 on clinical text, for the exact same detector, tested against the exact same underlying detection task.

A chunk-level gate is only as good as its classifier's recall on the specific kind of sensitive content it's asked to catch, and general-purpose detectors measurably lose that recall the moment the domain shifts away from whatever they were originally tuned on. That means the mechanism I built here, moving the decision to the chunk level, solves the granularity half of the problem completely. It says nothing about the detection half. A perfectly chunk-level-gated system running a detector that's blind to clinical-style phrasing will still leak clinical-style PHI, just at a much finer, more confident-looking granularity than before.

The practical implication is that this pattern needs pairing with a classifier tuned to the actual domain of the content flowing through it, not a generic one assumed to transfer. I'd treat "which detector, tuned on what" as a decision that gets revisited every time a new connector gets added, rather than a setting chosen once and left alone. A support-ticket connector and a clinical-notes connector don't share a detector's blind spots, even if they share the exact same chunk-level gating mechanism sitting in front of them. The gate is the easy part once you've decided to build it. Keeping the detector honest about what it can actually see is the part that needs ongoing attention.
