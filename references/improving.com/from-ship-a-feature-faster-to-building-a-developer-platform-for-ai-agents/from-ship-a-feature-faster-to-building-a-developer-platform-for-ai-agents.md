---
type: Reference
title: "From \"Ship a Feature Faster\" to Building a Developer Platform for AI Agents"
resource: "https://www.improving.com/thoughts/from-ship-a-feature-faster-to-building-a-developer-platform-for-ai-agents/"
author: "Bill Curry"
published: '2026-07-28'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Last October, David O'Hara and I hosted a webinar called *Ship a Feature Faster*. We set out to answer a practical question: could we use AI to build a real feature on Improving's internal Engage platform, live and in front of an audience, without hiding the problems along the way? Across four weeks, we worked through UX, code and testing, platform and CI/CD, and data and analytics.

In the months since, we have applied agentic development techniques across a growing number of client and internal projects. Project X, a recent project where this evolution is still unfolding, provides a useful lens into what we have learned more broadly. The most important lesson wasn't simply that agents could write code faster. It was that our existing developer platforms and delivery practices weren't designed to govern them across the development lifecycle.

On Project X, agent-generated implementations passed traditional quality gates while still diverging from the architecture, the story's intent, or the underlying business requirement. The code was well formed, but it wasn't always the right code. As agents move beyond autocomplete and begin planning work, modifying code, and opening pull requests, controls designed for human development teams are not automatically sufficient.

That gap — between passing every check and actually building the right thing — turned out to be the real story of the last nine months. Closing it pulled us into a much bigger platform question than we expected to be asking, and it's the one we'll pick up at our August webinar.

We also predicted that code generation would become increasingly compressible, while understanding the problem and assembling the right solution would not. Developers would spend less time producing an initial draft and more time reviewing AI-generated work. We argued that junior developers would still need the friction of writing and reviewing code themselves — the muscle memory that lets someone recognize a bad implementation on sight — and that paired programming would have to become paired review. Text-driven, spec-first workflows would also require tighter feedback loops to preserve the shared understanding traditionally built through conversation.

Those were predictions in October. Across the client and internal work we have done since, they have increasingly become operating realities.

### **How this played out on Project X**

Project X didn't begin as an experiment to see how much work we could hand to agents. It began like any well-run product effort, with detailed requirements, an MVP plan tied to them, and a weekly cadence of prioritized backlog items.

What changed was how the team moved each item from requirement to implementation. A developer worked with AI to draft the story and implementation plan, grounding both in the project's requirements, architecture, and design expectations. We then used separate agent-based checks to audit the story and plan for gaps before any code was written. Once the work was sufficiently defined, an execution agent using Devin or GitHub Copilot could implement it.

This was the "compressible work" we discussed in October: translating a well-defined plan into code. But as we saw on Project X and in other agentic development work, the speed of producing code exposed a different problem. The faster agents implemented, the more important it became to determine whether they had implemented the right thing.

### **The drift traditional quality gates could not catch**

Our existing quality gates were doing exactly what they were designed to do. Style checks, linting, type checking, and automated tests could tell us whether the code was well formed and whether known behaviors still worked. They could not determine whether an implementation reflected the intent of the story, satisfied the underlying requirement, or remained consistent with the architecture.

As a result, some agent-generated implementations passed every traditional automated check and still required significant correction. The problem was not necessarily code quality. It was alignment.

In one case, an agent created frontend tests by mocking an entire shared data module instead of using the project's established request-mocking infrastructure. The tests passed, but the approach could allow incomplete mocks to reach real APIs and made the test suite brittle as the data layer evolved. A linter or type checker would not flag the implementation because the code was valid and the tests were green. An architecture-aware review could recognize that it bypassed the project's intended testing pattern.

That exposed a new platform responsibility. We needed gates capable of evaluating the pull request against the linked issue, the acceptance criteria, the project requirements, and the architecture. In other words, we needed to test whether the agent had built the right thing, not only whether it had built the thing correctly.

Closing that gap became the focus of the next several months of tooling investment.

### **How the platform evolved around the agents**

Project X's tooling history shows a clear progression. Each stage added agent capability and exposed a new trust gap.

##### **April 2026: Establishing shared context.**

We introduced shared rules, reusable skills, basic commands, and CI and issue-synchronization plumbing so agents began with the project knowledge available to a human developer.

##### **May 2026: Improving specification quality.**

Agents helped draft stories, technical-debt items, implementation plans, and documentation updates. We added independent checks that audited those artifacts before implementation.

##### **June 2026: Standardizing behavior and adding independent review.**

We packaged the same skills across development environments and introduced AI quality gates in CI. These included architecture reviews, acceptance-criteria checks against the linked issue, and readiness checks before implementation.

##### **July 2026: Keeping project state trustworthy.**

We introduced readiness and synchronization capabilities that reconciled requirements, plans, documentation, and code. Developers could also verify acceptance criteria before opening a pull request.

The progression was shared context, specification quality, independent review, and project-level synchronization. Each stage increased what an agent could do and closed a trust gap exposed by the one before it.

### **From human in the loop to human on the loop**

With this tooling in place, agents could carry defined work through implementation, pull request creation, and review responses. Readiness, gap, and architecture checks gave us a practical way to address alignment problems.

This pointed toward a different operating model. Instead of initiating and approving every step, a human could supervise routine work and handle escalations. Human on the loop does not remove human accountability. People still define objectives, priorities, architectural and security boundaries, and decision rights. The agent operates within those boundaries and escalates exceptions, ambiguity, and material tradeoffs.

The remaining opportunity was not to let an agent determine product strategy. It was to reduce the manual coordination still required to move an eligible backlog item from planning through implementation.

![image 1 - From "Ship a Feature Faster" to Building a Developer Platform for AI Agents](images/AdobeStock_701849928.jpeg)

### **What's next: bounded planning loops**

That is the frontier we are working on now and the story we want to explore in August. The next evolution is not simply letting an agent write more code. It is allowing the agent to participate earlier in the lifecycle while remaining inside human-defined objectives and decision rights.

The planning loop we are working toward begins with a prioritized backlog and requirements established by the team. Within those boundaries, an agent identifies the next eligible candidate story, drafts the story and implementation plan, and evaluates both against the project's readiness and gap checks. If it encounters unclear requirements, conflicting priorities, architectural exceptions, or decisions outside its authority, it escalates to a person.

Once a story and plan pass those checks, they can be handed to a development-loop agent that:

- Builds the code.
- Validates the result against the goals stated in the requirement and the story. It checks not only whether tests pass, but whether the tests evaluate the right behavior.
- Confirms that the implementation follows our architecture and coding standards.
- Opens the pull request.

At every stage, the agent proceeds only within its defined authority and escalates when human judgment is required. Once a person resolves the issue, the process can resume. That is human on the loop applied across the delivery lifecycle, not just to code generation.

### **Why this matters for August**

The lesson extends beyond Project X. Across our agentic development work, the controls surrounding the agent have proven just as consequential as the agent's ability to generate code. As agents begin planning work, modifying code, opening pull requests, and running validation, the developer platform must do more than help human teams ship software. It must also govern agent identities, permissions, execution environments, access to code and data, and the path from a proposed change to production.

Most enterprise developer platforms were not designed with that actor in mind. Many secrets management practices were built around a human developer or a predictable pipeline identity, not an autonomous agent that can choose and invoke tools. Secure development controls often assume that a person will inspect a change before it ships. Default GitHub organization configurations assume that a developer pushes a commit and waits while the established review process takes over. Agents operate differently, and those assumptions can become control gaps.

Closing those gaps requires explicit controls for branch protections, repository permissions, agent authentication, auditability, secrets scope, and secret scanning. GitHub Apps, fine-grained personal access tokens, GitHub Actions environments, Azure Key Vault, and HashiCorp Vault all have roles to play, depending on the environment and regulatory requirements.

That makes agentic development a platform and operating-model concern, not simply a developer-tool decision. Platform, DevOps, architecture, security, and engineering leaders need to determine how agents will operate before those agents are allowed to participate broadly in delivery.

![image 1 - Improving Partners with Anthropic to Help Enterprises Adopt Responsible, Human‑Centered AI ](images/THE_TRUST_EVOLUTION.png)

The Project X progression also illustrates the [Improving AI Maturity Model](https://www.youtube.com/watch?v=OYbNxGzX_Ww), the eight-stage framework we introduced on June 8, 2026 — the same week, as it happens, that Project X's own tooling arc shows AI quality gates showing up in CI. The project began around Stage 3, with an agent completing a defined task and a human reviewing the output. The controls added later moved the delivery model toward Stages 5 and 6, where teams delegate objectives and let agents coordinate work within defined boundaries.

The important point is not the stage number itself. Every increase in agent autonomy requires a corresponding increase in platform maturity, governance, and oversight. Organizations cannot safely advance from assistance to delegation by expanding agent capability alone.

October asked whether AI could build a feature with us, live and in public. In August, we will continue with the harder question: Is the platform underneath development agents ready to support and govern what they are becoming?

A few of the questions worth sitting with before then:

- What does least-privilege access mean for an actor that can choose its own tools and touch several systems in a single run?
- Could your team answer, right now, what an agent did and why — without waiting for something to break first?
- Which of your current approval gates are sized for a human's pace, and which ones quietly become the bottleneck — or the blind spot — once code shows up ten times as fast?

We don't have all the answers yet either. That's what the August webinar is for.

If you'd rather talk it through sooner, we're also offering a 30-minute agentic developer platform readiness conversation for teams currently using, piloting, or evaluating GitHub Copilot. For teams that are still early in adoption, that conversation is also the door into our [GitHub Copilot Accelerator Workshop](https://marketplace.microsoft.com/en-us/marketplace/consulting-services/improving1723751010924.offer_id_github_copilot_accelerator?tab=Overview) — a hands-on, expert-led engagement to get developers using Copilot effectively before layering on the governance question this post raises.

If your organization is moving from AI-assisted development toward agents that plan work, modify code, and participate in delivery, join us on August 5 at 12:30 p.m. EDT for *Building the Developer Platform for AI Agents*.

[Register for Building the Developer Platform for AI Agents](https://www.improving.com/events/go-together/building-the-developer-platform-for-ai-agents/)
