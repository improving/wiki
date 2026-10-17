---
title: "Leveraging Analytics Features in SAP Analytics Cloud Stories"
type: "Source Summary"
description: "Shows how SAP Analytics Cloud's integrated Analytics Designer enables cascading dropdowns, background data actions, and planning UIs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, improving.com]
sources:
  - "references/improving.com/leveraging-analytics-features-in-sap-analytics-cloud-stories/leveraging-analytics-features-in-sap-analytics-cloud-stories.md"
---

# Leveraging Analytics Features in SAP Analytics Cloud Stories — Summary

**Original source**: `references/improving.com/leveraging-analytics-features-in-sap-analytics-cloud-stories/leveraging-analytics-features-in-sap-analytics-cloud-stories.md`

## Summary

Analytics Designer is now fully integrated into SAP Analytics Cloud's story design experience, letting users add widgets, buttons, inputs, and containers to build interactive applications. The post walks through the redesigned left side panel and three scenarios that together make a flexible, interactive planning interface.

## Key Claims

- The new Left Side Panel is split into Assets, Outline, and Filters; Assets holds draggable widgets, controls, text inputs, containers, and planning actions.
- Outline lists every canvas item and is where scripts are created and edited, with an improved scripting look and feel across pages.
- Story filters were grouped into the Filters panel section, though they can still be pinned to the top as before.
- Scenario 1, cascading dropdowns, filters one dropdown's options based on another's selection — for example showing only products from a selected country and company.
- Scenario 2 runs data actions in the background by feeding parameters through variables already calculated in the story, using `setParameterValue`.
- Scenario 3 visualizes or updates dimension members selected from a table using `getSelections`/`getResults`, and can trigger planning calculations on button click.
- Together these enable an interactive planning UI that can be extended with linked-analysis charts and comment widgets.

## Relevance

Demonstrates [business intelligence](/concepts/business-intelligence.md) and interactive [data visualization](/concepts/data-visualization.md) on SAP's cloud analytics platform, with planning workflows akin to [data storytelling](/concepts/data-storytelling.md).

## Quality

Product how-to by Sarisha Castillo; specific about functions and panel layout but narrow and tied to a single SAP tool.

## Entities Mentioned

- [SAP Analytics Cloud](/entities/sap-analytics-cloud.md) — the BI and planning tool whose story features are explained

## Concepts Covered

- [business intelligence](/concepts/business-intelligence.md) — decision-ready reporting and analysis
- [data visualization](/concepts/data-visualization.md) — interactive charts and interfaces
- [data storytelling](/concepts/data-storytelling.md) — presenting insight through narrative and visuals
