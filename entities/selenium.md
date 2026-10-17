---
title: "Selenium"
type: "Entity"
description: "Long-standing browser automation framework with the widest browser and language support and the largest ecosystem."
created: '2026-10-17'
updated: '2026-10-17'
tags: [testing, automation, web]
sources:
  - "/sources/deciding-among-the-titans-of-test-automation.md"
  - "/sources/is-qa-engineer-really-worth-the-investment.md"
  - "/sources/multi-layered-testing-overview.md"
---

# Selenium

Selenium is the oldest of the three browser test-automation tools compared in this corpus and the one with the broadest reach. It anchors the GUI layer of a layered automated testing strategy, acting as the browser automation family behind WebDriver.

## Strengths and Drawbacks

- Offers the widest browser support (Chrome, Firefox, Safari, Edge), bindings for Java, Python, C#, and JavaScript, and a mature ecosystem (Grid, WebDriver, IDE).
- Drawbacks: complex setup, flakiness, slow execution, no built-in runner or assertions, limited mobile support, and a steep learning curve.
- Has no native way to interact with the APIs the browser executes without a custom framework.
- Represents the system/GUI test layer, which should be used sparingly because GUI tests are slower and more brittle than unit and integration tests.
- Cited with Cypress as automation that lets QA teams stop doing repetitive manual checks and focus on edge cases.

## Related

- [Cypress](/entities/cypress.md) — the developer-friendly JavaScript alternative
- [Playwright](/entities/playwright.md) — the modern cross-browser competitor
- [test automation](/concepts/test-automation.md) — the practice it serves
- [test pyramid](/concepts/test-pyramid.md) — where its GUI tests belong
