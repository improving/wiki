---
type: Reference
title: "Why AI Skills Are Now Part of the Product Owner’s Playbook"
resource: "https://www.improving.com/thoughts/ai-skills-product-owners-playbook/"
author: "Claudio Lassala"
published: '2026-07-01'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Product Owners have always been managers of information, i.e. translators. They sit between what the business needs and what the engineering team builds. They write specifications, refine backlogs, prioritize features.

AI changes the economics of work. Not by replacing the PO, but by compressing the parts of the role that used to consume weeks into hours. The result isn’t a smaller role. It’s a role that finally has time for the work that matters most: understanding the problem, validating whether the solution is right, and making sure the team is building towards impact rather than output.

I’ve started thinking of this as the shift from **Information Technology to Impact Technology**. To survive this shift, the Product Owners must master the Impact Technology cycle, transitioning from raw inputs to human value:

- **Data:** Raw and unstructured building blocks.
- **Knowledge:** Information processed, synthesized, and understood.
- **Insights:** Identification of actionable patterns and connections.
- **Wisdom:** Strategic application of those insights to navigate complex problems.
- **Positive Impact:** Solving human needs and creating actual value.

We’ve spent years collecting data, organizing it, reporting on it. The industry is good at information. What it’s not good at is turning that information into something that changes an outcome for a user. That’s where the PO’s value lives now: not in managing information, but in driving the cycle from data to knowledge to insight to impact.

## **Fifteen Years of Procrastination, Resolved in an Afternoon**

I have a blog with over 600 posts spanning 20 years. For 15 of those years, the taxonomy was a mess. Overlapping categories, one-off tags, inconsistent naming. “Personal Growth” and “Personal Development” coexisted as separate categories. Posts sat uncategorized. The work to clean it up was always obvious and always deferred, because it was boring and manual and nobody wanted to spend weeks on it.

With AI, the cleanup took an afternoon.

I started by defining the rules: consolidate overlapping categories, remove one-off tags with fewer than three posts, flatten the hierarchy to under ten top-level themes. Then I ran frequency analysis across all posts to map where the overlaps lived.

For the execution, I used Python scripts through **LM Studio**, which let me run local models without sending data to a cloud API. I toggled between DeepSeek (7B parameters) for speed on straightforward categorization and a larger GPT OSS 20B model for posts that required more reasoning about where they belonged. Every script ran in **dry-run mode** first. For any post where the model’s confidence was below 85%, it generated a CSV for manual review instead of making the change automatically.

Out of one batch of 210 posts, 182 were categorized at high confidence. The final taxonomy landed at nine core themes. The 15-year backlog was gone – in an afternoon.

This is what AI does for a PO: it collapses the timeline on work that was always worth doing but never worth the manual cost. The PO’s job in this workflow wasn’t typing or categorizing. It was defining the rules, reviewing the edge cases, and making the judgment calls the model couldn’t. That’s the same skill set a PO uses when refining a backlog or validating acceptance criteria. The tool changed but the judgment didn’t.

## **Describing the “What,” Not the “How”**

One of the shifts AI enables for Product Owners is moving from writing specifications to describing outcomes in natural language and watching them materialize.

This is where Behavior-Driven Development becomes a different kind of tool. The “In order to / As a / I want to” format paired with Gherkin scenarios (Given / When / Then) has been around for years. What’s new is that an LLM can take those scenarios and produce working code from them directly. The PO writes the intent and the model generates the implementation. The PO reviews whether the output matches the intent.

I call the moment it clicks the "30-Second Wow," which means showing something concrete quickly and let the visuals make the point. We can take that prototype to stakeholders first. When stakeholders can see the thing and start saying "can we move this here?" or "could it also do that?", they stop evaluating and start contributing. That is where validated intent comes from. Once intent is confirmed, the prototype hands the Scrum Team something grounded to build against and improve their productivity much better than a 40-page specification document.

The PO's value in this loop is making sure outcome drives the work, not output. That requires understanding the user’s problem deeply enough to recognize when the solution misses, even if it looks correct on the surface. AI handles the translation from intent to code. The PO handles the validation that the intent was correct in the first place.

## **Getting a Second Opinion**

One discipline I’ve adopted: never trust a single AI session for anything that matters.

When I use an AI to help build a plan, a product strategy, a sprint scope, a prioritization framework, I spin up a separate instance and give it an adversarial prompt. “Find the holes in this plan. What am I not seeing? What assumptions haven’t been tested?”

The reason for a separate instance is that the first session has context bias. It helped build the plan, so it’s predisposed to defend it. A fresh instance approaches the work cold, the way a skeptical colleague would. The PO’s role here isn’t to accept either model’s opinion as final. It’s to hold both outputs and make the judgment call. (For more on how this auditing discipline works alongside [Investigation Markdown and the broader AI workflow](https://www.improving.com/thoughts/embedding-ai-into-daily-development/), I wrote about the engineering side in the first post in this series.)

## **Game You’re Playing**

*The resistance to AI in product roles usually comes from the same place it comes from everywhere: fear that the tool replaces the person. But the PO who thinks AI replaces them is confusing the output with the outcome.*

AI can generate a specification. It can categorize 600 blog posts. It can produce a working prototype from a Gherkin scenario. It cannot tell you whether any of those outputs solve the right problem for the right user.

That judgment is the PO’s job. AI makes product owners faster at everything around it. The Product Owner of the future is not a "human typewriter" transcribing requirements. You are a **"Badass Maker"** (in the spirit of Kathy Sierra). Your goal is not to master the tool, but to use the tool to make your users and your team awesome.

I keep coming back to a question: what is the prize of the game you’re playing? Are you playing to produce output, or are you playing to create impact? If it’s impact, then AI is the best tool a PO has ever been handed. Not because it does the work, but because it clears the path to the work that only a human can do.

As for me: I do not play to win. I play to learn. If you focus on learning and impact, the win takes care of itself.

If your product team is exploring how to build AI into their workflow, Improving’s [AI training programs](https://www.improving.com/services/training/ai/) are designed for exactly this, practical, role-based, and focused on adoption that sticks.

For any comments or suggestions on this article, find me on [LinkedIn](https://www.linkedin.com/in/claudiolassala/).
