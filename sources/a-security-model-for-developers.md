---
title: "A Security Model for Developers"
type: "Source Summary"
description: "Offers developers a mental model linking company policy, security principles, standards, and guidelines into testable user stories."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, improving.com]
sources:
  - "references/improving.com/a-security-model-for-developers/a-security-model-for-developers.md"
---

# A Security Model for Developers — Summary

**Original source**: `references/improving.com/a-security-model-for-developers/a-security-model-for-developers.md`

## Summary

Security is usually explained from the pen-tester's perspective, which leaves developers overwhelmed by acronyms. This guide gives developers a mental model that chains company policy to security principles, standards, and technology-specific guidelines, ending in requirements and user stories that are easy to test.

## Key Claims

- The model defines Policy (organizational directives), Principle (universal secure-design ideas like least privilege), Standard (specific techniques like OAuth2), and Guideline (technology-specific implementation help).
- The chain runs Policy → Standard → Principle → Guideline → Requirements → User Story → Test Case.
- Example: a policy that user data cannot be public leads to the TLS standard, then a Confluent Cloud guideline, then a story enabling TLS for client-broker and broker-broker communication.
- Reverse example: "Implement authorization" becomes SASL authentication plus Kafka/Zookeeper ACLs by applying least-privilege and attack-surface principles.
- If a manager mandates the internal RBAC system, that is simply a different Standard to satisfy with the same Kafka guideline.
- The definitions are deliberately working definitions; the terms overlap in other contexts.

## Relevance

Informs [application security](/concepts/application-security.md), [shift-left security](/concepts/shift-left-security.md), and [zero trust security](/concepts/zero-trust-security.md).

## Quality

Clear practitioner framework by Mark Soule, inspired by Brian Glas; practical, though its definitions are deliberately simplified.

## Entities Mentioned

- [Confluent](/entities/confluent.md) — supports TLS out of the box in the example
- [Apache Kafka](/entities/apache-kafka.md) — the messaging system in the examples

## Concepts Covered

- [application security](/concepts/application-security.md) — finding and fixing vulnerabilities across delivery
- [shift-left security](/concepts/shift-left-security.md) — moving checks earlier in the lifecycle
- [zero trust security](/concepts/zero-trust-security.md) — assuming the network is compromised
