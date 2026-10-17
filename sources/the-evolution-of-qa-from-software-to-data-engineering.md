---
title: "The Evolution of QA: From Software to Data Engineering"
type: "Source Summary"
description: "Argues QA has always been about data correctness, and that its scope now spans event streams, cloud services, and ML pipelines."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, testing, improving.com]
sources:
  - "references/improving.com/the-evolution-of-qa-from-software-to-data-engineering/the-evolution-of-qa-from-software-to-data-engineering.md"
---

# The Evolution of QA: From Software to Data Engineering — Summary

**Original source**: `references/improving.com/the-evolution-of-qa-from-software-to-data-engineering/the-evolution-of-qa-from-software-to-data-engineering.md`

## Summary

Federico Silva argues that quality assurance has always been about data correctness, and that its scope has expanded from front-end and API testing into data engineering. Event-driven architectures and platforms like Kafka now require testers to verify message schemas, event ordering, lag, retries, and downstream persistence. He reframes functional testing as data testing — nearly every functional bug is a data bug — and positions data quality engineering as the foundation of data-driven systems.

## Key Claims

- In modern AI, data quality differentiates models more than architecture or dataset size: garbage in, garbage out.
- Event-driven architectures and Kafka expanded QA to validating producer message schemas, consumer event ordering, lag and retries, and usable downstream records.
- In the AWS ecosystem, QA covers S3 ingestion and lifecycle rules, SQS message delivery, Lambda outputs and transformations, DynamoDB persistence, and CloudWatch metrics and logs.
- Hidden transformations can break even simple extract-and-load pipelines: encryption with mismanaged keys, differing compression algorithms, and encoding mismatches.
- All software instructions reduce to CRUD operations, so a form that doesn't persist is a Create defect, a wrong search a Read defect, and so on — almost every functional bug is a data bug.
- Classical API testing is itself an ETL process: query, serialize, and deliver.
- Non-functional testing (performance, security) sits on top of data correctness, protecting and scaling it rather than altering data.

## Relevance

Reframes [quality assurance](/concepts/quality-assurance.md) around [data quality](/concepts/data-quality.md), [ETL](/concepts/etl.md), and [event-driven architecture](/concepts/event-driven-architecture.md), with implications for [test automation](/concepts/test-automation.md).

## Quality

Opinionated practitioner essay by Federico Silva; a useful reframing, but the CRUD argument is asserted rather than evidenced.

## Entities Mentioned

- [Apache Kafka](/entities/apache-kafka.md) — platform that widened QA's scope
- [AWS](/entities/aws.md) — cloud services QA must validate

## Concepts Covered

- [quality assurance](/concepts/quality-assurance.md) — confidence in fitness
- [data quality](/concepts/data-quality.md) — accuracy and consistency
- [ETL](/concepts/etl.md) — pipelines that move and reshape data
- [event-driven architecture](/concepts/event-driven-architecture.md) — producer/consumer testing
- [test automation](/concepts/test-automation.md) — encoded checks
- [data integration](/concepts/data-integration.md) — connecting data across sources
