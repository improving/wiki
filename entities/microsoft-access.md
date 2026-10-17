---
title: "Microsoft Access"
type: "Entity"
description: "Legacy desktop database appearing here both as a long-lived RAD success and as a fragmentation and governance problem."
created: '2026-10-17'
updated: '2026-10-17'
tags: [legacy, databases, data-governance]
sources:
  - "/sources/stop-treating-legacy-systems-as-the-enemy.md"
  - "/sources/the-policy-binder-didnt-change-anyones-behavior.md"
---

# Microsoft Access

Microsoft Access is a legacy desktop database that appears in this corpus with two faces: as a rapid-application-development tool that quietly ran businesses for decades, and as a source of data fragmentation that modernization and governance programs must clean up.

## Legacy Success

- Access applications built with "rapid application development" were dismissed as cheating by mainframe-era engineers, yet some ran businesses for decades.
- The essay's argument is that a system surviving fifteen years is evidence of success; the buried edge cases and business logic are worth carrying forward rather than demolishing.

## Modernization and Governance Target

- In the California Department of Health Care Services case, behavioral health data was fragmented across Excel spreadsheets, Microsoft Access databases, and a legacy Teradata warehouse with a decade of undocumented assumptions.
- The fix was architectural — rebuilding on [Databricks](/entities/databricks.md) with governance engineered into the pipeline so metadata traveled with the data, rather than a hand-maintained catalog beside it.

## Related

- [legacy modernization](/concepts/legacy-modernization.md) — the practice of evolving such systems incrementally
- [data governance](/concepts/data-governance.md) — the problem Access fragmentation creates
- [FoxPro](/entities/foxpro.md) — the sibling RAD tool cited alongside it
- [data quality](/concepts/data-quality.md) — the property fragmentation undermines
