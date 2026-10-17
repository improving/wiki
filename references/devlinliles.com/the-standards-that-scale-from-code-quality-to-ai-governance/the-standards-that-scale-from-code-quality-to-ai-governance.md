---
type: Reference
title: "The Standards That Scale: From Code Quality to AI Governance"
resource: "https://www.devlinliles.com/the-standards-that-scale-from-code-quality-to-ai-governance/"
author: "Devlin Liles"
published: '2026-07-13'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

In 2013 I stood in a conference room and argued that a software craftsman should be willing to say no to people who can fire them when those people ask them to ship code that doesn't meet professional standards.

In 2026 I make a nearly identical argument about AI governance: that organizations willing to say no to the temptation of deploying autonomous agents without governance infrastructure are the ones that will build trustworthy AI systems.

The argument is the same argument. The scale is different.

## The Craftsman's Foundation

The 2013 version of the argument had three components:

**Non-negotiable quality standards.** A minimum level of quality is acceptable; below that minimum, the answer is no. Not "let's discuss what we can compromise on" — no. The standard exists because cutting below it costs more than it saves. The developer who ships untested code to meet a deadline has transferred the cost of the testing (low, now) to the cost of the production incident (high, later) — and added the reputational cost of having shipped something they knew was wrong.

**Technical debt as chronic behavior.** The problem is not one decision to skip tests. It is the pattern of making that decision repeatedly until the pattern becomes the policy. Professional standards exist to interrupt the normalization of the shortcut.

**Automation as obligation.** Deploy early, deploy often, use robots to deploy while you sleep. Automation is not a convenience for developers with spare time — it is the mechanism by which quality standards can be enforced consistently rather than depending on individual heroics.

These three components — non-negotiable standards, debt prevention through behavior, and systematic automation — are the precursors to everything that comes later.

## The Governance Parallel

The 2026 version has the same structure:

**Non-negotiable governance standards.** Deploying autonomous agents without audit trails, boundary enforcement, quality gates, and human approval points is the AI equivalent of shipping without tests. You are transferring a low cost now (building the infrastructure) to a high cost later (the production failure that damages organizational confidence in autonomous AI). The governance minimum is not optional.

**Governance debt as chronic behavior.** Organizations do not skip governance infrastructure in one dramatic decision. They skip it incrementally: "we'll add audit trails once the system is more stable." "We'll define boundary enforcement for the production system." "The quality gates will come in the next iteration." Each decision is individually defensible. The pattern is an operating system with no safety infrastructure, deployed into production.

**Automation as governance.** The governance infrastructure for AI is not people reviewing AI outputs manually at scale — that eliminates the value of autonomy. It is automated quality gates that check output against defined criteria, programmatic boundary enforcement that constrains what agents can do, automated audit logging that captures decisions without human intervention. The governance is in the system, not in the people watching the system.

## The Through-Line

What connects the 2013 craftsman's argument to the 2026 governance argument is the underlying principle: **quality is not a phase you add at the end. It is the structure within which capable work happens.**

The developer who writes tests as they code is building the feedback loop that makes their coding reliable, not doing "extra work." The organization that builds governance infrastructure before deploying autonomous agents is building the operating environment within which autonomous capability is trustworthy, not adding overhead.

The craftsman who holds to professional standards under pressure is the same person who builds governance infrastructure before it is demanded. The professional obligation does not change when the scale changes. The minimum of what we owe to the people who use what we build is encoded in the standards we hold.

Non-negotiable in 2013. Non-negotiable in 2026.

---

*Part of the *[*Thought Leadership series*](https://www.devlinliles.com/tag/thought-leadership/)* — Overlap: Thread 1 × Thread 3.*
