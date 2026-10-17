---
title: "How to use SharePoint REST APIs with Power Automate"
type: "Source Summary"
description: "Walkthrough of calling SharePoint Online REST APIs from Power Automate's HTTP action to create list items, covering URL and body structure."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, low-code, microsoft, improving.com]
sources:
  - "references/improving.com/how-to-use-sharepoint-rest-apis-with-power-automate/how-to-use-sharepoint-rest-apis-with-power-automate.md"
---

# How to use SharePoint REST APIs with Power Automate — Summary

**Original source**: `references/improving.com/how-to-use-sharepoint-rest-apis-with-power-automate/how-to-use-sharepoint-rest-apis-with-power-automate.md`

## Summary

Power Automate can drive SharePoint Online's REST APIs directly through its HTTP request action, giving professional and citizen developers CRUD access to SharePoint data without writing a backend. The post walks through the request anatomy and a concrete example that adds an item to a list.

## Key Claims

- Power Automate is the Power Platform workflow service, automating actions across 500+ apps via REST or on-premises via a gateway.
- SharePoint Online exposes REST APIs for Create, Read, Update, and Delete operations on its data.
- A REST request combines an entry point, a resource, and parameters; the `_api` postfix identifies the SharePoint channel.
- Example resource: `getbytitle('TestList')` retrieves a list by name.
- The "Send an HTTP request to SharePoint" action takes Site Address, Method (POST), Uri, and Body.
- The demo posts an item to a list named HTTP with the Title value "Test".

## Relevance

Informs [business process automation](/concepts/business-process-automation.md) and [low-code development](/concepts/low-code-development.md) over [SharePoint](/entities/sharepoint.md).

## Quality

Short practitioner how-to by Stephan Alexander; clear steps but assumes Power Platform familiarity and is screenshot-driven.

## Entities Mentioned

- [Power Automate](/entities/power-automate.md) — the workflow service doing the calls
- [SharePoint](/entities/sharepoint.md) — the target REST API
- [Power Platform](/entities/power-platform.md) — the containing suite
- [Microsoft](/entities/microsoft.md) — vendor

## Concepts Covered

- [business process automation](/concepts/business-process-automation.md) — automating repeatable workflows
- [low-code development](/concepts/low-code-development.md) — citizen-developer-friendly tooling
