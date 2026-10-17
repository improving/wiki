---
title: "Prompt Injection Is a Use/Mention Confusion. The Architecture Has No Fix."
type: "Source Summary"
description: "Prompt injection is an architectural use/mention confusion in LLMs; the fix is containment, not prevention."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, devlinliles.com]
sources:
  - "references/devlinliles.com/prompt-injection-is-a-use-mention-confusion-the-architecture-has-no-fix/prompt-injection-is-a-use-mention-confusion-the-architecture-has-no-fix.md"
---

# Prompt Injection Is a Use/Mention Confusion. The Architecture Has No Fix. — Summary

**Original source**: `references/devlinliles.com/prompt-injection-is-a-use-mention-confusion-the-architecture-has-no-fix/prompt-injection-is-a-use-mention-confusion-the-architecture-has-no-fix.md`

## Summary

The post argues prompt injection is a consequence of how language models process language, not an implementation bug. Borrowing the analytic-philosophy distinction between using a word and mentioning it, it contends models cannot tell an instruction they should follow from an instruction they should merely summarize — instruction-shaped text in context activates instruction-following patterns. Because the vulnerability is a shadow of the instruction-following feature, the actionable response is architectural containment rather than injection prevention.

## Key Claims

- OWASP ranks prompt injection LLM01:2025, the top AI application vulnerability; the UK's NCSC says it "may be a problem that is never fully fixed."
- Documented attack success rates run 50–84% on undefended models, exceeding 85% with adaptive techniques; one compiled dataset holds 461,000+ attempts.
- Indirect injection — instructions embedded in retrieved documents — succeeds at 68–71% even against models with instruction-following constraints.
- Sandbox isolation reduces exploitation most reliably by bounding what an injected instruction can do; instruction hierarchy and input sanitization help only at the margins.
- The recommended design separates retrieval from action, scopes tool permissions to the minimum, adds confirmation for consequential actions, and red-teams for injection before deployment.

## Relevance

Central to [prompt injection](/concepts/prompt-injection.md) and the risk framing in [OWASP](/entities/owasp.md)'s LLM Top 10.

## Quality

Practitioner blog post by Devlin Liles. Strengths: concrete, sourced figures and a clear architectural argument. Caveat: it synthesizes others' research and leans on the philosophical analogy rather than presenting original measurements.

## Entities Mentioned

- [OWASP](/entities/owasp.md) — ranks prompt injection as LLM01:2025

## Concepts Covered

- [Prompt injection](/concepts/prompt-injection.md) — main topic; reframed as a use/mention confusion
