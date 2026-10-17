---
title: "One Catalog, Every Consumer"
type: "Source Summary"
description: "Four 2026 enterprise agent platforms each cover only two or three of five governance capabilities, so buyers must build the gaps deliberately."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/one-catalog-every-consumer/one-catalog-every-consumer.md"
---

# One Catalog, Every Consumer — Summary

**Original source**: `references/devlinliles.com/one-catalog-every-consumer/one-catalog-every-consumer.md`

## Summary

Vendors claim their platforms do "everything," but an honest map of five capabilities from this series — unified catalog, progressive discovery, a [review gate](/concepts/review-gate.md) with separation of duties and version pinning, scalable ownership, and cross-boundary [federation](/concepts/federation.md) — covers only two or three per vendor. Four platforms shipped real capability in the first half of 2026, and none shipped all five. The pattern: each platform's governance is strongest at the edge of its own boundary and weakens the moment an agent crosses into another cloud, vendor, or company.

## Key Claims

- Microsoft Agent 365 (GA SDK at Build 2026) unifies the agent registry and extends [agent identity](/concepts/agent-identity.md) and ownership via Entra ID Governance, but its review gate — MDASH (96.55% on CyberGym) and Purview runtime DLP — is still in preview.
- Google's Gemini Enterprise Agent Platform (GA April 22, 2026) names Agent Identity, Agent Registry, and Agent Gateway as three separate products, matching the five-part structure, but Agent Registry is still a preview feature.
- Salesforce Agentforce 360 bakes a review gate into authoring via Agent Script and deterministic orchestration; ServiceNow's Action Fabric opens a generally available [MCP](/entities/model-context-protocol.md) server for cross-vendor action governance.
- No vendor solves the seam where agents cross organizational boundaries, because doing so would mean ceding control to a neutral layer none of them owns.
- Buyers should identify which two or three boxes their chosen platform leaves unchecked and build those deliberately.

## Relevance

Informs [review gates](/concepts/review-gate.md), [agent identity](/concepts/agent-identity.md), and [federation](/concepts/federation.md), extending the catalog-as-control-plane argument.

## Quality

Practitioner blog post by Devlin Liles. Well-structured vendor comparison with a summary table and dated GA/preview status; the five-part rubric is the author's own framework and coverage calls are judgment.

## Entities Mentioned

- [Model Context Protocol](/entities/model-context-protocol.md) — ServiceNow's open MCP server for cross-vendor actions

## Concepts Covered

- [Review Gate](/concepts/review-gate.md) — separation-of-duties gate before a skill ships
- [agent identity](/concepts/agent-identity.md) — cryptographic per-agent identity distinct from humans
- [AI Inventory](/concepts/ai-inventory.md) — registry of every agent running against the org
- [federation](/concepts/federation.md) — governance extended across boundaries the platform doesn't control
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — gateway governing tool calls before execution

## Related Sources

- [A Skill Registry Needs a Review Gate, Not Just a Folder](/sources/a-skill-registry-needs-a-review-gate-not-just-a-folder.md)
- [Publishing a Catalog Is Not the Same as Running a Registry](/sources/publishing-a-catalog-is-not-the-same-as-running-a-registry.md)
