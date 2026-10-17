---
title: "OWASP"
type: "Entity"
description: "Security body whose LLM Top 10 ranks prompt injection as the top risk, anchoring the corpus's containment argument."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, standards, llm]
sources:
  - "/sources/prompt-injection-is-a-use-mention-confusion-the-architecture-has-no-fix.md"
  - "/sources/your-agents-are-principals-treat-them-like-it.md"
---

# OWASP

OWASP is the security body whose LLM Top 10 the corpus leans on to establish prompt injection as the field's top vulnerability. Its ranking (LLM01:2025) is the factual anchor for a deeper architectural claim: the flaw cannot be fixed, only contained.

## Overview

The prompt-injection post argues the vulnerability is a use/mention confusion — models cannot distinguish instruction-shaped text from instructions to follow. Defenses reduce but do not eliminate injection success, so architectural containment, not prevention, is the actionable frame.

The agents-as-principals post connects the ranking to identity: indirect prompt injection is OWASP's top LLM risk, with real CVEs behind it. Because agents are injectable, the perimeter must be permissions rather than the model, and blast radius must be bounded by scoping. OWASP's ranking is used less as a checklist than as evidence that the problem is structural.

## Key Claims

- Prompt injection is the top LLM vulnerability, ranked OWASP LLM01:2025.
- Models cannot distinguish instruction-shaped text from instructions to follow.
- Defenses reduce but do not eliminate injection success.
- Architectural containment, not prevention, is the actionable frame.
- Indirect prompt injection is OWASP's top LLM risk, with real CVEs.

## Related

- [Prompt injection](/concepts/prompt-injection.md) — the risk OWASP ranks first
- [agent identity](/concepts/agent-identity.md) — the perimeter the ranking implies
- [Least privilege](/concepts/least-privilege.md) — the containment discipline
- [AI Governance](/concepts/ai-governance.md) — the program that responds
- [Prompt Injection Is a Use/Mention Confusion](/sources/prompt-injection-is-a-use-mention-confusion-the-architecture-has-no-fix.md) — primary source
