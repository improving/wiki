---
title: "Engineering Behind the Color: Software for a Global Paint Brand"
type: "Source Summary"
description: "A global paint brand built a secure internal RAG assistant on Azure AI, succeeding by fixing messy legacy data and refining how users ask questions."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, data, improving.com]
sources:
  - "references/improving.com/engineering-behind-the-color-software-for-a-global-paint-brand/engineering-behind-the-color-software-for-a-global-paint-brand.md"
---

# Engineering Behind the Color: Software for a Global Paint Brand — Summary

**Original source**: `references/improving.com/engineering-behind-the-color-software-for-a-global-paint-brand/engineering-behind-the-color-software-for-a-global-paint-brand.md`

## Summary

A global paint brand set out to stop employees from pasting confidential data into public AI tools, and built an internal generative-AI assistant inside a protected Azure cloud environment instead. The first use case let employees query internal product data sheets; the real work turned out to be curating two decades of messy, conflicting legacy content. Improving's differentiator was a smarter RAG design plus a reasoning layer that sharpened vague sales questions before retrieval.

## Key Claims

- The original driver was security: keep employees from exposing confidential data or training external models.
- Everything ran inside a protected Azure environment so sensitive information stayed private and was never reused for external training.
- Best practices for enterprise RAG were still emerging, so the solution evolved alongside the technology.
- Product data sheets spanned nearly two decades and referenced discontinued products, overlapping recommendations, and inconsistent terminology across acquired companies.
- Apparent AI "hallucinations" were often symptoms of outdated or conflicting source material rather than model failure.
- Fully normalizing data into rigid structures hit practical limits; filtering invalid documents, categorizing by relevance, and prompt design worked better.
- A reasoning layer that refined and deepened broad sales questions before querying dramatically improved answer quality.
- Power Platform Canvas Apps delivered the front end fast; Azure AI Foundry now reduces assembly to configuration and integration.

## Relevance

A concrete enterprise case for [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) and [prompt engineering](/concepts/prompt-engineering.md), showing that [data readiness](/concepts/data-readiness.md) — not model choice — was the binding constraint.

## Quality

Practitioner case study by Shelby Sansone Stephens; concrete on the data and prompt problems, but vendor-adjacent to Microsoft and Improving.

## Entities Mentioned

- [Improving](/entities/improving.md) — delivery partner
- [Microsoft](/entities/microsoft.md) — Azure AI foundation
- [Microsoft Power Platform](/entities/power-platform.md) — Canvas Apps front end
- [Bill Curry](/entities/bill-curry.md) — Improving VP quoted on AI and knowledge

## Concepts Covered

- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — internal knowledge assistant
- [prompt engineering](/concepts/prompt-engineering.md) — question-refining reasoning layer
- [data readiness](/concepts/data-readiness.md) — legacy data as the real blocker
- [AI adoption](/concepts/ai-adoption.md) — secure internal rollout
