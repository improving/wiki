---
type: Reference
title: "AI Governance as Infrastructure: A Four-Layer Framework for Agentic AI"
resource: "https://www.improving.com/thoughts/ai-governance-agentic-ai-framework/"
author: "Devlin Liles"
published: '2026-08-25'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

I sat with a CTO last quarter who walked me through their company’s AI governance framework. There were around forty slides covering acceptable use policy, data classification tiers, a list of prohibited use cases, and sign-off from legal and HR. It looked complete.

Three months later, a team in the same company had been routing vendor contracts through a personal AI account, and the framework had been sitting on the shared drive the entire time. The diligence was real, but the framework solved the wrong problem. It treated an AI governance framework as a policy problem, the same kind of problem a code of conduct solves for human behavior.

Policy framing assumes the entity being governed reads the document, exercises judgment about when to apply it, and occasionally chooses compliance. An AI agent does none of that. It executes exactly what it is configured to do, at machine speed, with no capacity to recognize that it crossed a line drawn in a document it never had access to. In this blog post, we will take a close look at an AI governance framework and how to build an enterprise AI governance framework that team actually implements.

## **Why the Policy-First Framework Fails at Machine Speed**

Policy governance had a good run in enterprise technology because humans are slow enough, and visible enough, to audit after the fact. You can review what an employee did last Tuesday, and you can ask them what they were thinking. The audit happens downstream of the action, and that is fine, because the action itself took hours or days to unfold.

Agentic AI governance does not give you that gap. A single enterprise workflow can complete dozens of discrete actions before a human looks at the output. The math on this is not abstract: an agent completing each step correctly 95% of the time, which is solid performance for an agent, completes a twenty-step chain successfully about 36% of the time. The odds are worse than a coin flip. By the time someone notices the anomaly, the agent may have sent a dozen emails, updated several records, and generated a document under terms nobody approved.

The lesson here is about governance design, not a reason to avoid agentic AI. The rules have to evaluate each action before it executes, not after the chain completes, and someone happens to review the output later. That single requirement is what separates a governance framework that works from one that reads well in a board deck, and it’s usually the first gap we find when we run an [AI governance and readiness assessment](https://www.improving.com/expertise/ai/strategy-roadmap-assessment/) with a client before their first agentic workflow goes into production.

## CI/CD Model for Enterprise AI Governance

I come at AI governance as an engineer, not as a policy person, and the framing that has worked for me is one I did not invent for AI. It is the one my teams already used for software delivery: **version control, automated testing, CI/CD pipelines**.

They exist because someone built infrastructure that makes carelessness structurally difficult.

- Version control externalizes the history of every change and makes it visible to anyone, regardless of who made the change or whether they remember why they made it.
- Automated tests encode what the system is supposed to do and check it on every run
- CI/CD pipelines encode the steps required to deploy safely and execute them the same way every time, whether or not the senior engineer who wrote them is in the room that day.

We can call it cognitive scaffolding, *infrastructure that holds knowledge and enforces behavior*, so the organization does not depend on any individual remembering the right thing to do under pressure.

AI governance is the same problem wearing different clothes:

- **Audit trail is your version control:** It tells what the agent did and why.
- **Quality gate is your automated test: **It answers whether the output meets the standard before it moves forward.
- **Boundary definition is your deployment pipeline:** It covers what the system is actually allowed to touch.
- **Human approval point is your pull request review:** Moment where a person’s judgment enters before something ships.

Line those up side-by-side and the parallel gets sharper.

- Software delivery scaffolding runs on version control, automated tests, a deployment pipeline, and PR review.
- AI governance scaffolding runs on audit trails, quality gates, boundary enforcement, and human approval points.

The organizations that already built the first list well are, unsurprisingly, the ones building the second list fastest.

## **Four Layers of an AI Governance Framework, Built as Infrastructure**

A governance framework built as infrastructure, rather than as policy, runs in four layers, and each one maps to something an engineering team already understands from delivery pipelines.

### **Layer One: Set the rulebook of risk tiers and approval thresholds**

The risk rulebook covers risk tiers, approval thresholds, data classification tiers, and the policy lifecycle itself. Most of that groundwork overlaps directly with the data governance checklist that should already exist before AI governance gets layered on top of it.

The original policy document earns a real job, as the input to a system that enforces it, rather than a PDF employees are expected to have memorized before they act.

### **Layer Two: Gate which models, tools, and data sources can participate**

Gating determines which models, tools, and data sources are even eligible to participate in a workflow at all. It functions as an [access control layer](https://www.improving.com/thoughts/mcp-authorization-policy-driven-tool-invocation-control/), applying least privilege to agents the same way it has always applied to service accounts, enforced technically rather than requested politely in an onboarding email.

### **Layer Three: Enforce runtime behavior before every action executes**

Runtime behavior is enforced by a controller sitting between every proposed action and its execution, checking that action against the active policy before it runs. It works like a deployment gate that blocks a bad build before it reaches production, except the “build” here is a single agent action, and the gate fires in milliseconds rather than on a nightly schedule.

Agent identity and privilege stop being an afterthought at this layer, since the controller has to know exactly what an [agent is allowed to touch](https://www.improving.com/thoughts/platform-security-governance-ai-agents/) before it decides whether to let an action through.

### L**ayer Four: Generate tamper-resistant evidence automatically**

Evidence means every action and decision captured automatically in a structured, tamper-resistant trail. They are not reconstructed from partial logs after something goes wrong. Evidence are generated as a byproduct of the action itself, the same way a CI pipeline produces a build log whether or not anyone ever reads it that week.

Across the organizations Improving has worked with, investment tends to concentrate in layer one, with almost nothing built for layers two through four.

- We worked with a **global industrial manufacturer** that had a dozen business segments running parallel AI efforts under one governance conversation, with staged rollout criteria and security sign-off requirements on paper, but **no unified way to see what was actually running** across segments or check it against that rulebook in real time.
- We advised an **energy technology company** with the same shape from a different angle: an AI council, a hackathon program, and an accelerator all generating activity in parallel, and a governance framework describing what should happen, with **nothing enforcing it action by action**.

Both had a thorough rulebook and a committee that revisits it quarterly, but the runtime did whatever it was configured to do, with nobody checking each action against the rulebook in real time.

They had the forty-some-slide framework from the opening of this piece, just built by a different company. Both frameworks are incomplete in exactly the place where incompleteness is most expensive, and NIST’s AI Risk Management Framework and ISO 42001 both point at that same gap without fully closing it. They describe what good governance should accomplish, but the process of accomplishment still has to be engineered.

## **Argument Against AI Governance Built as Architecture**

There are two arguments that can be made against the notion of building AI governance as architecture.

### Objection 1: Policy-first Governance is a Requirement

Regulated industries need policy-first governance, because auditors want documents, not architecture diagrams.

The objection is fair, and it misses the actual issue: an auditor wants evidence that governance actually happened, and a runtime system that logs every action automatically produces stronger evidence than a policy binder ever could. The documentation requirement stays in place, satisfied by an audit trail instead of a compliance narrative someone reconstructed from memory after the fact.

### Objection 2: Building Infrastructure Would be too Much

This much infrastructure is overkill for an organization running a handful of AI use cases rather than a fleet of autonomous agents, and that’s fair up to a point.

An organization still reviewing every AI output by hand doesn’t need a runtime enforcement layer yet, because a human is already checking every action in real time before it takes effect. The four-layer architecture becomes necessary at the exact moment autonomy enters the picture, when an agent starts taking actions between human checkpoints instead of at every single step. The real mistake is waiting until after the autonomous workflow is already live to notice that nothing was ever built to catch it.

## **What This Means for How You Build the AI Governance Framework**

If your organization already runs disciplined CI/CD, you’re extending a pattern that already works, instead of starting from zero on AI governance:

- Externalize judgment into infrastructure instead of leaving it in people’s heads
- Check things automatically instead of hoping someone remembers
- Generate evidence as a byproduct of normal operation instead of assembling it under pressure during an audit

The organizations that get this right treat NIST’s framework and ISO 42001 the way a good engineering team treats a coding standard: input describing what “good” looks like, not the enforcement mechanism itself. Checking it on every action, without relying on a human to remember, belongs to the runtime infrastructure rather than the standard.

For the specific controls that make each layer real in production, see the [five AI governance best practices](https://www.improving.com/thoughts/ai-governance-best-practices/) we recommend every enterprise put in place before an agent goes live. When we build this with clients, the pattern we apply, what we call the Governance & Risk Framework internally, is deliberately structured in this way. The policy work happens once, and the enforcement work happens on every single action after that, automatically.

I keep coming back to CI/CD when clients ask about what an AI governance framework actually requires. The analogy earns its keep because it is the same discipline underneath, aimed at a system that runs faster and less visibly than the one your engineering team already learned to govern.

## Final Words

The AI governance frameworks that survive contact with agentic AI are the ones built like pipelines. The ones that do not survive are the ones built like policy binders, and the difference shows up exactly once, at the moment an agent does something nobody approved, when the only question that matters is whether anything was actually watching.

Before your next AI project moves past a demo, pull up whatever AI governance document your organization currently has and ask one question: does anything actually check a proposed agent action against that document before the action executes, or does enforcement depend entirely on someone having read it first? If the honest answer is the second one, you already know where layer three needs to start. What would it take to close that gap on just one workflow this quarter?

If you’re wrestling with that question right now, I’d rather talk it through than have you guess. Find me on [LinkedIn](https://www.linkedin.com/in/devlinliles) and walk me through what your current framework actually enforces versus what it assumes people will do, and I’ll tell you honestly where I see the gap.

Improving works with enterprise teams to turn governance documents into runtime infrastructure: building the gating, quality checks, and audit trails that let agentic AI move fast without moving blind. If you’re staring down an agentic workflow that’s about to go into production faster than your governance framework can keep up, that’s exactly the [conversation we should have](https://www.improving.com/contact/).
