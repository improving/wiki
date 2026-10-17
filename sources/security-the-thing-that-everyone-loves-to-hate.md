---
title: "Security: The Thing That Everyone Loves to Hate"
type: "Source Summary"
description: "Argues cloud-native security must be everyone's responsibility, mapping the developer, security, PM, platform, and leadership lenses and the culture that connects them."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, culture, improving.com]
sources:
  - "references/improving.com/security-the-thing-that-everyone-loves-to-hate/security-the-thing-that-everyone-loves-to-hate.md"
---

# Security: The Thing That Everyone Loves to Hate — Summary

**Original source**: `references/improving.com/security-the-thing-that-everyone-loves-to-hate/security-the-thing-that-everyone-loves-to-hate.md`

## Summary

Sonali Srivastava argues that cloud-native security fails because it is treated as someone else's problem, pushed to "later" until an incident forces crisis mode. Drawing on a KubeCon + CloudNativeCon India 2025 panel, she maps how security looks through five lenses — developers, security engineers, product managers, platform engineers, and leadership — and argues the real fix is cultural: making security a shared responsibility baked in from day one rather than a compliance checkbox bolted on at the end.

## Key Claims

- Incidents like Log4j drove a 34% increase in vulnerability exploitation between 2020 and 2021.
- 50% of organizations now carry critical security debt — high-severity issues open for more than a year, per ITPO.
- The average fix time for security flaws rose 47% in five years, from 171 to 252 days.
- Emerging threats include QR phishing (quishing), prompt injection against LLM applications, jailbreaks, dependency confusion, and configuration drift exploits.
- Developers should simplify the stack, use simple base images, integrate SBOMs early, and enforce security at the PR stage.
- Security engineers should treat governance as discipline, build resilience through prevention, and establish non-negotiable security gates.
- Product managers should reframe security as a product feature, distinguish vulnerabilities from misconfigurations, and use tools like VEX and Kyverno.
- Platform engineers should enforce security through automation, maintain least-privilege access, manage configuration drift, and build observability into security.
- Leadership should allocate sprint capacity to security, tie it to customer trust, celebrate proactive security, and foster psychological safety.
- A security-first culture requires education, normalized ownership, blame-free feedback loops, visible metrics, and adaptability.

## Relevance

A culture-centered case for [security culture](/concepts/security-culture.md) and [shift-left security](/concepts/shift-left-security.md), tying [software supply chain security](/concepts/software-supply-chain-security.md) and [policy as code](/concepts/policy-as-code.md) to everyday practice.

## Quality

Practitioner panel write-up by Sonali Srivastava; broad and role-specific, though vendor-adjacent and reliant on third-party statistics.

## Entities Mentioned

- [Improving](/entities/improving.md) — author's firm
- [Kyverno](/entities/kyverno.md) — policy engine for misconfigurations
- [GDPR](/entities/gdpr.md) — cited compliance guardrail
- [KubeCon](/entities/kubecon.md) — venue for the panel

## Concepts Covered

- [security culture](/concepts/security-culture.md) — security as everyone's responsibility
- [shift-left security](/concepts/shift-left-security.md) — checks earlier in the lifecycle
- [software supply chain security](/concepts/software-supply-chain-security.md) — dependencies, SBOMs, dependency confusion
- [application security](/concepts/application-security.md) — prompt injection and jailbreaks
- [secrets management](/concepts/secrets-management.md) — credential handling and least privilege
- [policy as code](/concepts/policy-as-code.md) — Kyverno-style automated gates
- [least privilege](/concepts/least-privilege.md) — auditing and rotating access
