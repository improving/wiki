---
type: Reference
title: "Load the Schema, Don&#x27;t Paste It"
resource: "https://www.devlinliles.com/load-the-schema-dont-paste-it/"
author: "Devlin Liles"
published: '2026-10-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# Load the Schema, Don't Paste It

## The problem

A procurement automation agent I worked on extracts purchase-order documents into structured JSON against a forty-field schema, vendor info, line items, shipping terms, payment terms, all of it maintained by a data platform team as the canonical source of truth. When the prompt was first written, whoever wrote it pasted the schema's field definitions directly into the prompt text, which felt harmless at the time. The schema was right there, it was easy to copy, and the prompt worked.

The canonical schema kept evolving the way schemas owned by a separate team always do. Three fields got added. Two got renamed. None of that happened because anyone told the prompt's author, because there was no reason for the data platform team to know a prompt somewhere had quietly cloned their schema into its own text. The inline copy in the prompt kept reflecting the old version while the real, current schema moved on without it.

I tested this against twenty-five purchase orders, validating the extracted output against the current canonical schema. At least fifteen of the twenty-five failed validation, split between missing fields the old schema copy never asked for and wrong field names where the canonical schema had renamed something the prompt still referred to by its old name. Nobody noticed until a downstream consumer, a system expecting the current field names, broke on real data. The failure traced back to a second, unsynchronized copy of information that should have had exactly one home. That copy quietly drifted apart from the original until the two versions no longer agreed on what a valid purchase order even looked like.

## The pattern

The fix removes the copy entirely. The prompt no longer contains any schema text at all. Instead, it loads the canonical schema file at the moment the prompt gets assembled, right before the call goes out, and injects the current field list fresh, every single time. There's exactly one place the schema lives now, the canonical file the data platform team actually maintains, and the prompt reads from it instead of quoting it from memory.

The mechanism is the same reason you don't hardcode a configuration value that's supposed to come from a config file. Loading fresh at assembly time means a schema change upstream, a field added, a field renamed, propagates automatically with zero prompt-text edits required on my end. I reran the same twenty-five purchase orders against this version and validation failures dropped to near zero. Then I simulated the harder case: bumping the canonical schema to a hypothetical next version, adding fields the extraction logic had never seen before, and ran the same twenty-five orders again. No new drift failures showed up, because there was nothing left in the prompt that could go stale. The schema the prompt used was, by construction, whatever the schema currently was.

What makes this satisfying is that it eliminates the entire class of failure, fixing the fifteen failures I measured without leaving the next instance of the same drift to patch later. Pasting a schema into a prompt creates a second source of truth nobody assigned anyone to maintain. Referencing it removes the second copy, and a thing that doesn't exist can't drift.

## Design considerations

The obvious tradeoff is a runtime dependency you didn't have before. A hardcoded schema in the prompt text will always be there, for better or worse, even if the file it was copied from moves or gets deleted. A referenced schema means the prompt assembly step now depends on that file being reachable and readable at call time. If the schema file's storage has an outage, or someone renames the file without updating the loader, the prompt that used to fail silently on stale data now fails loudly on a missing dependency. I'd rather have the loud failure, because a missing file gets noticed and fixed fast, while a stale copy gets noticed only when a downstream system breaks on production data weeks later. But it's a real tradeoff with a real cost, and I'd define a fallback behavior for what the extraction agent does if the schema load fails rather than assuming it never will.

There's a token-cost angle too, and it cuts in an unexpected direction. A pasted schema is fixed at however many tokens it takes up, forever, even after it drifts out of date. A loaded schema tracks the canonical file's actual size, which means if the data platform team adds ten more fields over the next year, your per-call token cost grows right along with it without anyone deciding that tradeoff on purpose. That growth is worth planning for: look at the canonical schema's growth trajectory before assuming the pattern is a pure win with no ongoing cost implications.

The calibration question I'd ask before applying this anywhere else is who owns the schema and how often it actually changes. This pattern earns its keep specifically when the schema is maintained by a different team, or a different system, than the one maintaining the prompt, because that's exactly the condition under which the two copies have no reason to stay in sync. If I'm the only person who ever touches both the schema and the prompt, and I change them together as a matter of habit, the drift risk this pattern closes is smaller to begin with, because there's no organizational gap for the two versions to fall into. The moment a second team, a third-party API's schema, or anything outside my direct control owns the canonical definition, that's the exact point where an assumption about the schema's shape stops being something I can verify just by reading my own code, and that's where loading fresh instead of pasting stops being a nice-to-have and starts being the only version of this that actually holds up.
