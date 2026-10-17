---
title: "MCP Went Stateless. The State Didn't Go Anywhere."
type: "Source Summary"
description: "MCP's 2026-07-28 spec drops the session handshake for stateless, round-robin-friendly servers — but application state and its ownership remain."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/mcp-went-stateless-the-state-didnt-go-anywhere/mcp-went-stateless-the-state-didnt-go-anywhere.md"
---

# MCP Went Stateless. The State Didn't Go Anywhere. — Summary

**Original source**: `references/devlinliles.com/mcp-went-stateless-the-state-didnt-go-anywhere/mcp-went-stateless-the-state-didnt-go-anywhere.md`

## Summary

The Model Context Protocol's fifth release, the 2026-07-28 spec, removes the `initialize`/`initialized` handshake and the `Mcp-Session-Id` header, so any request can land on any server instance behind a plain round-robin load balancer. That unblocks Azure Functions' consumption plan and Container Apps' scale-to-zero tier, which sticky routing had worked against. But the author stresses a stateless protocol is not the same as a stateless application: state now moves into explicit handles the model passes back as arguments, and someone must still decide what a handle points to and how long it lives. Authorization also aligns with enterprise OAuth — RFC 9207 issuer validation, and Client ID Metadata Documents replacing Dynamic Client Registration — fitting Entra-governed tenants.

## Key Claims

- MCP crossed 400 million monthly SDK downloads in July, four times the start-of-year rate.
- The 2026-07-28 spec collapses three round trips into one self-describing request with no shared session store.
- Removing session affinity unblocks serverless and scale-to-zero hosting on Azure.
- Stateless protocol ≠ stateless application; state moves to explicit handles passed as arguments.
- RFC 9207 issuer validation and CIMD (replacing DCR over twelve months) align MCP authorization with Entra-style governance, while Roots, Sampling, Logging, and legacy HTTP+SSE get a twelve-month support window.

## Relevance

Informs agentic-delivery integration around the [Model Context Protocol](/entities/model-context-protocol.md), [Anthropic](/entities/anthropic.md)'s spec, and enterprise identity in [Entra ID](/entities/entra-id.md).

## Quality

Practitioner blog post by Devlin Liles. Strengths: precise spec details tied to real Azure deployment economics. Caveats: relies on vendor blog posts and Microsoft docs; the 400 million download figure appears only in a chart.

## Entities Mentioned

- [Model Context Protocol](/entities/model-context-protocol.md) — the protocol whose spec changed
- [Anthropic](/entities/anthropic.md) — spec author and steward
- [Entra ID](/entities/entra-id.md) — the enterprise identity system the authorization changes align with

## Concepts Covered

- None.

## Related Sources

- [The Box That Already Shipped - Rollback by Reversibility Type](/sources/the-box-that-already-shipped-rollback-by-reversibility-type.md)
