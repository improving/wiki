---
type: Reference
title: "Observability-Driven Development"
resource: "https://www.improving.com/thoughts/observability-driven-development-designing-observable-applications/"
author: "Atulpriya Sharma"
published: '2026-07-02'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

At almost every conversation around observability, I’ve noticed a pattern. Teams have metrics and logs in place but the moment tracing comes up, there's a pause. Either it's on the backlog, or it was set up partially and never completed, or nobody owns it.

Tracing is treated as the optional third pillar of observability, until an incident happens where it's the only metric that would have actually helped.

Lack of tracing isn't really the problem, instead it's a symptom. The deeper issue is that observability is still treated as something you wire up after the application is built. It’s either an ops concern or a post-deployment checklist, but not a design decision.

There is a better way to approach this, and in this blog post, we will explore observability driven development, where observability is securely tied to the application from day 1.

## Observability Paradox: More Tools, Worse Outcomes

The cost of hourly downtime exceeds [$300,000 for 90% of firms](https://itic-corp.com/itic-2024-hourly-cost-of-downtime-report/), and 41% of enterprises say hourly downtime costs $1 million to over $5 million. As a result, observability is being discussed in every room and 70% engineers admitted that observability budgets have increased in the past year in a [research done by Dynatrace in 2025](https://www.dynatrace.com/news/press-release/state-of-observability-2025/). But yet there are downtimes and teams scramble through multiple dashboards to find the root cause. Mean time to resolution (MTTR) during production incidents has trended in the wrong direction for four consecutive years. [In 2021, 47% of teams reported MTTR over an hour and by 2024, that number had climbed to 82%](https://logz.io/observability-pulse-2024/#current-state-of-observability). So, there’s more investment happening, newer tools and AI being added, yet recovery is slower.

The cost of that slowdown is not just technical. High-impact outages carry huge losses, with [median cost of $2 million per hour.](https://newrelic.com/blog/observability/top-trends-in-observability-the-2025-forecast-is-here) Teams with full-stack observability reduces the downtime cost in half. The gap between those two outcomes is not about which tools you bought but it is about how you use them and when you bring them in development.

[41% of leaders](https://newrelic.com/sites/default/files/2025-09/new-relic-2025-observability-forecast-report.pdf) still learn about service interruptions through inefficient means including customer complaints, incident tickets, or manual checks, even as organizations continue investing in observability. Your dashboards are green, but your users are already affected. That is a visibility gap baked into how the system was built.

## When Observability Is an Afterthought

Most teams start by building the service, writing the code, and shipping it to production. Then someone raises a ticket to setup monitoring dashboards and alerts. That’s because monitoring is the last item on the launch checklist and not the first item on the design document.

Even if the team implements visibility from the start, things aren’t helpful until an incident comes to light. For instance, a team building a new payments microservice does the right things at deployment time. Scraping Prometheus metrics, forwarding the logs to the aggregation stack and building dashboards, seems to cover the observability.

However, what a healthy request flow looks like end to end is not defined. Nobody mapped out which integration points needed tracing, and error budget was not set before the service went live.

It’s only when the first real incident hits, the gaps show up immediately:

- Metrics show something is wrong but not where
- Logs require manual correlation across multiple services to build any picture
- Third-party payment gateway sitting at the edge of the system has no instrumentation at all

You’ll have a few engineers to spend hours finding the root cause to fix it. This happens because observability was never part of the initial design and architectural conversations. Observability was treated as something ops handles after the application is built, not something engineers designed for while building it.

## Observability-Driven Development (ODD): Designing to Be Observed

Observability Driven Development (ODD) is a development practice that shifts observability left, treating it as a design concern from day one rather than an afterthought. Teams define their observability requirements the same way they define their functional requirements. To set up observability properly, a teams should note down answers to specific questions before any code is written:

- What does a healthy request flow look like end to end?
- Which integration points carry the most risk and need tracing?
- What failure modes are possible, and how will they surface?
- What does degraded performance look like versus a hard failure?

Test-driven development (TDD) changed how teams used to think about code quality, by making testing a design activity. ODD does the same for operational visibility. You are designing a system that is observable.

## Key Aspects of ODD

Here’s how ODD differs from standard observability practices:

- **Telemetry is a design requirement, not a deployment task:** Logs, metrics, and traces are scoped during design the same way API contracts and data models are.
- **SLOs come before code:** Error budgets and service level objectives are defined at the start, giving the team clear signals to build toward and clear thresholds to alert on.
- **OpenTelemetry as the instrumentation standard:** OpenTelemetry is now the second largest CNCF project after Kubernetes. It has become the default choice for vendor-neutral, portable instrumentation.
- **Observability gaps are treated as bugs:** If a critical path cannot be observed, that is a defect to fix, not a gap to live with.

### Implementing ODD in Practice

A complete overhaul of your existing tooling is not required to implement ODD in your software development lifecycle (SDLC) processes. It only requires shifting a few things within the process.

- **Identify** what needs to be observable during the design phase. Map critical paths, define instrumentation touchpoints, and set SLOs before writing code.
- **Instrument** observability during your development phase as you build. Treat observability gaps the same way you treat failing tests - something to fix before the PR merges, not after the service ships.
- **Validate** that telemetry actually works as a pre-launch item. Confirm traces are flowing, metrics are accurate, and alerts fire under the right conditions before go-live, not after the first incident.

## Benefits of ODD That Show Up in the Business

Implementing ODD doesn’t just improve your reliability metrics and product quality, but it directly affects your customer satisfaction and shows up in your financials.

- **Faster incident resolution:** Teams that design for observability upfront [cut MTTR by 40-50%](https://jetsoftpro.com/blog/what-actually-work-in-software-engineering-in-2025-and-what-didnt/). When traces are in place and instrumentation covers critical paths, engineers can find root causes in minutes. The difference between a 20-minute fix taking 20 minutes versus taking 3 hours is almost always a visibility gap, not a complexity gap.
- **Developers building instead of firefighting:** Cisco research found [developers spend more than 57% of their time pulled into war rooms for performance issues](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2024/m05/developers-spending-more-time-firefighting-issues-than-delivering-innovation.html). ODD changes it as when a system is built to surface its own failures, lesser efforts are spent to diagnose them.
- **Business cost of downtime shrinks:** Full-stack observability halves the median cost of a high-impact outage. Getting there requires designing for observability from the start, not layering tools on top after the fact.
- **Less noise, lower spend:** Nearly [70% of observability data most teams collect is unnecessary](https://jetsoftpro.com/blog/what-actually-work-in-software-engineering-in-2025-and-what-didnt/). Intentional instrumentation at design time means teams collect the signals that matter, not everything available, which directly reduces observability spend and alert fatigue.

## ODD in the Age of AI

AI has transformed software development. Codes are written by AI agents, reviewed by AI agents, and even validated by AI agents. AI also changes the observability problem in a fundamental way.

Traditional applications fail in predictable ways, like a service crashed, a query timed out or an API returned a 500. These were observable with standard tooling. But AI systems fail differently, like a model may return a confident but wrong answer, and a prompt can produce inconsistent outputs under similar conditions. Latency varies in ways that are difficult to attribute to any single component. These are subtle and silent failures and often challenging to catch reactively.

This is why ODD isn't optional for AI-powered applications. Designing for observability from day one means teams define upfront what they need to see - prompt and response logging, model latency tracking, token usage, output quality signals - and build the instrumentation to surface it.

## Conclusion

The correct sequence to implement ODD is:

1. Bring observability into the design conversation
2. Define what the system needs to surface before building it
3. Treat instrumentation gaps the same way you treat bugs.

This sequencing refines the type and speed of outcomes. Less engineering time is lost to correlating logs and finding the root cause, and cost of downtime reduces due to leaner intentional telemetry.

As AI gets embedded deeper into application stacks, observability becomes complicated. The teams with a foundation built on ODD will be better positioned to handle that complexity than those trying to retrofit visibility after the fact.

Have thoughts on how your team approaches observability? Connect with me on [LinkedIn](https://linkedin.com/in/atulpriyasharma). And if you are looking to build that foundation, the [Improving application observability and support team](https://www.improving.com/contact/) is a good place to start.
