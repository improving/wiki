---
type: Reference
title: "Business Roles and the AI Split: What to Delegate and What to Own"
resource: "https://www.devlinliles.com/business-roles-and-the-ai-split-what-to-delegate-and-what-to-own/"
author: "Devlin Liles"
published: '2026-07-29'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Business roles carry the clearest exposure to the judgment-bound / form-bound split. The client sees the output. Experienced clients can tell within minutes which layer got skipped. It's a different kind of credibility risk than shipping buggy code. It's visible in the first read, and it's attributed to the person who handed it over.

This post works through what that split looks like for the roles that sit closest to clients: business analysts, product managers, consultants, and strategists. For each, I'll name the tasks that belong in each category and the approach that actually works.

## Business Analyst

The BA role has more surface-area confusion between these two categories than almost any other.

**Judgment-bound:** Requirements elicitation is entirely judgment-bound. The BA's job in a discovery session is to hear what the stakeholder says, recognize what they mean, and surface the gap between the two. That pattern recognition comes from domain familiarity and from accumulated practice reading the difference between a feature request and an underlying need. AI can organize the notes from a session. It cannot do the interpretation. User persona development, as I described in part one, is the same: the observations belong to the BA; the structure belongs to the tool. Process flow analysis, particularly identifying where a current-state process breaks under load or exception conditions, requires someone who has seen enough processes to recognize a disguised workaround when they see one.

The right workflow for BA judgment-bound work looks like this: structured interview guides that AI generates in advance, elicitation sessions that the BA runs, and AI-assisted synthesis immediately after that organizes the raw observations into a first-pass model. The synthesis step is where the BA does the heaviest lifting, reviewing the AI's organization and correcting the interpretation. AI generates the structure of the synthesis; the BA corrects the meaning.

**Form-bound:** User story formatting is almost entirely form-bound once the requirements are understood. A well-defined template, a skill that enforces acceptance criteria structure, and a review pass are sufficient. The same is true for requirements traceability matrices, test scenario scaffolding from accepted stories, and meeting minutes from elicitation sessions. Generating a first-pass RACI from a stakeholder list and a project scope is form-bound. Verifying that the RACI is politically accurate is not.

## Product Manager

The PM role has a harder version of the same split because product decisions are judgment-bound in ways that look deceptively codifiable.

**Judgment-bound:** Prioritization is the clearest example. Frameworks like RICE and WSJF are form-bound; they're scoring models with defined inputs. But deciding what the inputs should be, and whether the model output reflects actual business reality, requires the PM to bring context that the framework cannot. A feature that scores low on a WSJF because the time-criticality is low might be the thing that closes a specific deal that finance is counting on. No model captures that unless someone with the context puts it in. The PM who lets AI fill in the prioritization scores without interrogating each one has outsourced the judgment to a formula.

Customer insight synthesis is judgment-bound in the same way BA requirements elicitation is. Interview notes can be organized and themed by AI accurately. The observation that three different customers described the same pain point in three completely different ways, and that the underlying complaint is actually about workflow visibility, not about the feature they requested, requires someone who was in the room.

**Form-bound:** Product requirements documents have a well-defined structure that AI handles well. Release notes are almost entirely form-bound, which is why they're one of the highest-leverage things a PM can automate. Competitive analysis formatting, roadmap presentation slides, and sprint review write-ups all fall here. Generating a first-draft PRD from a set of validated requirements and acceptance criteria is form-bound. Deciding whether the requirements are the right ones is not.

The PM's judgment-bound checklist should include: what problem are we solving (not what feature are we building), who specifically is experiencing it, what do we have to believe about the customer for this bet to pay off, and what would we see in six months if we're right. AI can prompt those questions and organize the answers. The answers are the PM's.

## Consultant

Consulting is almost entirely judgment-bound by design, which creates a specific risk: using AI to fill in the reasoning gaps that the consultant hasn't closed yet.

**Judgment-bound:** Situation assessment is the core of the work. The consultant observing an organization has to make a call about what's actually happening versus what the client thinks is happening. That call integrates what the consultant sees in the room, what they've seen in similar organizations, and what the data says. AI can analyze data. It cannot triangulate between data, observation, and pattern-matching across engagements because it doesn't have the engagements.

Recommendation development is judgment-bound for the same reason. The recommendation that will actually land with this client, given their current political dynamics, budget constraints, and change tolerance, is a judgment call. AI can generate a list of evidence-supported options. Deciding which one to lead with, and how to sequence the story, requires someone who knows the room.

Risk identification in a discovery engagement is particularly judgment-bound. The risks worth naming are not the ones on a standard risk register. They're the ones specific to this organization's conditions. An experienced consultant recognizes them because they've watched similar organizations fail in specific ways. That pattern-matching is precisely what AI lacks.

**Form-bound:** Proposal structure, SOW formatting, and deliverable templates are all form-bound. A well-built skill can produce a first-draft proposal from a meeting transcript and a scope definition. Executive summary formatting, status report structure, and findings presentation templates are form-bound. Review guides, interview scripts, and survey instruments are form-bound; the questions within them are judgment-bound.

The right approach for consulting work is to invest in form-bound tooling so that the consultant's time is as concentrated as possible on judgment-bound work. If a consultant is spending two hours formatting a proposal or restructuring a slide deck, that's two hours they're not spending on the analysis that justifies the engagement.

## Strategist

Strategy work is where the judgment-bound / form-bound split becomes most consequential, because the credibility exposure is highest.

**Judgment-bound:** Strategic framing is the work of deciding what the real question is, which is always different from the question as stated. AI cannot do that. It can answer the question as stated precisely. Deciding that the question as stated is the wrong question, and that answering it will give the client confidence in the wrong direction, is the strategist's core contribution.

Market analysis interpretation is judgment-bound in the synthesis step. The data can be gathered and organized well by AI. The leap from "this is what the data shows" to "this is what it means for this company's specific competitive position" requires the strategist's context and judgment. Done well, the data is the evidence for the argument. The argument is the human's.

Scenario planning is judgment-bound because it requires selecting the scenarios worth modeling, which is itself a strategic decision. Generating the content within a scenario is form-bound. Deciding which futures to take seriously is not.

**Form-bound:** Frameworks themselves are form-bound. A Porter's Five Forces template, a BCG matrix, a SWOT canvas: structure without substance. AI generates them cleanly. The strategist fills them in with judgment. Market data compilation, benchmark formatting, and competitor profile structure are all form-bound. First-draft scenario narratives from a defined set of parameters are form-bound; reviewing them for strategic plausibility is not.

The failure mode for AI-assisted strategy work is a finished-looking document that has the form of strategic insight without the reasoning underneath. Experienced clients and senior stakeholders detect this quickly, and the damage isn't just to the deliverable. It's to the credibility of the person who produced it.

## The Pattern Across Business Roles

The pattern holds across all four roles. Interpretation, synthesis, and recommendation belong to the human. Structure, format, and documentation can be automated. Build the form-bound infrastructure and protect the judgment time.

A BA spending forty minutes generating user story scaffolding manually is a BA spending forty minutes not talking to stakeholders. The tool should handle the scaffolding. The craft of using AI well in these roles isn't about writing better prompts. It's about knowing exactly where your reasoning is the product, and protecting that time.

Part three of this series takes the same framework into the development team, where the split shows up in specific and sometimes surprising ways for each role.

---

*Part 2 of 3 in the "Two Kinds of AI Work" series.*
