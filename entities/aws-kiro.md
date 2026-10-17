---
title: "AWS Kiro"
type: "Entity"
description: "AWS agentic coding tool cited in posts on agent containment failures and spec-driven development."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agent, aws, coding-tool, security]
sources:
  - "/sources/agent-containment-is-losing-the-race-to-capability.md"
  - "/sources/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it.md"
---

# AWS Kiro

AWS Kiro is an agentic coding tool that appears in this corpus both as a July 2026 containment incident and as a context for spec-driven development. The posts use it to argue that agent security fails at the action layer — where tool calls execute — rather than at the system prompt.

## Overview

- One post lists GitLost, Kiro, and the OpenAI-Hugging Face breach as incidents that bypassed prompts entirely.
- It argues orchestration patterns are a stronger attack surface than prompt wording, and that sandboxes, proxies, approval prompts, and scopes each had unchecked gaps.
- The companion post frames spec-driven development for agents as separating prompt, spec, and tests, while noting hard limits such as distribution shift and constraint decay.

## Key Claims

- Containment is losing the race to capability at the action layer.
- One artifact doing spec, documentation, and tests does none of them well.
- Distribution shift can drop accuracy up to 54% with no spec change.
- MCP is an under-specified tool contract, with 99 CVEs in 2025.

## Related

- [sandbox escape](/concepts/sandbox-escape.md) — the incident class Kiro exemplifies
- [Boundary enforcement](/concepts/boundary-enforcement.md) — the failing control
- [Tool Calling](/concepts/tool-calling.md) — the layer where enforcement must sit
- [Model Context Protocol](/entities/model-context-protocol.md) — the tool contract referenced
- [Agent Containment Is Losing the Race to Capability](/sources/agent-containment-is-losing-the-race-to-capability.md) — primary source
- [Spec-Driven Development for AI](/sources/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it.md) — companion source
