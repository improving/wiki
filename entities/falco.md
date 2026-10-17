---
title: "Falco"
type: "Entity"
description: "Open-source Kubernetes runtime security tool used for threat detection and audit visibility on agent workloads."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, kubernetes, observability]
sources:
  - "/sources/kubernetes-prompt-injection.md"
  - "/sources/platform-security-governance-ai-agents.md"
---

# Falco

Falco is a runtime security and threat-detection tool for Kubernetes that appears in this corpus as one of the structural guardrails for containing AI agents wired into clusters. Where admission control and least-privilege RBAC block disallowed actions before they run, Falco watches what workloads actually do and preserves evidence of suspicious behavior for audit.

## Role in Agent Containment

- In the corpus's prompt-injection defense model, Falco supplies the runtime-detection layer alongside least-privilege RBAC (scoped with `resourceNames`) and a Kyverno admission policy.
- Its contribution is audit visibility — detecting and alerting on behavior rather than blocking it — which complements the preventive layers.
- The argument behind it is that scanning prompts cannot be a primary defense, so detection tools earn their place mainly by recording what happened regardless of the instructions an agent followed.
- It fits the broader platform-security thesis that agents are a new class of privileged operator needing identity, policy, and decision attribution.

## Related

- [Kyverno](/entities/kyverno.md) — admission-control policy layer used beside Falco
- [Kubernetes](/entities/kubernetes.md) — the environment Falco watches
- [runtime policy enforcement](/concepts/runtime-policy-enforcement.md) — stopping disallowed actions before they execute
- [audit trail](/concepts/audit-trail.md) — the record that makes autonomy accountable
