---
type: Reference
title: "Right Way to Onboard an AI Coding Agent"
resource: "https://www.improving.com/thoughts/how-to-onboard-ai-coding-agent/"
author: "Daniel Scheufler"
published: '2026-09-15'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

When you hire a new engineer, you spend time teaching them how your organization writes code. You show them your standards, your patterns, and why you do things in a certain way. You do this because you know that without it, they'll write code that works but doesn't belong, like putting the implementation of a service method in the repository. Or reimplementing the business logic rather than using the existing service to do it.

AI has the same problem. The agent wasn't in the meetings where you discussed and decided on your architecture. It doesn't know what "the right way" means in your context. If you don't tell it, it will do what it thinks is right... which is usually whatever was the most common and popular approach on the internet.

You need to onboard the AI agent and help them by capturing context. You'll have to write down what "the right way" actually means. But don't just document everything. You'll spend a thousand dollars generating documentation that only increases your token costs.

## Providing Context to Onboard an AI Agent

The goal of providing context is to provide the knowledge that matters with consistency, so the AI coding agent can onboard succesfully.

Here are few ways to do it:

### 1. Start with coding standards

Different code serves different purposes.

- Production code should be succinct, while test code should be descriptive. Less code in production means fewer bugs, less cognitive load, and less token spend.
- Test code is different and when a test fails, you want it to immediately reveal what went wrong. So, Test names should be descriptive enough to reveal the intention.

That information shows up in your standards, not the just hows, but the whys too.

### 2. Your architecture patterns matter

You want the agent to follow your design decisions, right? The rationale behind why you chose one approach over another. This is where Architectural Decision Records (ADRs) come in.

An [ADR](https://github.com/architecture-decision-record/architecture-decision-record) captures the stuff everybody knows, but nobody writes down. It takes the implicit understanding about where X behavior should live and makes it explicit. For AI, this is critical as the agent can read an ADR and understand not only what you decided, but why as well. That means it can continue that pattern, instead of internet-default!

### 3. A quick aside about guardrails

Context is what you document. Your architecture, coding standards, ADRs, glossary of business terms. Guardrails are the constraints you encode. They are specific, enforceable guidelines, like, "Keep Code Coverage above 80%" and "Code Should be formatted like ...".

The AI agent needs to understand the intent before it can follow the ‘what’ correctly. And you want those guardrails to run deterministically. But we can often conflate context with constraints in conversations. [Rules like “Keep Code Coverage above ...” are only suggestions](https://www.devlinliles.com/a-rule-in-the-prompt-is-a-suggestion/) if we include them in any document. This kind of context is best captured as a guard rail. We’ll cover guard rails in future posts.

### 4. Structure your context file

For context management, you can't just dump all your documentation into a folder and hope the AI finds it. Suppose you have three documents about old patterns and one about the new pattern. Guess which one the AI is more likely to reproduce? Yeah, the more common one. The context you keep where the AI can find it has to serve the AI AND the Human.

Structure your documentation so the most important information comes first. An ADR starts with the decision and rationale. A coding standards document starts with the most critical rules. Documenting the thinking upfront would also reduce your AI costs as input tokens are cheaper than output tokens. That means your AI spends less tokens hunting for the right file, because you fed it the critical information first.

### 5. Delete over deprecate

When you change a pattern, don't mark the old documentation as "deprecated." Delete it! Deprecated documentation is poison for AI. The agent will read it and think it's still valid.

When you delete it, do not let just move to the trash for 30 days. The AI agent can peak inside the trash as well sometimes. Remove the file from directory or folder completely.

### 6. Start small

Pick one area - architecture or coding standards. Document what already exists and make it discoverable. Then iterate.

Each time the agent makes a mistake, ask yourself: did I document this? If not, document it. If you did, make the documentation clearer or more prominent.

## Final Words

You're not trying to create a perfect knowledge base. You're trying to make your AI more consistent. Consistency comes from making implicit knowledge explicit. The work hasn't changed. The tool has changed.

Now the question is what does your team know that you haven't written down yet?

We’ve been helping enterprises build AI systems that work the way they actually work, not the way the internet assumes they should. [Talk to our AI team](https://www.improving.com/expertise/ai/) to see where your context is thin and how to fix it.
