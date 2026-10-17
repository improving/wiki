---
title: "Leveraging SAP Analytics Cloud through Custom Widgets"
type: "Source Summary"
description: "How to build and register custom widgets in SAP Analytics Cloud with JS, CSS, and JSON files."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, analytics, improving.com]
sources:
  - "references/improving.com/leveraging-sap-analytics-cloud-through-custom-widgets/leveraging-sap-analytics-cloud-through-custom-widgets.md"
---

# Leveraging SAP Analytics Cloud through Custom Widgets — Summary

**Original source**: `references/improving.com/leveraging-sap-analytics-cloud-through-custom-widgets/leveraging-sap-analytics-cloud-through-custom-widgets.md`

## Summary

SAP Analytics Cloud (SAC) lets users embed custom widgets — built from JavaScript logic and CSS styling, declared by a JSON file — into standard stories to add functionality, UI elements, or visualizations that the built-in widgets cannot provide. The post walks through locating sample code and uploading a widget's JSON file from the Stories menu.

## Key Claims

- Custom widgets extend SAC stories with functionality, UI, or visualizations standard widgets lack.
- Because SAC runs in a browser, widgets are authored with HTML, CSS, and JavaScript.
- A widget requires a JS file for logic, a CSS file for appearance, and a JSON file that declares the function plus its parameters, variables, or triggers.
- SAP publishes sample widget code on GitHub (`SAP-samples/analytics-cloud-custom-widget`).
- Registration happens in the SAC tenant via Stories → Custom Widget → "+", uploading the JSON file.
- Once uploaded, the widget is called in the story and its JS functions can be bound to events with the needed parameters.

## Relevance

Informs [business intelligence](/concepts/business-intelligence.md) and [data visualization](/concepts/data-visualization.md) practice on SAP Analytics Cloud.

## Quality

Short practitioner how-to by Sarisha Castillo; concrete steps but specific to SAC tooling and light on implementation detail.

## Entities Mentioned

- [SAP Analytics Cloud](/entities/sap-analytics-cloud.md) — the BI and planning tool being extended
- [SAP](/entities/sap.md) — vendor of the platform
- [GitHub](/entities/github.md) — hosts SAP's sample widget code

## Concepts Covered

- [business intelligence](/concepts/business-intelligence.md) — custom reporting in SAC
- [data visualization](/concepts/data-visualization.md) — custom visualizations in stories
