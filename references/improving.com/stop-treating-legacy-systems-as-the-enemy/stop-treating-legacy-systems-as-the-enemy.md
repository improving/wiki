---
type: Reference
title: "Stop Treating Legacy Systems as the Enemy"
resource: "https://www.improving.com/thoughts/stop-treating-legacy-systems-as-the-enemy/"
author: "Claudio Lassala"
published: '2026-06-17'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Many legacy software are built using "rapid application development" (RAD) tools like FoxPro or Microsoft Access. At that time, the senior engineers around, the ones who had spent decades with punch cards and mainframe batch jobs, looked at what FoxPro users were doing and called it cheating. FoxPro was too easy and high-level. It abstracted away the real work. A tool like that couldn’t produce anything serious.

They were wrong as those FoxPro applications were able to run businesses and created the bedrock of successful enterprises. Some of them are still running today, decades later. The people who dismissed the tools could never dismiss the results.

I’ve watched this pattern repeat through every generation of technology I’ve worked in. Visual Basic was too simple for C++ developers. .NET was too abstracted for the Visual Basic crowd. And now, AI-assisted development gets the same skepticism from the previous generation. Every era’s tools get treated as cheating by the people who built the last era.

The pattern isn’t just about tools, though. It shows up in how we talk about the systems those tools produced. We call them “legacy” and mean it as an insult. That’s a mistake.

## **What “Legacy” Actually Means**

A system that has been running for fifteen years didn’t survive by accident. It survived because it solved a real problem for real people, and it kept solving that problem through market shifts, leadership changes, and at least two or three technology cycles that were supposed to replace it. That’s not a failure. That’s evidence of success.

The problem isn’t that legacy systems exist. The problem is that we approach them with contempt instead of curiosity. When the default attitude is “Rip and Replace,” we lose something. Buried in that old code is business logic that nobody documented, edge cases that took years to discover, and decisions that were made for reasons the current team may not even know about.

Treating a legacy system like an enemy means treating your organization’s history like a liability. I’d rather treat it like a foundation.

## **Refueling the Plane While It’s Still in the Air**

The urge to do a total rewrite is one of the most dangerous instincts in enterprise software. I have seen too many systems fail because they were 'Ground-and-Rewritten' instead of evolved. A total rewrite introduces massive risk and ignores the nuanced business rules embedded in the existing code.

I compare modernization to refueling a plane in mid-flight. The business cannot stop generating revenue because the technology underneath needs an upgrade. You can’t land the plane to refuel the engines. You have to do it while it’s still moving, and that demands a different discipline than a greenfield build.

The discipline is evolutionary maintenance**, **systematic, incremental, and protected by automated tests.

A recent example: migrating from Fluent Assertions to Shouldly across a large .NET codebase including over 3,000 tests. Deprecated APIs scattered through years of accumulated work. The process started with Context7, feeding the AI current library documentation that post-dates its training data. Without that step, the model works from stale knowledge and confidently introduces errors. With it, the AI reasons about actual API changes rather than guessing at them.

What surfaced next was something a purely manual process would likely have missed: Lamar and Marten shared a dependency. Updating one without the other would have broken the build in ways that wouldn't show up immediately. The AI found the link during the initial dependency scan.

Rather than forcing a full rewrite of existing test code, the AI generated custom extension methods to bridge the gap, preserving the developer experience on top while changing the underlying library beneath it. What would have been a multi-week manual effort compressed into two days with AI-assisted workflows. (I wrote about the full process in [Embedding AI Into Daily Development](https://www.improving.com/thoughts/embedding-ai-into-daily-development/).)

The safety net is the non-negotiable part. Without automated tests, evolutionary maintenance is just a polite name for changing things and hoping nothing breaks. With them, you can refuel the plane with confidence, one engine at a time, the passengers never noticing.

The teams that get this right don’t frame modernization as a one-time event. They treat it as ongoing technical hygiene, closer to changing the oil regularly than waiting for the engine to seize. There are key steps you need to follow to [make application modernization successful](https://www.improving.com/thoughts/key-steps-to-making-application-modernization-successful/).

## **What You Find When You Look With Respect**

Something happens when you approach a legacy codebase as archaeology rather than demolition. *You find things!* I’ve lost count of how many modernization projects have surfaced buried business logic that was still correct, still needed, and completely undocumented. For examples:

- An edge case handler that prevents a specific error nobody remembers anymore,
- A validation rule that catches a regulatory requirement the compliance team forgot was encoded in software.
- A workflow that routes exceptions to the right person because someone five years ago spent three weeks figuring out who that person should be.

These are what I call ‘little gems’** **in the overlooked. When you modernize with contempt, you demolish them along with everything else. When you modernize with respect, you discover them, and you carry them forward into the new system deliberately, rather than rediscovering the need for them six months after launch through a production incident. This is the part of modernization that rarely makes the project plan. The plan says “migrate module X.” It doesn’t say “discover why module X has forty-seven edge cases that nobody can explain.” But that discovery is where real value lives. The teams who do it well are the ones who treat the legacy code as an artifact that encodes organizational knowledge, not just syntax waiting to be replaced.

## **A Different Starting Question**

Most modernization conversations start with “How do we get rid of this old system?”

That’s already the wrong question because it assumes the system is the problem. Majority of the time, the system isn’t the problem, the system is the accumulated answer to problems the organization has faced over the years. The real question is: what has this system been holding together, and how do we keep that intact while we evolve everything around it?

The organizations that modernize well don’t treat their legacy systems as enemies to defeat. They treat them as foundations to build on. The code changes. The infrastructure changes. But the business logic, the hard-won edge cases, and the organizational knowledge encoded in software carries forward.

If your team is facing a [legacy modernization](https://www.improving.com/expertise/applications/legacy-modernization/) challenge, the first step isn’t picking a new tech stack. It’s understanding what you already have, and what it’s been doing for you all along.

For any comments or suggestions to discuss this article, send me a message on [LinkedIn](https://www.linkedin.com/in/claudiolassala/).
