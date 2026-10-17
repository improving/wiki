---
type: Reference
title: "Own the Interface: Why Enterprise AI Needs a Governed Gateway"
resource: "https://www.improving.com/thoughts/own-the-interface-why-enterprise-ai-needs-a-governed-gateway/"
author: "Michael Slater"
published: '2026-09-08'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

I ask every client the same two questions before we talk architecture: Have you calculated what happens to your bill if your model provider raises prices 30% tomorrow? And have you forecasted what a 1,000% increase in token usage per employee over the next year does to that same bill?

Most of the time, teams haven't run either number. That's not a knock on them. Six months ago, a lot of us were paying $20 a month for predictable, flat-rate AI access, and it was easy to treat that stability as permanent. But now, enterprise API pricing runs per token. The rate changes with every model release, and the providers setting those rates have no obligation to make your budget easy to plan around.

That's the starting problem. Most enterprises call a frontier model API directly, with no abstraction layer in between. It works fine until the vendor changes pricing, changes usage terms, or deprecates the model you built around. At that point, the direct line your platform depends on becomes the most expensive line item on your roadmap.

## The Exposure You're Carrying

Calling a vendor's API directly creates risk in a few specific places, and most teams are only tracking one or two of them.

**Pricing** is the obvious one. You're on a per-token rate that changes with every release, and you have no counterparty when it moves.

**Availability** is next. When a provider's API slows down or goes down, you inherit that outage. Cloud infrastructure teams plan for this kind of failure everywhere else in the stack. AI inference usually isn't planned for the same way, because there's only one path to it.

**Data residency and data privacy** are related but distinct. Residency is about where the inference physically runs, which matters the moment you're operating under GDPR or a similar regulatory regime and need to guarantee which data center handled a given request. Privacy is about who can see the data and whether it trains someone else's model. Terms of service on this have been inconsistent enough across providers that "trust the vendor" isn't a real answer for critical systems.

**Vendor viability** matters more than people want to admit right now. Nobody knows for certain which labs are still standing in three years. Planning your architecture around a provider that might not exist on that timeline is a real bet, whether or not anyone frames it that way internally.

**Model risk** rounds it out. Providers deprecate models fast. Anthropic has already moved from Sonnet 4 to Sonnet 5, and no one can tell you exactly when the older versions disappear. If you have applications or agents tuned to how a specific model behaves, you're riding out that model on borrowed time, whether or not your team has budget allocated to migrate it.

None of these are hypothetical. All six are already showing up on client roadmaps.

![image 3 - Own the Interface: Why Enterprise AI Needs a Governed Gateway ](images/AdobeStock_2006667732.jpeg)

## Our Solution: From Model as a Service to Platform as a Service

Here's the reframe that fixes this: we've spent the last decade or two building cloud infrastructure as platform as a service, and AI inference can work the same way. Instead of calling a provider's API directly, you can route through a hyperscaler like AWS Bedrock (the same logic applies to Azure AI Foundry or Google Vertex AI), which hosts Anthropic, OpenAI, and open-weight models behind one governed layer that you control.

The principle underneath this is simple. Whoever owns the interface to AI inference owns the leverage. Own that layer, and you control a lot more of your own destiny than you do renting a direct line to one vendor.

## The Path, in Three Steps

You don't need to build all of this at once. I walk clients through it as three stages, and each one is a real, usable stopping point on its own.

#### **Step one: go direct to a hyperscaler.**

If your agents or harnesses currently point at api.openai.com or api.anthropic.com, pointing them at an AWS Bedrock endpoint instead is close to a one-line change. The API compatibility holds, so you send the same payload with a different authentication token and get the same inference back. There's no hardware to buy and no infrastructure migration. You immediately get model flexibility across providers and a consolidated, predictable billing relationship with the cloud you're probably already on. The limitation at this stage is that you're locked into that one hyperscaler's endpoint, without the routing intelligence that comes next.

#### **Step two: put a governed gateway in front of it.**

This is where the architecture starts doing real work. A gateway sits between your applications, agents, and harnesses on one side, and your hyperscaler (or any inference backend) on the other. It receives the same API-compatible requests, logs everything about them (which prompt, which model, which system, which user), then forwards the request and streams the response back exactly as before. Because it sees every call before it leaves your environment, it can inspect prompts for policy violations, strip data that shouldn't leave the building, and route requests to a cheaper model when a cheaper model can do the job.

#### **Step three: add multiple backends behind the gateway.**

Once the gateway is in place, it doesn't have to point at one destination. A request for a specific model can go to that model hosted on your hyperscaler, get routed to the vendor's own API when there's a reason to, or land on an equivalent open-weight model through a third-party inference provider for a speed or cost advantage. Your applications never know the difference, because to them an endpoint is an endpoint. Your infrastructure team decides where the traffic goes.

## What the Gateway Buys You

The gateway itself is a small, self-contained piece of software (a UI, an API, and usually a Postgres-backed data layer) that you run on the same cloud as your models. Once it's running, a few capabilities show up that you don't get any other way.

Every user or team gets a **virtual key** instead of a raw API key. That key can carry a budget, a cost ceiling, and a model routing policy, so a $50-a-week limit for a team or a per-request cost cap for a product line becomes something you enforce technically instead of asking people to respect.

**Model routing** happens automatically once policy is in place. A simple request can get quietly routed to a cheaper open-weight model without the user ever knowing, at a fraction of the cost of the frontier model they asked for by default.

**Data governance** runs at the same layer. If a prompt contains something that shouldn't leave the environment, the gateway can strip it or block the request before it reaches any external provider.

**Observability** is the piece most teams don't realize they're missing until they have it. Provider dashboards give you basic usage charts, because their incentive is for you to use more AI, not less. A gateway gives you real visibility into who's using what, at what cost, with what outcome, across every team and every provider at once.

Several of these platforms also run an **MCP gateway**. This solves the real headache of giving an AI agent secure access to something like your Jira board, which usually means handing users more credential access than you'd like. A gateway can hold hardened, enterprise-grade authentication for that connection centrally, so users get the capability without anyone having to manage the credentials themselves.

You don't need to build this from scratch. LiteLLM was one of the first open-source gateways to mature into something enterprise-ready, and there are a dozen or more legitimate options now, from Bifrost to Kong AI to Portkey.

![image 2 - Own the Interface: Why Enterprise AI Needs a Governed Gateway ](images/AdobeStock_1506343687.jpeg)

## The Cost Metric That Actually Matters

Once you have this visibility, the conversation shifts from **cost per token** to **cost per successful task**. That distinction matters more than it sounds like it should. A hundred dollars in tokens can be worth its weight in gold, or it can be a hundred dollars wasted, plus the time lost cleaning up after it.

Two runs can burn identical token counts and produce completely different value. An open-weight model that costs a third of the price per token isn't a third of the cost if it needs twice as many tokens to finish the same task. Gateways are starting to build early versions of this metric in, and it's worth getting ahead of before it becomes the standard way finance asks about AI spend.

## This Reaches Further Than Your Own Agents

The same architecture applies to the tools your developers already use. Claude Code, Codex, and similar harnesses point at a provider's API by default, but they're typically two or three configuration settings away from pointing at your gateway instead. On managed machines, that's a policy your IT team can push without users noticing anything changed, beyond the fact that their usage is now governed, budgeted, and visible.

It also solves a problem that looks like a software maintenance problem but is really a model lifecycle problem. Applications and agents outlive the models they were built against. When a provider sunsets a model your production agent depends on, migrating that workload happens at the gateway, on the virtual key, without touching the application code at all.

## Deciding When to Move

Not every organization needs to reach step three on day one. Four variables tell you when to move:

1. Your current monthly AI spend
2. Your growth rate in tokens or active users over the past twelve months
3. Whether your applications have latency requirements a routing layer might affect
4. Whether compliance or data residency requirements already constrain your options

In practice, compliance is usually what accelerates the timeline. Even organizations with modest spend move to a gateway sooner once they realize it's the only way to demonstrate to auditors that their AI usage actually aligns with SOC 2, GDPR, or their existing cloud governance standards. Everyone else can build the case on cost and flexibility alone. For most teams, that means running your own numbers before picking a date.

It's also worth knowing there's a fourth option outside the gateway architecture entirely: running smaller open-weight models locally, on hardware you own. A high-RAM laptop can run models like Qwen with inference that never leaves the device, which sidesteps the residency and privacy questions completely in exchange for an upfront hardware cost instead of an ongoing cloud bill. It won't replace frontier-model workloads, but for the right use cases, it's a real option worth having on the table alongside the gateway.

## Reminder: This Isn’t a Vendor Swap

Swapping vendors gets you the same service under different pricing. Owning the interface changes your actual frame of reference like which models your teams can use, how you control spend, how you prove compliance, and how fast you can move when the leaderboard shifts again next quarter (because it will).

If you want help running these numbers against your own workload or working out where you sit on the path from a direct API call to a fully governed, multi-backend gateway, Improving would love to hear what you're building. [Reach out to our team](https://improving.com/contact), and let's figure out what the right next step looks like for you.
