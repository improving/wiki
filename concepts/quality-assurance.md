---
title: "quality assurance"
type: "Concept"
description: "Engineering confidence in a product's fitness, spanning process, data, and layered testing rather than only test execution."
created: '2026-10-17'
updated: '2026-10-17'
tags: [quality, testing, process]
sources:
  - "/sources/process-focused-quality-assurance.md"
  - "/sources/the-evolution-of-qa-from-software-to-data-engineering.md"
  - "/sources/is-qa-engineer-really-worth-the-investment.md"
  - "/sources/multi-layered-testing-overview.md"
  - "/sources/software-testing-manual-and-automation.md"
---

# quality assurance

The work of engineering confidence that a product is fit for use — broader than running tests, and increasingly broader than testing software at all. The corpus reframes QA from a gate at the end of delivery into a process role that shapes requirements up front, verifies data correctness, and improves how the team works after a defect escapes.

## Key Claims

- Testing is only one expression of QA; the highest value often starts before development, when QA reviews requirements, surfaces ambiguities, and challenges assumptions.
- Many bugs originate in conversations, unclear requirements, misunderstood business rules, or architecture decisions — not in code — so the more useful question after a defect is why the process allowed it.
- QA has always been about data correctness: event-driven architectures and Kafka expanded it to validating message schemas, event ordering, lag, retries, and downstream persistence.
- All software instructions reduce to CRUD, so nearly every functional bug is a data bug, and classical API testing is itself an ETL process of query, serialize, and deliver.
- QA is framed as risk mitigation and user trust rather than a cost center; the real cost is lost customers, hotfix delays, and damaged reputation.
- A layered automated suite — unit, integration, and system/GUI — should raise quality and cut production defects, with bugs reaching production diagnosed, wrapped in a test, and released so they never recur.
- A combined manual-plus-automated strategy beats replacing one with the other; each covers the other's blind spots.

## Related

- [manual testing](/concepts/manual-testing.md) — the human-driven part of QA
- [automated testing](/concepts/automated-testing.md) — encoded checks in the pipeline
- [defect management](/concepts/defect-management.md) — root-cause triage beyond the symptom
- [data quality](/concepts/data-quality.md) — the data-correctness core of modern QA
- [Cypress](/entities/cypress.md) — a tool cited for automating repetitive QA checks
