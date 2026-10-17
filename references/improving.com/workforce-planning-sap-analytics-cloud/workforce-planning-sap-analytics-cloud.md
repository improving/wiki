---
type: Reference
title: "Workforce Planning – SAP Analytics Cloud"
resource: "https://www.improving.com/thoughts/workforce-planning-sap-analytics-cloud/"
author: "Shelby Sansone Stephens"
published: '2022-05-03'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

With **SAP HXM Workforce Planning**, SAP offers a complete pre-configured guided solution to fill the gap of operational workforce planning (with a horizon going from 1 year to 2 years in the future). This solution enables such functionality as calculating cost and FTE planning, as well as creating new positions and administration of absences, transfers, terminations, etc.

## A Cohesive View of the Data

Workforce Planning integrates the Finance and the expense side to share information from HR to Finance. Mainly based on SAP SuccessFactors, it is also integrated with S4 Finance for integration of historical average personnel costs and with SAP Fieldglass for external workforce planning. SAP offers the ability to customize based on other third-party solutions if needed.

The solution employs two different approaches that can be used in sequence, in combination, or switch between both:

1. Top-down approach / Aggregated Planning: allows you to plan on an aggregated level and then break down the numbers.
2. Bottom-up approach / Detailed Planning: allows you to plan on more granular level (i.e., Employee level)

## The Process

Let’s imagine you want to see the average salary on a higher level and at the same time plan absences, terminations, transfers by employee as well as created new positions. You can drive individual personal costs from Success factor and then adjust costs at the employee level.

### Step 1: Configuration and preparation

- Import data
  – Master and transactional data from a source system like SAP SuccessFactors Employee Central.

- Maintain planning parameters
  – Administrators can maintain planning parameters, can copy from existing planning categories, use predictive analysis, or integrate with other planning processes (e.g., Cost center planning or P/L planning)
- Initialize/Unlock plan version
  – Plan version to be created and initialized (also pre-populated with FTE and costs).

### Step 2: Aggregated planning or detailed planning, based on use cases.

After the cost calculation, it is possible to adjust the cost (set up for example a general increase of 5% of a specific job unit) after the calculation cost.

At each step of the process, a landing page allows the user to have an overview of the total cost and the Head Count, adjust the cost and drill down.

### Step 3: Transfer Financial Plan

- Derive G-L accounts: Pay components from HR planning are mapped during the process preparation to G/L accounts in workforce planning model.
- Copy to financial plan: Personnel costs need to be copied from workforce plan to cost center plan and integration process happens on company code, cost center and G/L account level.

## Reporting That Meets Your Needs

And finally, SAP HMX Worforce Planning comes with four reports that are fully customizable based on your specificity to directly compare Actuals vs Plan results:

- Progress Overview (Actuals vs Plan)
- Gender Analysis (Actuals vs Plan)
- External Workforce (Actuals vs Plan)
- Budget Comparison (Plan vs Budget)

This solution is pre-configured but customizable to meet your organization’s specific needs. It allows you to create your own reports, customize cost calculation logic, add additional plan cost types for cost calculation, use custom data model, dimensions, etc.

Interested in how SAP HMX Workforce Planning can help provide deeper insights and drive more informed planning decisions in your organization? Contact us to get our team of experts working on the best solution for you.
