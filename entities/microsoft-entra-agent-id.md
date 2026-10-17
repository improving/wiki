---
title: "Microsoft Entra Agent ID"
type: "Entity"
description: "Microsoft's identity service for AI agents, giving non-human principals first-class identity, scoping, and runtime policy."
created: '2026-10-17'
updated: '2026-10-17'
tags: [identity, security, governance]
sources:
  - "/sources/the-architecture-of-enterprise-ai-retrieval.md"
  - "/sources/your-agents-are-principals-treat-them-like-it.md"
---

# Microsoft Entra Agent ID

Microsoft Entra Agent ID extends the Entra identity platform to AI agents, treating them as non-human principals with their own identities, permissions, and lifecycle. This corpus cites it as the concrete infrastructure for governing agents at scale.

## Key Claims

- 91 percent of organizations deployed agents; only 10 percent have a governance strategy.
- Agents break human security assumptions: machine speed, dynamic permissions, injectable.
- Indirect prompt injection is OWASP's top LLM risk, with real CVEs.
- Permissions, not the model, are the perimeter; scope them to bound blast radius.
- Permissions must hard-exclude before scoring; tags should soft-boost to preserve precision.

## Work

Entra Agent ID makes the corpus's "agents are principals" argument operational: each agent gets an identity that can be scoped, audited, and constrained at runtime. The same identity boundary governs enterprise retrieval, where permissions must hard-exclude documents before scoring rather than filter results afterward.

## Related

- [Mythos 5](/entities/mythos-5.md) — a model whose governance depends on such identity infrastructure
- [agent identity](/concepts/agent-identity.md) — the concept it implements
- [Least privilege](/concepts/least-privilege.md) — the scoping principle it enforces
- [Permission Pre-Filtering](/concepts/permission-pre-filtering.md) — the retrieval pattern it enables
- [Your Agents Are Principals. Treat Them Like It.](/sources/your-agents-are-principals-treat-them-like-it.md) — primary source
