---
title: "KeyDB"
type: "Entity"
description: "A multithreaded Redis fork, benchmarked against Redis here."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, benchmark, engineering]
sources:
  - "/sources/is-keydb-5x-faster-than-redis.md"
---

# KeyDB

KeyDB is a multithreaded fork of Redis that appears in this corpus as the subject of a head-to-head benchmark. InfraCloud tested KeyDB's marketing claim of being "5x faster than Redis" and found it did not hold, making KeyDB a case study in whether a vendor performance claim survives independent measurement.

## Benchmark Findings

- Test hardware: three servers with 112 cores, 1 TB RAM, 50 Gbps network, and 1 TB disk each, using Memtier.
- Redis in multi-threaded mode processed 6,000,000 requests in 549s versus KeyDB's 1603s.
- At 1,000,000 requests (1024KB), Redis took 46s versus KeyDB's 119s; uploading about 547 million records took Redis 14 minutes versus KeyDB's 18–19 minutes.
- Adding an HAProxy load balancer improved KeyDB roughly 50%, but it still trailed Redis (29s vs 25s at 512KB).
- Redis multi-threaded was roughly 2x single-threaded; KeyDB won only on some commands, so the post recommends Redis multi-threaded for this workload.

## Related

- [benchmark validity](/concepts/benchmark-validity.md) — whether a vendor claim predicts real performance
- [Redis](/entities/redis.md) — the comparison baseline and the recommended choice here
- [Improving](/entities/improving.md) — publisher of the benchmark (by InfraCloud)
