---
title: "Context-Based Testing"
type: "Source Summary"
description: "Argues that brittle, unmaintainable test fixtures drive teams to abandon automated testing, and prescribes organizing specs by context with shared setup."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, testing, improving.com]
sources:
  - "references/improving.com/context-based-testing/context-based-testing.md"
---

# Context-Based Testing — Summary

**Original source**: `references/improving.com/context-based-testing/context-based-testing.md`

## Summary

Through the fictional developer Don Testa'lot Moore, the post shows how a single bloated test fixture — nearly 1,000 lines for one class — makes testing so painful that a fix requiring 50 lines of test code for one line of implementation gets shut down by a manager. The mentor's remedy is to treat tests as specs, split them by method and then by scenario context, and extract shared arrange-act-assert code into reusable base classes.

## Key Claims

- A BankAccount test fixture can reach ~1,000 lines because each method's branches and exceptions get their own tests.
- The fix for a defect once needed 50 new lines of test code for a single-line implementation change, killing the practice at that company.
- First step: rename tests to "specs" and split the fixture into one file per method (`Depositing`, `Withdrawing`, `TransferringFunds`).
- Extract identical and near-identical arrange/act/assert code into parameterized helper methods, then pull shared helpers into a base class or module.
- Group remaining tests by scenario context (e.g. "insufficient funds", "flagged fraud victim") so a reported defect is easy to locate.
- Benefits: small readable spec files, easier reuse, faster impact analysis on failures, and tests that stop rotting.
- The approach is framework- and layer-agnostic — unit, integration, or end-to-end, front or back end, MS-Test/NUnit/JUnit/xUnit/Jest/Cypress.

## Relevance

Directly informs [test automation](/concepts/test-automation.md) and [test pyramid](/concepts/test-pyramid.md), showing how test organization, not just coverage, determines whether a suite survives.

## Quality

Practitioner how-to by Claudio Lassala; concrete and actionable, illustrated with a worked example but anecdotal rather than measured.

## Entities Mentioned

- [Claudio Lassala](/entities/claudio-lassala.md) — author, Improving
- [NUnit](/entities/nunit.md) — one of the named test frameworks

## Concepts Covered

- [test automation](/concepts/test-automation.md) — making suites maintainable enough to keep
- [test pyramid](/concepts/test-pyramid.md) — spanning unit, integration, and end-to-end tests
