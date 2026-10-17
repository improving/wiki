---
title: "Business Process Automation Tools: AI Solutions in the Real World"
type: "Source Summary"
description: "Case study: automating 100,000 invoices a year with Microsoft's prebuilt model, validation checks, and human review of exceptions."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, microsoft, improving.com]
sources:
  - "references/improving.com/business-process-automation-tools-ai-solutions-in-the-real-world/business-process-automation-tools-ai-solutions-in-the-real-world.md"
---

# Business Process Automation Tools: AI Solutions in the Real World — Summary

**Original source**: `references/improving.com/business-process-automation-tools-ai-solutions-in-the-real-world/business-process-automation-tools-ai-solutions-in-the-real-world.md`

## Summary

A consulting case study of automating accounts payable for "Company X," which processes roughly 100,000 invoices a year by hand and pays penalties for late payments. Improving chose Microsoft's prebuilt invoice-processing model over a custom one for speed, wired it into SharePoint, and added 13 validation checks plus a human review interface for exceptions, cutting an estimated $75,000 of annual effort.

## Key Claims

- Company X's AP team manually processed ~100,000 invoices a year, missing payment deadlines and at times incurring late-payment penalties.
- Two options were weighed: train a custom Microsoft AI model versus use the existing prebuilt invoice-processing model. The prebuilt model won because varied supplier formats made custom training slow and its maintenance would fall to the client.
- The workflow extracts key fields from invoice PDFs into SharePoint, then calls a local supplier database through a custom connector using the purchase order number as the identifier.
- An invoice auto-validates only when all 13 validation checks pass and the model's confidence score is at least 70%.
- Exceptions surface in a review interface showing extracted data, database data, and the original PDF side by side; a per-field search highlights where a value was extracted.
- Rejected invoices trigger an automated email to the supplier listing reasons and requesting a corrected resubmission.
- The initiative is projected to save 1 FTE ($75,000) per year; the post concedes AI can confidently extract wrong fields but argues validation checks and human fallback cover the risk.

## Relevance

A concrete [business process automation](/concepts/business-process-automation.md) case that pairs [AI augmentation](/concepts/ai-augmentation.md) with [human-in-the-loop](/concepts/human-in-the-loop.md) review.

## Quality

Practitioner case study by Janine Jeanson; specific on workflow and numbers, though the client is anonymized and results are projections.

## Entities Mentioned

- [Microsoft](/entities/microsoft.md) — prebuilt invoice model
- [SharePoint](/entities/sharepoint.md) — where extracted fields land
- [Janine Jeanson](/entities/janine-jeanson.md) — author
- [Improving](/entities/improving.md) — author firm

## Concepts Covered

- [business process automation](/concepts/business-process-automation.md) — automating a repeatable workflow
- [AI augmentation](/concepts/ai-augmentation.md) — AI as a tool beside people
- [human-in-the-loop](/concepts/human-in-the-loop.md) — clerks review exceptions
- [human approval points](/concepts/human-approval-points.md) — the 70% confidence gate
- [data quality](/concepts/data-quality.md) — validation checks against source data
