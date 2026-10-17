---
type: Reference
title: "Which Failure Mode Can You Afford? The Security Personality of Your Model"
resource: "https://www.devlinliles.com/which-failure-mode-can-you-afford-the-security-personality-of-your-model/"
author: "Devlin Liles"
published: '2026-07-23'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every conversation about model selection eventually arrives at the same question: which model is better? The answer most people expect is a leaderboard ranking: here are the top five, use number one, done.

The Sonar leaderboard study of 4,000+ Java tasks produced something more useful and more inconvenient than a ranking. It produced profiles. Every major frontier model has a distinct pattern of where and how it fails, and those patterns do not track the overall capability scores in any predictable way. The model with the best security posture has the worst concurrency reliability. The model with the highest functional pass rate generates the most code by volume, which creates its own category of risk. The frontier models within four points of each other on SWE-bench Verified span a 12x range in security-critical defect density.

The right question is not which model is better. It is which failure mode your compliance environment can absorb.

## What the Sonar data actually shows

Sonar instrumented 4,000+ Java coding tasks across major frontier models, measuring blocker vulnerabilities, concurrency errors, resource leaks, code smells, and total lines of code generated per task.

GPT-5.2 High generated the best security posture by one measure: 16 blocker vulnerabilities per million lines of code, lowest in the study. It also produced the worst concurrency error rate: 470 per million lines of code, roughly seven times Gemini 3.1 Pro's 69. A system using GPT-5.2 High is choosing low vulnerability density and accepting a severe concurrency risk. Whether that trade makes sense depends entirely on what the system does.

Claude Opus 4.5 Thinking sits at 44 blocker vulnerabilities per million lines of code, well below Claude Sonnet 4.5's 198, and in reasoning mode it achieved the highest functional pass rate in the study at 83.6%. The reasoning mode comes with a volume cost: Opus 4.5 Thinking generated the most code by far. More generated code means more surface area for all categories of defects, even if the per-line density is lower.

Gemini 3.1 Pro landed in the middle on vulnerability density (72 per MLOC) with the best concurrency reliability in the study. For systems where threading correctness is the priority risk, that profile is more valuable than a lower vulnerability number paired with worse concurrency behavior.

The benchmark scores don't predict any of this. If you are using a leaderboard to make compliance-relevant model selection decisions, you are using the wrong instrument.

## Why compliance requirements make this concrete

SOC 2 Type II requires that systems handling in-scope data maintain controls over security and availability. A model generating code with high blocker vulnerability density is generating code that will, at some rate, produce systems with real vulnerabilities. The vulnerability density is a measurable input to your control environment. An organization that selects a model based on benchmark score and then finds security defects at a higher-than-expected rate in production code has a gap between its model selection process and its security controls. That gap is auditable.

The EU AI Act's Annex III obligations add a second dimension. High-risk AI systems require documentation of model selection rationale and evidence that the model's behavior remains within expected parameters. Choosing a model based on a benchmark leaderboard is a thin basis for that documentation. A selection decision based on task-specific evaluation data, including security defect density on representative tasks, is a much stronger one.

## How to approach model selection

Run your candidate model set against your actual task distribution before committing to a production deployment. Instrument specifically for the failure modes your compliance environment specifies. For a system handling financial data under SOC 2, measure security defect density and data handling correctness. For a system with high concurrency requirements, instrument threading behavior specifically. For a system where output volume creates downstream review costs, measure generated line counts alongside task completion rates.

The evaluation output is a profile match, not a ranking. The question is whether this model's failure pattern fits what this environment can catch. A high vulnerability density model works fine behind a mature static analysis pipeline; the pipeline catches what the model generates before it reaches production. Pull that pipeline away and the same model is a liability.

## The gap that static analysis doesn't cover

Sonar measured static defect categories. The harder category is semantic correctness: does the code do what the requirement says, in a way a human maintainer would accept?

METR's March 2026 PR study addressed that directly. Maintainers reviewed 296 AI-generated pull requests that had already passed automated grading. Roughly half would not have been merged. The rejection reasons included code quality, breaking other code, and core functionality failures, none of which show up in a static analysis scan. The grader-versus-maintainer gap averaged about 24 percentage points across the model set.

Static analysis catches the Sonar categories. Human-calibrated evaluation catches the METR categories. A complete model selection process needs both. The models that minimize the Sonar categories are not always the same ones that minimize the METR gap, and the compliance environment doesn't care which category a failure falls into when something breaks in production.

The selection decision is always about which failure mode fits the environment. The Sonar data makes that tradeoff explicit. Use it.

---

*Sources: Sonar leaderboard study, 4,000+ Java coding tasks (mid-2026). METR, "PR Mergability Study" (March 2026), 296 AI-generated PRs reviewed by active maintainers. NIST AI RMF, MAP function. EU AI Act, Annex III high-risk AI obligations (effective August 2, 2026).*
