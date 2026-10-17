---
title: "Cypress.io Tips to Make Your Life Easier"
type: "Source Summary"
description: "Practical Cypress tips: prefer data-cy attributes and use partial-match selectors plus .contains() to target elements with unstable GUIDs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, testing, improving.com]
sources:
  - "references/improving.com/cypress-io-tips-to-make-your-life-easier/cypress-io-tips-to-make-your-life-easier.md"
---

# Cypress.io Tips to Make Your Life Easier — Summary

**Original source**: `references/improving.com/cypress-io-tips-to-make-your-life-easier/cypress-io-tips-to-make-your-life-easier.md`

## Summary

A practical guide to writing reliable Cypress.io end-to-end tests. It recommends adding dedicated `data-cy` attributes to markup, then shows how partial-match selectors and chained `.contains()` calls handle elements whose attributes contain randomly generated GUIDs.

## Key Claims

- Cypress constrains you in good ways toward readable, well-organized tests; adding `data-cy` attributes is more reliable than selecting on classes.
- Exact GUID-based selectors work but are unreadable and break often because the GUID changes when lists update.
- Cypress supports prefix (`^=`), suffix (`$=`), and contains (`*=`) attribute matching, e.g. `cy.get('[data-cy^=item-]')`.
- Chain `.contains()` with a partial selector to target one item: `cy.get('[data-cy^=item-]').contains('Red Delicious Apples')`.
- `cy.contains()` selects by text content, complementing `cy.get()` which selects by attribute.
- `.closest()` narrows from a text match up to the enclosing element, such as a table row, for a more specific assertion.

## Relevance

Informs [test automation](/concepts/test-automation.md) and [automated testing](/concepts/automated-testing.md) through the [Cypress](/entities/cypress.md) framework.

## Quality

Hands-on how-to by Christopher Owens; concrete and code-specific, based on seven months of real use rather than benchmarks.

## Entities Mentioned

- [Cypress](/entities/cypress.md) — the testing framework covered

## Concepts Covered

- [test automation](/concepts/test-automation.md) — main topic
- [automated testing](/concepts/automated-testing.md) — end-to-end test design
