---
type: Reference
title: "The Scaffolding Is the Product: Why AI in Software Development Is a Systems Integration Problem"
resource: "https://www.devlinliles.com/the-scaffolding-is-the-product-why-ai-in-software-development-is-a-systems/"
author: "Devlin Liles"
published: '2026-07-02'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Parts of the industry have declared these systems AGI. Sequoia said it. Jensen Huang agreed. The same systems, asked to multiply two six-digit numbers, could not reliably do it.

A heatmap from o3-mini benchmarks tells the story compactly. When both operands are small, single digits or double digits, accuracy sits at 100%. Push past five digits on either operand and accuracy falls off sharply. By fifteen-digit multiplication, success rates are in the single digits. The model did not get less capable. It ran out of patterns to match.

This is not an edge case. It is the architecture describing itself.

## The Same Cliff Exists in Software

Software development follows the same curve. Ask an LLM for a sorting algorithm and you get textbook output. A React component with Tailwind, a CRUD endpoint in a well-documented framework: clean, fast, correct.

Ask it to refactor a 200-file service that evolved over three years across four teams, with undocumented business rules embedded in conditional logic, and it produces abstractions that look elegant and break behavior the business depends on.

The pattern maps directly onto the heatmap. Small, well-represented problems produce near-perfect output. Scale the complexity, more files, more domain context, more institutional knowledge required, and accuracy degrades on the same curve. Production-grade enterprise systems live in the red zone.

Research on grokking points at the mechanism. Models memorize first, building lookup tables of training examples, and only under specific conditions discover the underlying algorithm. For large models trained on internet-scale data, we have no reliable method to distinguish reasoning from retrieval. A correct answer and a memorized answer look identical from the outside.

Correct answers with broken reasoning follow. In math, the final number is right while the intermediate steps are wrong more than half the time. In software, the code compiles, the happy-path tests pass, and the edge case your domain produces every Tuesday at 3am fails it.

## Scale Does Not Close This Gap

The instinct is to assume the next model fixes this. The research argues otherwise: compositional generalization, the ability to combine known concepts into novel solutions, does not emerge from scale alone. The observation is older than the current architecture. Jerry Fodor and Zenon Pylyshyn made essentially this argument against connectionist systems in 1988, and the systematicity problem they described has outlived several generations of network design. A model trained on numbers up to 1,000 hits a wall at 2,000 regardless of parameter count. A model trained on five-file refactors does not understand your 200-file monolith because you gave it a longer context window.

This matters because it changes where you invest. If the ceiling were a scale problem, the right strategy would be waiting for bigger models. The ceiling is a scaffolding problem, and scaffolding is engineering work that compounds.

## General Intelligence Creates a Floor

Precision matters here, because the claim is easy to overread.

These systems are far from useless. I use them every day. They are strong tools for code generation, document analysis, and pattern recognition across volumes no human team could process at that speed. The production value is real, and I have watched it change how teams work across multiple companies and product lines.

General intelligence, human or artificial, creates a floor. Education does the same for people. A computer science degree gives you baseline capacity across a range of problems. You can read code in languages you have never used and reason about systems you have never built. The foundation transfers.

Nobody staffs a critical project by hiring the most generally educated person they can find. You hire for domain expertise, specific tooling fluency, and process discipline. General intelligence gets you in the room. Domain-specific capability gets the work done.

The same logic applies to AI in the engineering workflow. The foundation model gives you a floor, a remarkably high one, higher than anything available five years ago. The floor is now commodity. Every team on every project has access to the same baseline. The differentiation has moved upward.

## Where Differentiation Actually Lives

The teams pulling ahead treat AI-assisted development as a systems integration problem. The model is one node in a graph that includes human review, automated verification, domain-specific retrieval, and institutional process. Remove any node and the system degrades. The model alone produces 70% solutions. The scaffolding converts that to 95%. The last 5% is the team's accumulated understanding of their domain, their users, and their failure modes.

What the scaffolding looks like in practice follows a few recurring patterns.

**Context matters more than model capability.** A model generating code without knowledge of your domain model, your API contracts, and your data shapes is guessing. It interpolates from training data that looks similar enough. The highest-velocity teams I have worked with feed structured context into every generation: architecture decision records, interface definitions, test fixtures that encode expected behavior. They build retrieval pipelines tuned to their own codebase. Specific institutional knowledge replaces generic training data. The model stops guessing when you stop making it guess.

**Testing becomes the primary feedback mechanism.** Testing here is the layer that makes generated code trustworthy. Write the test first. Let the model write the implementation. Run the test. This is test-driven development, the discipline Kent Beck codified decades ago, and it turns out to be the right verification layer for a system that produces plausible-looking code with no model of correctness. The test is the guardrail the model cannot provide for itself. Teams that had strong test cultures before AI arrived are collecting a dividend they never anticipated.

**Code review changes shape.** Reviewing for syntax and style is finished work; the model handles both. Review moves to intent alignment. Does this generated code solve the actual business problem, or a problem that looks similar from the training distribution? This is the software equivalent of the correct answer with broken reasoning. The output compiles. The happy-path tests pass. The domain-specific edge case exposes the gap between pattern matching and understanding.

**CI/CD pipelines work as chain-of-thought scaffolding.** Each stage (lint, test, security scan, integration test, canary deploy) is a verification step that catches failures the model cannot self-detect. The teams that invested in pipeline maturity years ago built infrastructure designed to validate output from an unreliable producer. They did not know the producer would be an LLM. The principle was always the same: never trust the output, verify the output.

**Feedback loops have to encode learning the model cannot do itself.** The model does not learn from your production incidents. It does not adapt when your schema changes. It does not improve from the bug it introduced last Tuesday. Your process has to capture that learning and feed it back into the context the model receives. Post-incident reviews become training data for prompts. Architecture decisions become retrieval documents. The institutional memory lives in your scaffolding, not in the model's weights.

## The Real Separation

The gap between teams is no longer about which model they use. Everyone has access to the same foundation models. The gap is in the scaffolding.

One team asks the model to write code, reviews the output manually, and ships what looks right. Another team feeds the model structured domain context, validates output against automated test suites, runs it through a CI pipeline with security and integration gates, and captures failures as retrieval documents for the next generation cycle. Both teams use the same model. The outcomes are not comparable.

This is the systems integration problem. The model is a powerful component. Components do not ship products. Systems ship products. The engineering work (the retrieval pipeline, the test harness, the review process, the feedback loops, the governance layer) is the product. The model is a dependency.

## Where the Argument Could Break

Two counterarguments deserve real weight. The first is that tool use already solves the arithmetic problem: a model that calls a calculator multiplies fifteen-digit numbers perfectly, and the same pattern extends to code execution, retrieval, and verification. True, and the concession proves the point. The calculator call, the retrieval step, and the verification harness are scaffolding. The capability came from the system around the model, which is the argument.

The second is that scale skeptics have a poor track record. Capabilities that looked architecturally impossible kept arriving with the next training run, and compositional generalization may improve the same way. It may. Even a model that composes perfectly still lacks your undocumented business rules, your incident history, and the constraints that live in your team's heads. None of that is in the training data of any model at any scale. The domain knowledge gap survives the capability curve, and closing it is scaffolding work.

## The Question That Matters

The industry keeps asking when AGI will arrive. The useful question is different: have you built the scaffolding that makes the intelligence you already have perform in your domain?

AGI, if it ever arrives, is a learning problem. Does your system learn continuously in production? Does it adapt without retraining? Does it improve from its own mistakes? The models do not do this. Your engineering process can.

General intelligence creates the floor. Your specific learnings, your domain-tuned tools, and your deliberate process design set the ceiling. The floor is free. The ceiling is earned.

The teams that treat this as a systems integration problem are pulling away from the ones still waiting for the model to be smart enough on its own. No amount of capital, compute, or consensus changes what a frozen pattern engine is. The right scaffolding changes what it can do.

Build the scaffolding. That is where the compounding happens.
