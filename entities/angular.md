---
title: "Angular"
type: "Entity"
description: "Google's TypeScript single-page application framework, recommended here for enterprise separation of concerns and testability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [web, frontend, developer-tools]
sources:
  - "/sources/6-reasons-to-use-angular-instead-of-asp-net-mvc-razor.md"
  - "/sources/how-do-i-choose-new-technologies-for-an-organization.md"
---

# Angular

Angular is a TypeScript single-page application framework that this corpus recommends over server-rendered ASP.NET MVC with Razor for enterprise front ends. The case rests on clean separation of client presentation from server-side logic, which improves both testing and the design-to-implementation workflow.

## Why It Appears

- Razor mixes client and server code in one file; Angular decouples client-side processing completely from the server.
- Separation of concerns: the Angular client handles rendering, validation, formatting, and navigation, while the server handles authentication, business logic, and data.
- Because the layers are separated, automated tests for each need not account for the other, and the Angular CLI ships pre-packaged UI testing tools.
- Eases the UX/UI design-to-implementation handoff, since layout is governed by HTML, CSS, and JavaScript rather than server-side code, and offers a larger set of presentation libraries than ASP.NET MVC.
- Follows an MVC (more precisely MVVM) style and lets teams split expertise between server-side and front-end developers.
- Cited as an approachable adoption for a C# team given TypeScript's similarity to C#, VS Code, and Microsoft backing.

## Related

- [Microsoft](/entities/microsoft.md) — maker of ASP.NET MVC and Razor, and backer of the Angular/TypeScript path
- [C#](/entities/c-sharp.md) — the team language used in the adoption example
- [test automation](/concepts/test-automation.md) — easier client and server tests from separation
- [user experience](/concepts/user-experience.md) — smoother design-to-implementation transition
