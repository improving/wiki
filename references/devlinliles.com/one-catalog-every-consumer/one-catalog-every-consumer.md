---
type: Reference
title: "One Catalog, Every Consumer"
resource: "https://www.devlinliles.com/one-catalog-every-consumer/"
author: "Devlin Liles"
published: '2026-09-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Ask a vendor whether their platform does everything this series has described, catalog and registry together, review gates before a skill ships, ownership that scales past one team, federation that holds up at the edge of the organization, and the answer is yes. Ask what "everything" means to them specifically, and the honest map only covers two or three of the five. That gap between the pitch and the actual coverage is worth mapping directly, because four platforms shipped real, dated, GA-or-near-GA capability against this exact problem in the first half of 2026, and none of them shipped all of it.

The five things worth checking for, pulled straight from the rest of this series: a unified catalog that resolves the same capability for a person and a pipeline, not two descriptions that drift apart. Progressive, metadata-first discovery so an agent isn't drowning in every skill it could theoretically call. A review gate with separation of duties, evaluation, and version pinning before anything reaches production. An ownership structure that scales past a single central team without losing scrutiny on what actually carries risk. And federation that extends the same governance across a boundary the platform itself doesn't control, another cloud, another vendor, another company entirely.

## Microsoft Agent 365

Agent 365 shipped its SDK into general availability at Build 2026, and the shape of it is a direct answer to the ownership and review-gate problem this series spent two posts on. The Agent 365 registry, which absorbed the agent inventory that used to live separately in Microsoft Entra, gives an organization one place to see every agent running against it, including ones nobody provisioned on purpose. Microsoft says the registry recognizes more than twenty kinds of local agents, coding agents and MCP servers included, which is the exact skill-sprawl problem from earlier in this series, except surfacing shadow agents instead of duplicate SKILL.md files. Entra ID Governance extends scoped permissions, ownership accountability, and time-bound access to agent entitlements the same way it already does for human accounts, which is the ownership-structure answer this series has been building toward since the piece on who owns the skill library.

Where it thins out is the review gate itself. Microsoft's own scanning system, MDASH, benchmarks well, a reported 96.55% on CyberGym, but it's still in expanded preview, and Purview's runtime data-loss prevention for agent prompts is preview too. A registry that shows what exists is a different thing from a pipeline that stops a bad skill before it ships, and as of mid-2026 the piece of Agent 365 that does the stopping is the piece still in preview.

## Google Gemini Enterprise Agent Platform

Google's platform, generally available since April 22, 2026, is architecturally the closest thing on the market to the five-part structure this series has described, because it names the same three layers separately: Agent Identity for a cryptographic per-agent identity distinct from any human user, Agent Registry as what Google's own documentation calls "a single source of truth" for approved tools and agents, and Agent Gateway as the enforcement point that governs every tool call before it executes. That's catalog, identity, and runtime enforcement as three explicit products rather than one bundled feature, and it maps almost one to one onto the sequence this series laid out for a governed skill pipeline.

The catch is maturity, not architecture. Google's own documentation marks Agent Registry as a preview feature, subject to the reduced support terms that come with anything pre-GA. The RAG Engine underneath it does support hybrid search and reranking natively, which answers the retrieval half of this series directly, but the governance half, the part that determines whether a skill or agent can be trusted, is still earlier in its lifecycle than the retrieval half is.

## Salesforce and ServiceNow

Salesforce's answer is Agent Fabric, a control plane inside Agentforce 360 built around deterministic orchestration rather than open-ended agent autonomy, paired with Agent Script, a human-readable expression language for defining exactly what an agent is and isn't allowed to do. That's a review-gate philosophy baked into the authoring step itself rather than bolted on after, which is a genuinely different bet than Microsoft's or Google's registry-first approach. Data 360 extends governance to the unstructured documents and transcripts feeding those agents, which is the same "ground the skill in a governed source" principle this series covered when it addressed why a flawless skill can still return a confidently wrong number.

ServiceNow took the opposite entry point: instead of building its own agent authoring layer, it opened Action Fabric so third-party agents, ServiceNow's own, Copilot, Claude, a homegrown one, can trigger ServiceNow workflows and approvals through a generally available MCP server. Otto unifies conversational AI, enterprise search, and workflow execution into one interface, which is the person-and-pipeline-asking-the-same-question problem from earlier in this series, answered for ServiceNow's own workflow surface specifically. What ServiceNow is selling is less a skill registry than a governed action layer sitting downstream of whatever registry an organization already has, which makes it a strong complement to Microsoft's or Google's catalog rather than a substitute for one.

## Where every one of them shares the same gap

Lay the four side by side and a pattern holds that should sound familiar from the federation piece earlier in this series. Each platform's governance is strongest exactly at the edge of its own boundary and weakens the moment an agent has to cross into someone else's cloud, someone else's vendor, or someone else's company. Microsoft's controls run deepest inside Windows, Entra, and Microsoft Foundry. Google's run deepest inside Gemini Enterprise and Google Cloud IAM. Most real enterprises run agents across more than one of these plus a long tail of SaaS tools with their own embedded assistants, and none of the four vendors has solved what happens at that seam, because solving it would mean ceding some control to a neutral layer none of them owns. That's not a failure of engineering. It's the same incentive problem this series named when it covered why Agentic Resource Discovery is a real answer to a narrower question than the one this series has been asking.

| Platform | Catalog / registry | Progressive discovery | Review gate | Ownership structure | Cross-boundary federation |
| --- | --- | --- | --- | --- | --- |
| Microsoft Agent 365 | Yes, unified, GA | Partial (Entra-scoped) | Preview (MDASH, Purview runtime) | Yes, via Entra ID Governance | Weak outside Microsoft stack |
| Google Gemini Enterprise | Yes, preview | Yes (RAG Engine hybrid + rerank) | Partial, preview-stage | Yes, via IAM + semantic policy | Weak outside Google Cloud |
| Salesforce Agentforce 360 | Partial (Agent Fabric) | Not the focus | Strong, authoring-time (Agent Script) | Yes, centralized in Fabric | Weak outside Salesforce |
| ServiceNow Action Fabric | No native registry | Not the focus | Downstream, action-level only | Governs actions, not authorship | Strongest cross-vendor (open MCP) |

## What this means for a decision being made now

None of this is a reason to wait for a platform that covers all five. It's a reason to be precise about which two or three an organization is actually buying when it picks one, and to build the rest deliberately rather than assume the vendor already has. For an organization already anchored on Microsoft 365, Entra, and Intune, Agent 365 is the natural default specifically because the ownership and identity layer already exists and simply extends to agents, with the honest caveat that the review-gate piece needs a bridge, internal evaluation and security review, until MDASH and Purview's runtime controls clear preview. An organization already deep in Google Cloud gets the cleanest architectural match to this series' five-part structure, with the same preview-stage caveat sitting on the registry itself. Salesforce and ServiceNow are worth adding to either stack for what they do best, deterministic authoring and cross-vendor action governance respectively, not as replacements for the identity and catalog layer underneath them.

The organizations that get this right in the next year won't be the ones that pick the platform with the longest feature list. They'll be the ones that read a list like this one, know exactly which two boxes their chosen platform leaves unchecked, and go build those two on purpose instead of discovering the gap during an incident.

---

*Sources: Microsoft, "Agent Registry convergence with Microsoft Agent 365" (Microsoft Learn, updated 2026-05-09); Janakiram MSV, "Microsoft Makes Governance the Gate for Enterprise AI Agents" (Forbes, 2026-06-09); Google Cloud, "Agent Registry" and "Agent Platform overview" (Gemini Enterprise Agent Platform documentation, 2026); Salesforce, "Governing AI Agents with Agentforce 360 Platform" and "Salesforce Advances Agent Fabric" (2026); ServiceNow Knowledge 2026 product announcements and newsroom coverage; Everest Group, agentic AI review of ServiceNow Knowledge 2026.*
