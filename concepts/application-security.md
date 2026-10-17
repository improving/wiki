---
title: "application security"
type: "Concept"
description: "Finding and fixing vulnerabilities in applications across the development lifecycle, now including LLM-specific risks."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, delivery, ai]
sources:
  - "/sources/how-generative-ai-is-revolutionizing-application-security.md"
  - "/sources/owasp-top-10-llm-security-guide.md"
  - "/sources/kubernetes-prompt-injection.md"
  - "/sources/human-cost-security-ai-era.md"
  - "/sources/security-the-thing-that-everyone-loves-to-hate.md"
  - "/sources/a-security-model-for-developers.md"
---

# application security

Application security is the practice of finding and fixing vulnerabilities in software across the whole development lifecycle, from the code a developer writes to the live system it runs in. As AI accelerates code generation, the corpus argues the discipline must keep pace — manual review and SAST/DAST alone struggle with scale and context — and it now must cover LLM-specific risks such as prompt injection and excessive agency.

## Key Claims

- AI is shifting AppSec from detection toward context-aware remediation: inline IDE and CI feedback, autofixing, false-positive reduction, and plain-language guidance from tools such as Snyk DeepCode AI Fix, Qwiet AI AutoFix, and GitHub Copilot AutoFix.
- Reported gains are large but vendor-sourced: Snyk claims up to 20% better accuracy with fewer false positives, Qwiet AI reports up to 95% faster fixes, and CodeRabbit up to 50% less manual review time — against a ~20% fix failure rate and system-level context gaps.
- The OWASP Top 10 for LLM Applications (2025) ranks prompt injection first and adds sensitive information disclosure, supply chain, data/model poisoning, improper output handling, excessive agency, system prompt leakage, vector weaknesses, misinformation, and unbounded consumption.
- In cloud-native environments, the durable mitigation is structural rather than detection: least-privilege RBAC scoped with `resourceNames`, Kyverno admission policy, NetworkPolicy egress containment, and Falco runtime detection decide the outcome regardless of the instructions an agent follows.
- Human triage is the real bottleneck: 50% of organizations carry critical security debt (high-severity issues open over a year), so scoped local LLMs are used to reason through one CVE at a time against real manifests and source.
- A developer-facing model chains Policy → Standard → Principle → Guideline → Requirements → User Story → Test Case, so that a policy such as "user data cannot be public" becomes a testable TLS requirement.

## Related

- [shift-left security](/concepts/shift-left-security.md) — moving these checks earlier in delivery
- [software supply chain security](/concepts/software-supply-chain-security.md) — dependencies and artifacts as attack surface
- [prompt injection](/concepts/prompt-injection.md) — the top LLM risk
- [least-privilege](/concepts/least-privilege.md) — scoping what agents and services may do
- [OWASP](/entities/owasp.md) — publisher of the LLM Top 10
