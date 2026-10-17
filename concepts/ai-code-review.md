---
title: "AI code review"
type: "Concept"
description: "Automated review that catches patterns but lacks architectural context, leaving judgment to humans."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, engineering, testing]
sources:
  - "/sources/ai-code-review.md"
  - "/sources/embedding-ai-into-daily-development.md"
  - "/sources/how-generative-ai-is-revolutionizing-application-security.md"
  - "/sources/software-supply-chain-security-package-age-enforcement.md"
---

# AI code review

AI code review automates pattern matching, security scanning, and style enforcement, but it lacks the architectural, historical, runtime, and business context that human review supplies. The sources warn that teams approving pull requests because the AI stayed silent are trading detection for understanding, and that better review comes from expanding context — ADRs, incident reports, dependency maps — rather than trusting the model more.

## Key Claims

- AI reliably catches anti-patterns, unused variables, null-reference risks, hardcoded secrets, and SQL injection/XSS, and enforces style consistently without fatigue.
- It cannot judge architectural intent, why workarounds exist, hidden cross-service dependencies, production behavior under load, or domain correctness.
- False confidence is the top risk: teams approve pull requests because the AI stayed silent, not because the change is safe.
- A study of 54,791 AI review comments found the two most common reasons developers ignored feedback were incorrect suggestions and intentional design decisions.
- GitHub reports Copilot code review surfaces actionable feedback in 71% of reviews and says nothing in 29%, and is working to reduce low-value comments ("silence is better than noise").
- AI security tooling shifts AppSec from detection toward context-aware remediation — tools like Snyk DeepCode AI Fix and Qwiet AI AutoFix — but a roughly 20% fix failure rate remains.
- AI assistants also expand dependency suggestions with no freshness context, so install-time controls such as a 7-day minimum package age apply regardless of whether a human or an agent requested the package.
- Better reviewers need expanded context, ecosystem integration via MCP with read-only scoping, change-impact analysis, and review that triggers targeted tests and scans.

## Related

- [Review Bottleneck](/concepts/review-bottleneck.md) — verification gating throughput
- [verification tax](/concepts/verification-tax.md) — effort spent checking AI output
- [Context Management](/concepts/context-management.md) — the missing ingredient in review
- [Tacit Knowledge](/concepts/tacit-knowledge.md) — historical context AI lacks
- [Model Context Protocol](/entities/model-context-protocol.md) — protocol for live ecosystem access
- [GitHub Copilot](/entities/github-copilot.md) — cited for review coverage statistics
