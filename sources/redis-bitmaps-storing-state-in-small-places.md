---
title: "Redis Bitmaps: Storing State in Small Places"
type: "Source Summary"
description: "Two Redis bitmap use cases: tracking multi-step task completion and counting distinct users, using SETBIT, BITPOS, and BITCOUNT."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, engineering, improving.com]
sources:
  - "references/improving.com/redis-bitmaps-storing-state-in-small-places/redis-bitmaps-storing-state-in-small-places.md"
---

# Redis Bitmaps: Storing State in Small Places — Summary

**Original source**: `references/improving.com/redis-bitmaps-storing-state-in-small-places/redis-bitmaps-storing-state-in-small-places.md`

## Summary

A Redis bitmap treats each bit of a string as state, letting an application represent a lot of state in very little space with constant-time bit access. The post walks through two use cases — determining "done" in an asynchronous multi-step task, and counting distinct users — using SETBIT, BITPOS, and BITCOUNT.

## Key Claims

- Redis stores bitmap data in strings and exposes commands that set and get any bit in constant time.
- Use case one: an async task with a fixed number of parallel steps tracks completion by flipping the bit at each step's offset.
- Flipping the bit at the offset equal to the step count first marks the end; the task is done when all earlier bits are also set.
- The `isDone` check combines BITPOS (index of the first zero bit) and BITCOUNT (number of set bits): done when BITPOS is absent or equals BITCOUNT.
- Worked example with four steps: `00001000` → `00101000` → `10111000` → `11111000` (done).
- Use case two: counting distinct users by setting the bit at each userId offset and reading BITCOUNT for the distinct count.
- Bitmaps don't fit every problem but shine when space is scarce and state volume is large.

## Relevance

Informs [real-time data streaming](/concepts/real-time-data-streaming.md), [event-driven architecture](/concepts/event-driven-architecture.md), and [Redis](/entities/redis.md) data modeling.

## Quality

Focused practitioner how-to by Aaron Burk, with a companion Java/Jedis project; assumes familiarity with Redis commands.

## Entities Mentioned

- [Redis](/entities/redis.md) — the in-memory data store providing bitmaps

## Concepts Covered

- [real-time data streaming](/concepts/real-time-data-streaming.md) — tracking state across async processing
- [event-driven architecture](/concepts/event-driven-architecture.md) — coordinating parallel steps and consumers
- [observability](/concepts/observability.md) — cheap metrics such as distinct-activity counts
