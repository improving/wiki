---
title: "Is KeyDB 5x Faster than Redis? We Tested!"
type: "Source Summary"
description: "Benchmarks show Redis in multi-threaded mode outperforms KeyDB, contradicting KeyDB's '5x faster' claim."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, platform, improving.com]
sources:
  - "references/improving.com/is-keydb-5x-faster-than-redis/is-keydb-5x-faster-than-redis.md"
---

# Is KeyDB 5x Faster than Redis? We Tested! — Summary

**Original source**: `references/improving.com/is-keydb-5x-faster-than-redis/is-keydb-5x-faster-than-redis.md`

## Summary

InfraCloud benchmarks Redis (multi-threaded, Master-Replica with Sentinel) against KeyDB (multi-master) using Memtier and finds Redis faster on both throughput and replication. KeyDB's marketing claim of being "5x faster than Redis" did not hold in their tests, even after adding an HAProxy load balancer. The post concludes Redis in multi-threaded mode is the better choice, with KeyDB winning only on a few commands.

## Key Claims

- Hardware: three servers with 112 cores, 1 TB RAM, 50 Gbps network, and 1 TB disk each.
- Redis multi-threaded processed 6,000,000 requests in 549s vs KeyDB's 1603s.
- At 1,000,000 requests (1024KB), Redis took 46s vs KeyDB's 119s.
- Uploading about 547 million records took Redis 14 minutes vs KeyDB's 18–19 minutes.
- Adding a load balancer improved KeyDB roughly 50% but it still trailed Redis (29s vs 25s at 512KB).
- Redis multi-threaded was roughly 2x single-threaded; KeyDB won only on some commands.

## Relevance

Tests whether a vendor performance claim survives measurement, bearing on [benchmark validity](/concepts/benchmark-validity.md) and in-memory data store selection. Key subjects are [KeyDB](/entities/keydb.md) and [Redis](/entities/redis.md).

## Quality

Hands-on benchmark by InfraCloud (published on Improving's blog); detailed but environment-specific and vendor-neutral on results.

## Entities Mentioned

- [KeyDB](/entities/keydb.md) — the multithreaded Redis fork under test
- [Redis](/entities/redis.md) — the comparison baseline

## Concepts Covered

- [benchmark validity](/concepts/benchmark-validity.md) — whether a vendor claim predicts real performance
