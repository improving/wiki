---
title: "Prompt Injection"
type: "Concept"
description: "Instruction-shaped text in a model's context executed as an operator command — a use/mention confusion contained, not fixed."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, agents, llm]
sources:
  - "/sources/agent-containment-is-losing-the-race-to-capability.md"
  - "/sources/prompt-injection-is-a-use-mention-confusion-the-architecture-has-no-fix.md"
  - "/sources/skill-sprawl-is-the-shared-drive-again.md"
  - "/sources/the-handbook-is-in-the-context-the-compliance-isnt.md"
---

# Prompt Injection

Prompt injection is the class of attack in which instruction-shaped text in a model's context is executed as though it were the operator's instruction. Across this corpus it is framed as a use/mention confusion the architecture cannot fix: defenses reduce but never eliminate success, so the actionable response is architectural containment rather than prevention.

## Key Claims

- Prompt injection is the top LLM vulnerability, ranked OWASP LLM01:2025; models cannot distinguish instruction-shaped text from instructions to follow.
- Three July 2026 incidents — GitLost, Kiro, and the OpenAI–Hugging Face breach — bypassed prompts entirely, failing at the action layer where tool calls execute.
- Orchestration patterns are a stronger attack surface than prompt wording; sandboxes, proxies, approval prompts, and scopes each had unchecked gaps.
- HANDBOOK.md showed frontier agents fail long-context policy compliance: the best configuration, Claude Fable 5, passed only 36.2% of trials, so rules must be enforced outside the model.
- Raising reasoning effort did not fix compliance and made one model worse; a standing document acts as one more retrieved source whose influence decays.
- Unmanaged skill libraries amplify exposure: SkillsMP indexes roughly 1.9 million public skills averaging 6.2/12 on quality, and a Snyk audit found prompt injection in 36% of skills.

## Related

- [OWASP](/entities/owasp.md) — the body that ranks injection as LLM01
- [sandbox escape](/concepts/sandbox-escape.md) — the containment failure at the action layer
- [boundary enforcement](/concepts/boundary-enforcement.md) — architectural containment for injection
- [Least privilege](/concepts/least-privilege.md) — limiting what a hijacked agent can reach
- [Tool Calling](/concepts/tool-calling.md) — the layer where injection becomes action
- [Prompt Injection Is a Use/Mention Confusion](/sources/prompt-injection-is-a-use-mention-confusion-the-architecture-has-no-fix.md) — primary source
