---
title: "SAP Analytics Cloud"
type: "Entity"
description: "SAP's cloud business intelligence and planning tool, positioned as the successor to BusinessObjects and BPC."
created: '2026-10-17'
updated: '2026-10-17'
tags: [business-intelligence, sap, planning]
sources:
  - "/sources/leveraging-analytics-features-in-sap-analytics-cloud-stories.md"
  - "/sources/workforce-planning-sap-analytics-cloud.md"
  - "/sources/leveraging-sap-analytics-cloud-through-custom-widgets.md"
  - "/sources/transforming-financial-planning-from-sap-bpc-to-sap-analytics-cloud-sac.md"
  - "/sources/leveraging-sap-analytics-cloud-with-sap-businessobjects.md"
  - "/sources/new-feature-in-sap-analytics-cloud.md"
---

# SAP Analytics Cloud

SAP's all-in-one SaaS product for [business-intelligence](/concepts/business-intelligence.md), budget planning, and predictive analytics. In this corpus it is the reporting and planning layer that sits on top of [SAP](/entities/sap.md)'s data stack, and the designated migration target for customers on legacy on-premises tools.

## Migration Target

- SAP BusinessObjects is the on-premises BI suite; legacy Explorer and Xcelsius dashboards are being retired and should move to SAC.
- BOBJ capabilities such as Analysis for Office, Lumira Designer, and scheduling/bursting exist in SAC; keep Universe, Web Intelligence, and Crystal Reports only if critical.
- SAP extended BOBJ maintenance to 2027 to protect investments while customers plan cloud transitions.
- Many companies still lack a dedicated planning system and rely on Excel; SAP BPC brings rigid workflows, macro errors, and an end-of-support horizon. Improving's xi.Planning packages extend SAC across opex, capex, workforce, revenue, and cash flow.

## Building on SAC

- Analytics Designer is integrated into story design, letting users add widgets, buttons, inputs, and containers for interactive planning applications.
- Cascading dropdowns, background data actions via `setParameterValue`, and selection-driven planning all run inside Stories.
- Custom widgets, authored in JavaScript and CSS and declared by JSON, extend stories with visualizations the built-in widgets lack; SAP publishes sample code on GitHub.
- The Q4/2021 release added Best Performance Tips, non-blocking hints in Edit mode that flag layouts likely to slow a story.

## Planning and Reporting

- SAP HXM Workforce Planning links SuccessFactors HR data to finance for cost and FTE planning, with Actuals-vs-Plan reports.
- SAC serves as the visualization and forecasting layer across the SAP data stack, including Group Reporting output.

## Related

- [SAP](/entities/sap.md) — the vendor and data ecosystem
- [business-intelligence](/concepts/business-intelligence.md) — decision-ready reporting and analysis
- [data-visualization](/concepts/data-visualization.md) — interactive charts and story interfaces
- [data-platform-modernization](/concepts/data-platform-modernization.md) — leaving legacy BPC and BOBJ
