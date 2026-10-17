---
title: "Microsoft Purview"
type: "Entity"
description: "Microsoft's data governance and compliance product, positioned in this corpus as the governance arm of a unified AI asset layer."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, compliance, platform]
sources:
  - "/sources/governance-as-the-control-plane-for-ai.md"
  - "/sources/nobody-is-building-a-separate-silo-for-ai-assets-anymore.md"
  - "/sources/the-architecture-of-enterprise-ai-retrieval.md"
  - "/sources/the-four-layers-of-runtime-ai-governance.md"
---

# Microsoft Purview

Microsoft Purview is a data governance and compliance product. In this corpus it stands as the governance half of Microsoft's answer to AI asset management — paired with [Microsoft Entra Agent ID](/entities/microsoft-entra-agent-id.md) for identity — and as one vendor's implementation of a governance [control plane](/concepts/control-plane.md).

## Key Claims

- Microsoft gives agents identity via Entra Agent ID and governance via Purview, converging with Databricks Unity Catalog, AWS, and Google on one architecture ([nobody is building a separate silo](/sources/nobody-is-building-a-separate-silo-for-ai-assets-anymore.md))
- Governance must be a runtime control plane, not a policy document: only a control plane can see, stop, or detect violations ([governance as the control plane](/sources/governance-as-the-control-plane-for-ai.md))
- Only 8% of organizations rated their governance program highly successful, and agents act at machine speed without the judgment that made human audit viable.
- Four layers — policy, inventory, monitoring, enforcement — form a dependency chain, with runtime enforcement the hardest and most commonly missing ([the four layers](/sources/the-four-layers-of-runtime-ai-governance.md))
- Enterprise retrieval needs distinct gates, including [permission pre-filtering](/concepts/permission-pre-filtering.md) that hard-excludes before scoring ([enterprise ai retrieval](/sources/the-architecture-of-enterprise-ai-retrieval.md))

## Related

- [AI Governance](/concepts/ai-governance.md) — the discipline Purview serves
- [Control plane](/concepts/control-plane.md) — the architectural pattern
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — the hardest layer
- [Microsoft Entra Agent ID](/entities/microsoft-entra-agent-id.md) — the paired identity product
- [Microsoft](/entities/microsoft.md) — the vendor
