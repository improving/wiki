---
title: "Cypress"
type: "Entity"
description: "JavaScript end-to-end testing framework valued for automatic waiting, time-travel debugging, and a built-in runner."
created: '2026-10-17'
updated: '2026-10-17'
tags: [testing, automation, javascript]
sources:
  - "/sources/deciding-among-the-titans-of-test-automation.md"
  - "/sources/cypress-io-tips-to-make-your-life-easier.md"
  - "/sources/is-qa-engineer-really-worth-the-investment.md"
  - "/sources/context-based-testing.md"
---

# Cypress

Cypress is a JavaScript end-to-end testing framework that appears in this corpus as the developer-friendly option among browser automation tools. It is cited both as a tool choice in QA strategy and as the subject of hands-on selector guidance.

## Capabilities and Limits

- Provides real-time reloading, automatic waiting, time-travel debugging, a built-in runner, and fast execution.
- Limited primarily to Chrome, JavaScript-only, without mobile app testing, and with a smaller ecosystem than Selenium.
- Recommended practice: add dedicated `data-cy` attributes rather than selecting on classes, and use prefix (`^=`), suffix (`$=`), and contains (`*=`) attribute matching plus chained `.contains()` for elements with unstable GUIDs.
- Named alongside Selenium as the automation tooling that makes repetitive QA checks worth automating.
- Listed among the frameworks a framework-agnostic testing approach can target, spanning unit, integration, and end-to-end layers.

## Related

- [Selenium](/entities/selenium.md) — the broader, older browser automation family
- [Playwright](/entities/playwright.md) — the modern cross-browser alternative
- [test automation](/concepts/test-automation.md) — the practice it implements
- [quality assurance](/concepts/quality-assurance.md) — where it fits in the QA strategy
