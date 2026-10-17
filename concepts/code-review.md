---
title: "code review"
type: "Concept"
description: "Peer inspection of changes that spreads knowledge and catches defects early, a bottleneck as AI speeds generation."
created: '2026-10-17'
updated: '2026-10-17'
tags: [engineering, delivery, quality]
sources:
  - "/sources/drop-everything-and-review.md"
  - "/sources/ai-code-review.md"
  - "/sources/the-corrections-are-the-leak.md"
  - "/sources/how-generative-ai-is-revolutionizing-application-security.md"
---

# code review

Code review is peer inspection of a change before it merges, catching defects early and spreading knowledge of the codebase across the team. The corpus frames it as a distinct "middle loop" of software development — the first time multiple stakeholders see the same new code — and warns that as AI accelerates code generation, review becomes the bottleneck that governs how much of that speed reaches production.

## Key Claims

- Review sits between the fast single-developer inner loop (code-build-test) and the slow outer loop (deployment, acceptance and performance tests, minutes to days); async review unnecessarily inflates this middle loop.
- Review is thankless and crowds diffuse responsibility, so reviewers delay and assume others will cover the work; the "Drop Everything and Review" (DEAR) norm makes reviewing code the first task after production incidents.
- AI code review is good at pattern matching, security scanning, style enforcement, and fast feedback, but cannot judge architectural intent, historical context, cross-repository dependencies, runtime behavior, or business rules.
- False confidence is the top risk: teams approve pull requests because the AI stayed silent rather than because the change is safe, and a study of 54,791 AI review comments found the top reasons for ignoring feedback were incorrect suggestions and intentional design decisions.
- GitHub reports Copilot code review surfaces actionable feedback in 71% of reviews and says nothing in 29%, working toward "silence is better than noise."
- Every correction a reviewer makes — in a proposal, a code review, or a client project — is a lesson recorded somewhere, so the eval-and-correction layer is arguably the real moat, and its ownership needs scrutiny.

## Related

- [AI code review](/concepts/ai-code-review.md) — automated review and its context limits
- [review bottleneck](/concepts/review-bottleneck.md) — verification gating throughput
- [verification tax](/concepts/verification-tax.md) — effort spent checking output
- [developer experience](/concepts/developer-experience.md) — flow and blocking
- [software craftsmanship](/concepts/software-craftsmanship.md) — the standards review upholds
- [Andrew Watson](/entities/andrew-watson.md) — names the review "middle loop" and the DEAR norm
