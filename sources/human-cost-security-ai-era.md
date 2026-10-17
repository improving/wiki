---
title: "The Human Cost of Security in the AI Era"
type: "Source Summary"
description: "AI-driven attacks are outrunning human triage, so point a local LLM at CVE triage instead — and raise better issues."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, ai, improving.com]
sources:
  - "references/improving.com/human-cost-security-ai-era/human-cost-security-ai-era.md"
---

# The Human Cost of Security in the AI Era — Summary

**Original source**: `references/improving.com/human-cost-security-ai-era/human-cost-security-ai-era.md`

## Summary

Sonali Srivastava argues that AI-enabled attacks are multiplying faster than humans can triage them, and that the real cost lands on the people who must validate every low-effort issue, CVE, or alert. She then shows how to turn the same AI around: a scoped local LLM that reasons through one CVE at a time against a project's actual dependency manifests and source code.

## Key Claims

- AI-enabled adversaries increased attacks 89% year-over-year, with software supply chain security among the hardest-hit areas.
- The 2026 TeamPCP compromise of Aqua Security's Trivy scanner (CVE-2026-33634, CVSS 9.4) used stolen CI/CD credentials; 19 days after remediation, 76 version tags were force-pushed, and exposure reached 2,500+ organizations including AWS, Samsung, and Cisco.
- Low-effort issue reports shift the entire "doing" half onto whoever picks them up, wasting maintainer hours and eroding trust on both sides.
- Local models suit CVE triage for data sovereignty, offline resilience during incident response, no cross-customer exposure, fewer credentials to defend, and predictable economics.
- The demo tool (Python 3.8+, Ollama, qwen3.5) reads a CVE record, dependency manifests, and source code, using a structured six-step reasoning scaffold that can return "NOT AFFECTED" even when a scanner already filed a report.
- Practical tips: keep the reasoning scaffold specific, feed only relevant files per step, and lean on the model for classification and pattern matching rather than open-ended analysis.

## Relevance

Sits at the intersection of [software supply chain security](/concepts/software-supply-chain-security.md) and a narrow [agentic AI](/concepts/agentic-ai.md) use aimed at [application security](/concepts/application-security.md) triage. Local inference serves [data sovereignty](/concepts/data-sovereignty.md), and the triage burden is a form of [alert fatigue](/concepts/alert-fatigue.md).

## Quality

Practitioner talk write-up by Sonali Srivastava (KubeCon India 2026 keynote); concrete with a working repo, but the local-model recommendation is argued rather than benchmarked.

## Entities Mentioned

- [Ollama](/entities/ollama.md) — local model runtime used for triage
- [Kubernetes](/entities/kubernetes.md) — the project used in the demo
- [LiteLLM](/entities/litellm.md) — named among the downstream supply chain victims
- [KubeCon](/entities/kubecon.md) — venue of the original keynote
- [AWS](/entities/aws.md) — named in the exposure list
- [Samsung](/entities/samsung.md) — named in the exposure list

## Concepts Covered

- [software supply chain security](/concepts/software-supply-chain-security.md) — the main topic
- [agentic AI](/concepts/agentic-ai.md) — scoped triage agent
- [application security](/concepts/application-security.md) — vulnerability handling
- [data sovereignty](/concepts/data-sovereignty.md) — why local models
- [alert fatigue](/concepts/alert-fatigue.md) — the triage overload
