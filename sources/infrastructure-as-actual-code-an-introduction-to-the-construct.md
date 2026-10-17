---
title: "Infrastructure as Actual Code: An Introduction to the Construct Programming Model"
type: "Source Summary"
description: "The Construct Programming Model defines infrastructure in real programming languages, enabling reusable, testable, governable patterns."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, cloud, improving.com]
sources:
  - "references/improving.com/infrastructure-as-actual-code-an-introduction-to-the-construct/infrastructure-as-actual-code-an-introduction-to-the-construct.md"
---

# Infrastructure as Actual Code: An Introduction to the Construct Programming Model — Summary

**Original source**: `references/improving.com/infrastructure-as-actual-code-an-introduction-to-the-construct/infrastructure-as-actual-code-an-introduction-to-the-construct.md`

## Summary

Will Wermager argues declarative IaC tools like Terraform and CloudFormation become unwieldy for large systems because they lack abstraction. He introduces the Construct Programming Model (CPM) — AWS CDK, CDKtf, CDK8s, and Projen — which defines infrastructure in imperative languages and offers three abstraction tiers (L1–L3), so teams can share, extend, and test reusable constructs.

## Key Claims

- Declarative IaC forces explicit definition of every resource, producing boilerplate and little abstraction.
- AWS CDK (open-sourced as TypeScript, with other-language bindings via JSII) spawned CDKtf, CDK8s, and Projen; the CPM suits anything configured via declarative language.
- Constructs come in three tiers: L1 maps 1:1 to a resource, L2 removes boilerplate and adds helpers (e.g. AWS CDK's grant), L3 packages whole architecture patterns.
- In the example project, roughly 20 lines of L3 code synthesize over 2000 lines of CloudFormation JSON.
- Internally curated constructs let application teams self-serve while meeting security requirements; non-standard use routes through infosec approval.
- Abstraction is no substitute for foundational cloud knowledge; test synthesized output with the provided unit-test utilities.
- Caveats: L2/L3 constructs lag L1 updates, and CDKtf is not yet GA with mostly L1 provider constructs.

## Relevance

A case for [infrastructure as code](/concepts/infrastructure-as-code.md) with reusable constructs that create [golden paths](/concepts/golden-path.md), while warning about [abstraction debt](/concepts/abstraction-debt.md).

## Quality

Experienced practitioner deep-dive by Will Wermager with a public example repo; detailed and candid about trade-offs, though biased toward CDK.

## Entities Mentioned

- [Terraform](/entities/terraform.md) — declarative IaC tool and target of CDKtf
- [HashiCorp](/entities/hashicorp.md) — maker of Terraform
- [AWS](/entities/aws.md) — provider behind the AWS CDK
- [Kubernetes](/entities/kubernetes.md) — target of CDK8s

## Concepts Covered

- [infrastructure as code](/concepts/infrastructure-as-code.md) — defining infrastructure in version-controlled code
- [golden path](/concepts/golden-path.md) — curated constructs as the supported route
- [abstraction debt](/concepts/abstraction-debt.md) — the risk of high-level abstractions hiding decisions
