---
title: "Power Automate"
type: "Entity"
description: "Microsoft's workflow automation service, connecting 500+ apps and automating business processes."
created: '2026-10-17'
updated: '2026-10-17'
tags: [microsoft, low-code, automation]
sources:
  - "/sources/how-to-use-sharepoint-rest-apis-with-power-automate.md"
  - "/sources/power-up-with-power-apps.md"
  - "/sources/shutdown-app.md"
  - "/sources/building-a-line-of-business-application-with-microsoft-365.md"
---

# Power Automate

Power Automate is the workflow service of [Microsoft Power Platform](/entities/power-platform.md), automating actions across 500+ apps via REST or on-premises through a gateway. It is the connective tissue in Improving's low-code solutions, from SharePoint integrations to contract workflows.

## Key Claims

- Power Automate can drive SharePoint Online's REST APIs directly through its HTTP request action, giving professional and citizen developers CRUD access without writing a backend.
- A REST request combines an entry point, a resource, and parameters; the `_api` postfix identifies the SharePoint channel, and `getbytitle('TestList')` retrieves a list by name.
- The "Send an HTTP request to SharePoint" action takes Site Address, Method, URI, and Body.
- In a contract lifecycle management system, Power Automate provided the workflow and notification connective tissue, with a central contract hub and minimal flows in child department sites.
- It also handles automation in the mine "Shutdown App" alongside [Power Apps](/entities/power-apps.md) and dashboards.

## Related

- [Microsoft Power Platform](/entities/power-platform.md) — the suite Power Automate belongs to
- [SharePoint](/entities/sharepoint.md) — the REST API target
- [business process automation](/concepts/business-process-automation.md) — automating repeatable workflows
- [low-code development](/concepts/low-code-development.md) — citizen-developer-friendly tooling
