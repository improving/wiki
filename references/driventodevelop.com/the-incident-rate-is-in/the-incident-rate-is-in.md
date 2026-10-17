---
type: Reference
title: "The Incident Rate Is In"
resource: "https://driventodevelop.com/2026/09/21/the-incident-rate-is-in/"
author: "David O'Hara"
published: '2026-09-21'
fetched: '2026-10-17'
tags: [blog, driventodevelop.com]
---

We spent two years talking about AI agent security as a risk to manage before something goes wrong. New research says something already went wrong. Eighty-eight percent of enterprises confirm it.

In conversations with clients over the past year, my agent security framing was almost always forward-looking: here is what could happen if you do not get the identity layer right. Strata's 2026 research on enterprise AI identity ends that framing. Eighty-eight percent of organizations reported a confirmed or suspected AI agent security incident in the last year. Ninety-two percent lack full visibility into their AI identities. The "before something goes wrong" window has closed for most of the room.

The root cause is specific: teams are sharing human credentials and access tokens with agents because no dedicated agent identity infrastructure exists. Agents run with the same access as the person who set them up, which means they can reach ERP systems, CRMs, and financial data with no scope limitation and no audit trail distinguishing agent actions from human ones. This is exactly what we address with the Agentic Landing Zone at Improving: a structured approach to releasing agents safely, with the right access boundaries, the right governance model, and the right visibility so you know what goes where.

The technical fix is not complicated conceptually: registered OAuth clients for each agent, short-lived scoped tokens, per-task authorization, and audit logs that track agent provenance separately from human provenance. That is not a governance initiative. That is an architecture decision that follows the governance you want. The harder shift is reframing the client conversation. The question used to be "are you prepared for an AI agent security incident?" Eighty-eight percent of the data says that question has already been answered. The current question is: do you know which of your incidents last year involved an agent, and does your incident response process handle that differently?

When your team ran that last security incident, was there a way to flag the ticket as "agent-initiated action"? If not, you may have had one and don't know it. Better check.

[
![David O'Hara](images/Headshot---current.jpg)
](https://driventodevelop.com/author/david/)

[David O'Hara](https://driventodevelop.com/author/david/)

21 Sep 2026

[AI](https://driventodevelop.com/tag/ai/)
