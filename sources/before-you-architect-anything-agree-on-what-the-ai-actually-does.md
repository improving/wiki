---
title: "Before You Architect Anything, Agree on What the AI Actually Does"
type: "Source Summary"
description: "A two-part taxonomy-and-ontology scheme for classifying AI systems before architecture and governance decisions."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/before-you-architect-anything-agree-on-what-the-ai-actually-does/before-you-architect-anything-agree-on-what-the-ai-actually-does.md"
---

# Before You Architect Anything, Agree on What the AI Actually Does — Summary

**Original source**: `references/devlinliles.com/before-you-architect-anything-agree-on-what-the-ai-actually-does/before-you-architect-anything-agree-on-what-the-ai-actually-does.md`

## Summary

Most enterprise AI disputes are arguments about words: one person says "agent," another hears "chatbot," and nobody is building the same thing. Devlin argues a shared classification language is the cheapest, highest-leverage artifact an AI practice can own, and proposes a two-part scheme — a taxonomy of what a model produces and an ontology of how it is built and run. Classify before you architect; three discovery questions do most of the work.

## Key Claims

- A two-tier taxonomy: three core families (predictive, generative, perceptive) plus three applied decision patterns (prescriptive, recommendation, decision intelligence) layered on top.
- The perceptive/predictive boundary resolves by intent — describing patterns in data versus scoring a new observation — not by data type.
- Autonomy level is the single largest determinant of risk, change management, and required observability; latency profile drives deployment topology, model size, and retrieval strategy.
- Gartner reported a 1,445% jump in multi-agent system inquiries between early 2024 and mid-2025.
- The ontology maps cleanly onto NIST AI RMF and OECD classification frameworks when a client needs a governance crosswalk.

## Relevance

Grounds [AI governance](/concepts/ai-governance.md) and [human-in-the-loop](/concepts/human-in-the-loop.md) decisions in an explicit classification step before architecture is chosen.

## Quality

Practitioner blog post by Devlin Liles. Strong structured framework; the one quantitative figure is a cited industry-analyst statistic, and the scheme is the author's own construction.

## Entities Mentioned

- [Gartner](/entities/gartner.md) — source of the multi-agent inquiry statistic
- [NIST AI RMF](/entities/nist-ai-rmf.md) — framework the ontology crosswalks onto

## Concepts Covered

- [AI Governance](/concepts/ai-governance.md) — classification as the prerequisite for governance
- [human-in-the-loop](/concepts/human-in-the-loop.md) — guided/approval-gated autonomy levels in the taxonomy

## Related Sources

- [AI Governance Is Data Governance With Consequences](/sources/ai-governance-is-data-governance-with-consequences.md)
- [Five Firms Built Five AI Frameworks. None of Them Built a Ruler.](/sources/five-firms-built-five-ai-frameworks-none-of-them-built-a-ruler.md)
