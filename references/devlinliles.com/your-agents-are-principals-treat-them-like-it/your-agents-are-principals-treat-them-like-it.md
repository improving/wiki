---
type: Reference
title: "Your Agents Are Principals. Treat Them Like It."
resource: "https://www.devlinliles.com/your-agents-are-principals-treat-them-like-it/"
author: "Devlin Liles"
published: '2026-07-20'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Ninety-one percent of organizations have already deployed AI agents. Ten percent have a governance strategy for them. That gap is a decision that hasn't been made yet. The window to make it cleanly is closing.

I have watched this exact pattern before. A decade ago, service accounts proliferated across enterprise environments faster than any access review process could track them. They were created for convenience, granted broad permissions because scoping them precisely took too long, and then forgotten. When those accounts were compromised, the blast radius was almost always larger than it needed to be. The security principles were there. We just didn't apply them to service accounts with the same rigor we applied to humans. Agents are service accounts at 80 times the scale, with autonomous action capability bolted on top.

## Every security framework we have was designed for humans

That is the structural problem. Zero trust, identity governance, UEBA, access reviews: the entire security stack assumes the principal at the other end of a session is a person who authenticates, reasons about what they are authorizing, and behaves within predictable bounds across a working day. Agents violate every one of those assumptions simultaneously.

An agent authenticates. It does not think about what it is authorizing. It operates at machine speed, which means it can take thousands of actions in the time a person would take one. It acquires permissions dynamically during task execution, which makes the static quarterly access review not just inadequate but structurally useless. And it cannot be phished. It can be injected. The attack moves to the environment, not the inbox.

This is what OWASP ranks as the number one risk for LLM applications: indirect prompt injection, or XPIA. An adversarial instruction embedded in content the agent retrieves — a web page, a calendar event, a document in SharePoint, an email — and the user and operator never see it. CVE-2025-32711, called EchoLeak, scored a CVSS 9.3 and demonstrated exactly this: adversarial instructions embedded in PowerPoint speaker notes caused Copilot to return sensitive email data to the attacker. CVE-2025-53773 achieved remote code execution via prompt injection in GitHub Copilot. These have CVE numbers.

The Model Context Protocol supply chain adds another layer. MCP accumulated 99 published CVEs in 2025 alone. Tool poisoning attacks embed adversarial instructions in tool descriptions, invisible to users, processed as operational context by the model. The OWASP MCP Top 10 now exists because the threat surface is real enough to warrant its own taxonomy.

Microsoft's red team spent a year cataloging what goes wrong at scale. Their Taxonomy of Failure Modes in Agentic AI Systems hit version 2.0 on June 4, 2026, seven categories larger than the April 2025 v1.0. The additions (supply chain compromise, tool abuse, excessive agency, feedback loop poisoning, goal misalignment, reasoning-based information leakage, autonomy escalation) are failure patterns observed in real deployments, not hypotheticals.

## The tools already exist

You probably already have the tools. You need the policies and the playbook applied to a new class of principal.

Microsoft's answer is Entra Agent ID, announced at Ignite 2025. It extends the Entra ID identity fabric directly to agents: autonomous agents get their own identity and authenticate via client credentials flow; delegated agents act on behalf of a human user with that user's scoped permissions. Both are subject to the same Conditional Access policies, the same Identity Protection risk signals, the same Workload Identity Federation for secretless auth you already apply to human accounts. The governance machinery you already built for humans extends to agents. You just have to make the deliberate decision to point it there.

API keys, OAuth tokens, AWS access keys, GitHub PATs, AI agents: all of these already outnumber human identities 50:1 in some enterprises. CyberArk puts the machine-to-human ratio at 80:1 across their customer base, with 68% of organizations lacking identity security controls for AI systems specifically. Okta's Identity Security Posture Management now covers non-human identities with the same lifecycle management and policy enforcement applied to human accounts. The lifecycle is the same: provision, scope, monitor, review, revoke.

Agents have predictable operational envelopes. A document summarization agent calls specific tools, accesses documents within a defined scope, and completes tasks within an expected time window. Deviations map directly to existing UEBA detection logic. Microsoft Entra Agent ID's Identity Protection risk signals apply behavior-based risk scoring to agent identities using the same signal model used for human accounts.

CyberArk's AI Agent Gateway takes privilege to its logical conclusion: zero standing privileges for agents, with ephemeral OAuth tokens scoped per request. The token exists for the duration of the action and no longer. If an agent is compromised mid-session, the blast radius is bounded by what that token could reach, not by what the agent's broad standing permissions could reach.

## The compliance picture is jury-rigged but workable

SOC 2 Type II has no control families specific to agent identity, agent behavior monitoring, or agentic supply chain integrity. Organizations doing this work today are mapping agent risks into existing categories: access control, change management, monitoring. That is the right move, and it is workable with careful documentation of the mapping. NIST AI RMF (AI 600-1 for generative AI) combined with ISO/IEC 42001:2023 is the closest thing to a deployable compliance baseline. The EU AI Act's high-risk obligations, including 15-day serious-incident reporting, activate August 2, 2026.

The IETF published its first formal draft for AI agent authentication in March 2026 (draft-klrc-aiagent-auth-00), composing SPIFFE and OAuth 2.0 into a coherent authentication model. The scaffolding is being built. The question is whether your governance program is being designed to stand on it.

## What the ratio means for governance

The NHI ratio (80 machine identities for every human one) makes manual access governance operationally impossible. That's not a scaling challenge — it's a category change. Agents are created and destroyed faster than any human-reviewed provisioning cycle can handle. The governance model has to shift from review-at-provisioning to policy-as-code enforced at runtime. Microsoft's Agent Governance Toolkit, open-sourced in April 2026, is built on exactly this: sub-millisecond policy enforcement at runtime, addressing all ten OWASP Agentic AI risks.

The attack surface that matters is what the agent can reach. An agent with read-only access to a scoped SharePoint library has a bounded blast radius. An agent with broad delegated permissions across Exchange, SharePoint, Teams, and your CRM does not. The security conversation about agentic AI keeps defaulting to "how do we make the model safer." That is the wrong frame. The model is not the perimeter. The permissions are the perimeter. Scope the permissions, scope the blast radius. That principle is twenty years old and it applies here without modification.

There is no light switch moment on this. Organizations that are serious about agentic AI deployment in the next twelve months need to make agent identity a first-class concern before the agents are in production, not after the first incident. The security principles are twenty years old. Applying them is the decision that hasn't been made.

---

*Sources: Microsoft Entra Agent ID (Ignite 2025); Microsoft Taxonomy of Failure Modes in Agentic AI Systems v2.0 (June 4, 2026); Microsoft Agent Governance Toolkit (April 2026); Okta NHI research (2025); CyberArk AI Agent Gateway and machine identity report (2025); OWASP Top 10 for Agentic Applications 2026; OWASP MCP Top 10; IETF draft-klrc-aiagent-auth-00 (March 2026); CVE-2025-32711 (EchoLeak, CVSS 9.3); CVE-2025-53773 (GitHub Copilot RCE); EU AI Act timelines.*
