---
type: Reference
title: "The Four Layers of Runtime AI Governance"
resource: "https://www.devlinliles.com/the-four-layers-of-runtime-ai-governance/"
author: "Devlin Liles"
published: '2026-07-20'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

August 2 is five weeks away.

That's the date the EU AI Act's Annex III high-risk AI obligations take full effect. Credit decisions, hiring systems, critical infrastructure controls, educational scoring, law enforcement AI: if your organization operates any of those in Europe, compliance is no longer optional. The audit trail, the human oversight mechanisms, the documentation of training data and model performance: those are legal requirements starting in five weeks.

The tooling gap is what I want to talk about. The majority of organizations I've worked with this year have invested in the wrong layer, and that's going to matter on August 3.

**Four layers, not one**

A complete AI governance stack runs across four layers. They work in sequence. Each depends on the one below it.

**Layer one: Policy and compliance management.** Defining what the organization allows, under what conditions, and with whose authorization. Capturing attestations and approval records. Checking AI deployments against rules and regulatory requirements. Generating audit-ready documentation when a regulator or auditor asks. For organizations anchored on Microsoft 365 and Azure, Microsoft Purview is the default first stop. Purpose-built tools like Credo AI map development and deployment steps against a defined policy pack and automate compliance assessments across NIST AI RMF and EU AI Act frameworks.

**Layer two: AI inventory and shadow AI discovery.** You cannot govern what you don't know about, and most organizations don't know what they have. Individual employees using personal AI accounts for work tasks. Browser-embedded AI assistants that went through no procurement review. AI features embedded in SaaS tools that IT evaluated two years ago, before the AI features existed. Every one of those is a governance gap. Microsoft Defender for Cloud Apps discovers unsanctioned SaaS and AI usage for M365 environments.

**Layer three: Model monitoring and drift detection.** Deployed models behave differently over time. The data distribution they were trained and validated on shifts as the world changes. A model that was accurate and fair when you approved it may not be now. Fiddler AI does real-time production monitoring: data drift, model drift, prediction anomaly detection, performance degradation, explainability. Azure AI Foundry handles this natively for workloads on Azure with direct integration to Purview. The key requirement: monitoring has to be continuous and automated.

**Layer four: Runtime policy enforcement.** This is where most enterprises have almost nothing, and where it matters most.

A centralized gateway sits between an AI agent and every tool it can call. When an agent proposes an action, the gateway evaluates that action against the active policy pack, the identity and permissions of the agent, and any current limit or budget controls — before the action executes. If the action falls within policy, it proceeds. If it doesn't, it stops. The decision is logged either way. The audit trail is generated at the action level automatically.

This is a qualitatively different kind of governance from the first three layers. Policy management and inventory are about knowing the rules and knowing what you have. Monitoring is about detecting drift after the fact. Runtime enforcement is the only layer where the governance system actually intercepts a wrong action before it happens. It is also the only layer where "audit-ready" means the record was generated at the moment of the decision, not assembled afterward from whatever logs happened to survive.

The picture is not encouraging. Most large enterprises have meaningful coverage in layer one. Fewer than half have done a real AI inventory. Model monitoring in production is spotty. Runtime enforcement at the agentic layer is almost entirely absent.

**Why layer four is the hard one**

The tooling exists. Enterprise MCP Gateway architectures are a 2026 pattern that several vendors are building against. The challenge isn't availability of tooling. It's that layer four requires layers one through three to be done correctly first. The runtime gateway enforces the policy pack. If the policy pack doesn't exist, the gateway enforces nothing meaningful. You can't shortcut the sequence.

**The non-human identity problem no one is talking about**

Agent identity is the control nobody is talking about. Every agentic AI action executes under a set of credentials, permissions, and access rights. In most current deployments, agents run under over-provisioned service accounts that haven't been audited in months. An agent configured to access the CRM inherits everything that service account can reach.

Before deploying any agent with file or system access, run a permission audit. Compare the service account's current permissions against the actual scope of what the agent's workflow needs. Treat agent identity with the same rigor as privileged human identity, because the blast radius of a misconfigured agent is comparable.

**Where to start with five weeks left**

If August 2 matters to your organization: confirm scope (which systems fall under Annex III), close the layer one documentation gaps with audit-ready evidence, run an inventory sweep for shadow AI, and be honest about where your monitoring and runtime controls actually sit.

The organizations I've seen ahead on this started with a shadow AI audit, not a governance framework. They knew what they had before they tried to govern it. From there, each closed the highest-risk layer gap for their specific exposure, in sequence, without trying to do all four at once.

The sequence is not complicated. What makes it hard is the organizational commitment to treat governance as an engineering problem, not a documentation project.

---

*This is the final post in a three-part series on active AI governance. Part 1 covered why policy documents aren't governance. Part 2 covered the people and process architecture.*
