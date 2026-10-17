---
title: "Designing Distributed Systems"
type: "Source Summary"
description: "Explains synchronous vs asynchronous communication in distributed systems using phone-call and postal-service analogies and real trade-offs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, improving.com]
sources:
  - "references/improving.com/designing-distributed-systems/designing-distributed-systems.md"
---

# Designing Distributed Systems — Summary

**Original source**: `references/improving.com/designing-distributed-systems/designing-distributed-systems.md`

## Summary

Distributed systems rest on one basic choice: synchronous communication, modeled on the phone call, or asynchronous communication, modeled on the postal service. The post argues that asynchronous messaging is the more powerful default for computers, and that the most robust real systems blend both.

## Key Claims

- Synchronous communication ("phone calls") underlies the web and suits customized, real-time experiences.
- Asynchronous messaging ("postal service") scales because messages queue instead of requiring an immediate answer.
- Large-sale commerce like Ticketmaster or Hasbro card drops uses async requests to temporarily lock inventory so seats are never sold twice.
- Streaming services (Netflix, Spotify, Prime Video) deliver the last mile synchronously per consumer while running asynchronously internally.
- A technology conference recorded attendees downloading 11 TB from Netflix in three days.
- Sync costs compute and network; async adds per-message overhead, so designs should match the business goal.

## Relevance

Grounds [event-driven architecture](/concepts/event-driven-architecture.md) and [reactive systems](/concepts/reactive-systems.md), and explains the delivery model behind [real-time data streaming](/concepts/real-time-data-streaming.md).

## Quality

Accessible explainer by Tim Rayburn; strong analogies for non-technical readers, with little implementation depth.

## Entities Mentioned

- [Netflix](/entities/netflix.md) — streaming example of synchronous last-mile delivery
- [Spotify](/entities/spotify.md) — streaming service cited alongside Netflix

## Concepts Covered

- [event-driven architecture](/concepts/event-driven-architecture.md) — systems communicating through events
- [reactive systems](/concepts/reactive-systems.md) — message-driven, elastic, resilient systems
- [real-time data streaming](/concepts/real-time-data-streaming.md) — processing events as they occur
