---
title: "When MCP Is Not The Right Choice"
type: "Source Summary"
description: "Argues Model Context Protocol is powerful when needed but expensive over-engineering otherwise, with a decision framework and red flags."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, architecture, improving.com]
sources:
  - "references/improving.com/when-mcp-is-not-the-right-choice/when-mcp-is-not-the-right-choice.md"
---

# When MCP Is Not The Right Choice — Summary

**Original source**: `references/improving.com/when-mcp-is-not-the-right-choice/when-mcp-is-not-the-right-choice.md`

## Summary

Model Context Protocol (MCP) gives LLMs a standard way to reach tools and data, and it is powerful when users genuinely need orchestration. This post argues it becomes expensive over-engineering when they don't. It lays out the benefits, the hidden operational and security costs of production adoption, red flags for when MCP is the wrong choice, and a decision framework.

## Key Claims

- MCP is a model-agnostic protocol that decouples AI applications from individual model providers.
- Benefits: standardization and interoperability, developer velocity and reuse, centralized governance, and architectural flexibility.
- Hidden costs: an operational complexity tax, an extra network hop of tens to hundreds of milliseconds per call, an enlarged security blast radius, a nascent ecosystem, and hard multi-boundary debugging.
- The postmark-mcp case involved a malicious server BCC'ing emails to attackers, exposing memos and invoices.
- Red flags: customer-facing latency sensitivity, minimal or static integrations, regulated security gaps, immature teams, and AI as a peripheral feature.
- Decision framework: complexity assessment, team capability audit, TCO calculation, strategic alignment, and a constrained pilot before commitment.
- Common pitfalls: exposing overly powerful tools, treating MCP as a security boundary by itself, skipping monitoring, and unrestricted production access.

## Relevance

Informs [model-agnostic architecture](/concepts/model-agnostic-architecture.md) and [AI sovereignty](/concepts/ai-sovereignty.md), and warns about [prompt injection](/concepts/prompt-injection.md) and [least privilege](/concepts/least-privilege.md) in agent tooling.

## Quality

Balanced technical analysis by Sarvani Yallapragada; concrete trade-offs and named incidents, but still vendor-adjacent.

## Entities Mentioned

- [Model Context Protocol](/entities/model-context-protocol.md) — the protocol assessed
- [Improving](/entities/improving.md) — author's employer
- [Sarvani Yallapragada](/entities/sarvani-yallapragada.md) — author

## Concepts Covered

- [model-agnostic architecture](/concepts/model-agnostic-architecture.md) — provider-neutral interface
- [AI sovereignty](/concepts/ai-sovereignty.md) — avoiding vendor lock-in
- [prompt injection](/concepts/prompt-injection.md) — misuse of powerful tools
- [least privilege](/concepts/least-privilege.md) — narrow tool scoping
- [agentic AI cost management](/concepts/ai-cost-management.md) — hidden operational costs
