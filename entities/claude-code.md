---
title: "Claude Code"
type: "Entity"
description: "Anthropic's agentic coding product, cited here for spend control, quality regressions, and the review bottleneck."
created: '2026-10-17'
updated: '2026-10-17'
tags: [coding-agent, tooling, anthropic]
sources:
  - "/sources/checking-the-math-on-the-500-million-ai-spend-story.md"
  - "/sources/eval-driven-development-the-discipline-agent-teams-are-missing.md"
  - "/sources/off-the-shelf-gets-you-partway-there.md"
  - "/sources/the-machine-is-learning-to-build-itself-you-still-have-to-decide-what-to-build.md"
  - "/sources/the-model-didnt-change-the-default-did.md"
  - "/sources/the-model-stays-home-the-patch-ships.md"
  - "/sources/the-scaffolding-just-got-a-learning-rate.md"
  - "/sources/writing-code-vs-shipping-code-the-maturity-gap.md"
  - "/sources/the-audit-nobody-wanted.md"
---

# Claude Code

Claude Code is Anthropic's agentic coding product. It is cited across this corpus for spend-control math, a silent default-driven quality regression, plugin-marketplace sprawl, and the review bottleneck that caps its throughput gains.

## Key Claims

- A 34-day quality regression came from a changed default reasoning effort — high to medium on March 4 — not from the model; the API was never touched.
- A versioned production eval suite would have caught the drop on day one.
- Over 2,500 Claude Code plugin marketplaces exist with no trust authority, so discovery lacks verification, versioning, and ownership.
- Hitting a viral $500M monthly bill would require 2 to 3.3 million developer seats, but the underlying token-cost anxiety is real.
- Teams pairing tooling with Stage 4 workflow redesign ship 12-30% more features, crossing 50% with governance.
- Microsoft canceled most of its internal Claude Code licenses, an example of post-hoc spend discipline once invoices did not match business cases.
- Uber burned its annual AI coding budget in four months; use cases with measurable output, like code, are the ones that survive scrutiny.

## Related

- [Claude](/entities/claude.md) — the model family it runs on
- [Anthropic](/entities/anthropic.md) — its vendor
- [Version Pinning](/concepts/version-pinning.md) — the lesson of the changed default
- [evals-as-code](/concepts/evals-as-code.md) — how the regression would have been caught
- [Skill Discovery](/concepts/skill-discovery.md) — the marketplace problem
- [token cost](/concepts/token-cost.md) — the spend anxiety behind the license cuts
- [The Model Didn't Change. The Default Did.](/sources/the-model-didnt-change-the-default-did.md) — primary source
