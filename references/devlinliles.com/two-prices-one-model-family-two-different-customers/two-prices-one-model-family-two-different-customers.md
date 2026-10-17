---
type: Reference
title: "Two Prices, One Model Family, Two Different Customers"
resource: "https://www.devlinliles.com/two-prices-one-model-family-two-different-customers/"
author: "Devlin Liles"
published: '2026-10-01'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Meta shipped two models five days apart this month, and the five days is the part I can't stop thinking about.

On August 5, Meta released Muse Spark 1.2, an updated checkpoint in its Muse Spark line. API-only. Priced at $1.25 per million input tokens and $4.25 per million output tokens on the standard tier. There's a second tier too: $0.10 and $0.20 per million tokens, twelve to twenty times cheaper, and it exists for one reason. It catches the price-sensitive volume that would never touch the standard tier at all, without Meta having to cut the price everyone else already agreed to pay.

That gap is the first tell. A twelve to twenty times spread doesn't get built into a single closed product unless the company already knows its buyers don't look alike. Some of them want the fastest, best-supported version and will pay for it without blinking. Others are running the model at a scale where every fraction of a cent compounds into a number that matters to a finance team, and they'll take a slower or more limited tier to get it. Meta priced for both inside the same API, on the same day, before anyone outside Menlo Park had heard of Glimmer.

Five days later, on August 10, Glimmer shipped under an Apache 2.0 license. Open weights. No API key, no per-token bill, no tier at all. If Spark 1.2 was Meta answering "how do we price for buyers who want us to run this," Glimmer is Meta answering a completely different question: what do we hand to the people who never wanted us to run it in the first place.

These are two different customers standing at two different shelves. The API buyer is paying for a relationship: uptime, support, a roadmap, someone to call. The self-hosting buyer wants none of it. They want to fine-tune on proprietary data without sending it through someone else's endpoint, or run inference on hardware they already own, or build a product where variable per-token cost at scale is the thing they're trying to engineer away from. No price on the closed tier, not $1.25 and not $0.10, was ever going to move that buyer. They were never in the market Spark 1.2 was priced for.

Which is what makes the five-day gap read as a decision. Releasing both on the same day would have made Muse look like one confused product trying to be everything. Spacing the closed version and the open one a full business quarter apart would have lost the shared branding moment, the sense that these two ship from the same family. Five days is close enough that the two products get talked about together and far enough apart that each one gets its own moment of coverage.

The commercial logic underneath is straightforward once you see it. The closed API keeps the revenue-paying enterprise customer inside Meta's billing relationship, tiered so it doesn't leave margin on the table with either the buyer who'll pay full price or the one who'll only show up at a discount. The open release goes after something Meta can't invoice for directly: developer mindshare, the goodwill of the open-weight community, and the compounding advantage of being the model that gets embedded into other people's tools before a competitor's does. Neither group is bidding against the other for the same unit of revenue, so there's no cannibalization to manage and no reason to hold one release back for the other.

One family name is doing the work of two go-to-market strategies at once, and that's the part I keep coming back to. A segmentation strategy wearing a version number, five days and one press cycle apart.
