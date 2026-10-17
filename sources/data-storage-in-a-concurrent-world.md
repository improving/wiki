---
title: "Data Storage in a Concurrent World"
type: "Source Summary"
description: "Uses a seat-booking race to explain why concurrent systems must partition data by causal relationship to get well-ordered events."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, software, improving.com]
sources:
  - "references/improving.com/data-storage-in-a-concurrent-world/data-storage-in-a-concurrent-world.md"
---

# Data Storage in a Concurrent World — Summary

**Original source**: `references/improving.com/data-storage-in-a-concurrent-world/data-storage-in-a-concurrent-world.md`

## Summary

Starting from a relativity analogy — two observers can disagree about which of two unrelated lightning flashes came first — the post argues that concurrent systems face the same problem. Two users can load the same seating chart and pick the same seat, but because their actions are not causally related, the fix is to partition data by its causal property: only seats within the same flight segment truly conflict.

## Key Claims

- Disagreement about event order arises whenever events are not causally related; a traveler moving the other way could disagree about which lightning struck first.
- In software, it takes far less than relativistic speed: loading data into a browser and acting ~20 seconds later is enough for another actor to disagree about order.
- Two people selecting seat 15C only conflict within the same flight segment; the seat selection is causally related to the segment, and the segment is the common cause.
- The resolution is data partitioning: define a partition (here by flight segment) so events are well-ordered, only one processor handles a partition at a time, and data is co-located to allow locking.
- The per-seat algorithm: look up the co-located record, lock it, assign if unassigned, then unlock and move on.
- Actions causally tied to the segment — seat selection, first-class upgrades, standby — need that partition; unrelated actions such as payment, car rental, and travel insurance do not.
- Data moves between stores and gets re-partitioned by different properties; global order may be undecidable, but order within the right partition is not.

## Relevance

Informs [event-driven architecture](/concepts/event-driven-architecture.md) and [data integration](/concepts/data-integration.md) by showing how causal partitioning makes concurrent state deterministic.

## Quality

Practitioner essay by Michael Perry; a vivid, well-argued analogy with a concrete partitioning rule, but conceptual rather than a detailed implementation guide.

## Entities Mentioned

- [Guadalajara](/entities/guadalajara.md) — destination of the flight that opens the essay

## Concepts Covered

- [event-driven architecture](/concepts/event-driven-architecture.md) — ordering and decoupling of events
- [data integration](/concepts/data-integration.md) — moving and co-locating data across stores
