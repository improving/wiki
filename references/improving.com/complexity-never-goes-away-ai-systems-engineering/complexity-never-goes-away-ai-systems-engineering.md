---
type: Reference
title: "Complexity Never Goes Away, it Just Moves"
resource: "https://www.improving.com/thoughts/complexity-never-goes-away-ai-systems-engineering/"
author: "Josh Harrison"
published: '2026-07-29'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Like many of the physical inputs powering the AI economy (electricity, semiconductors, memory, etc.) engineering talent is a scarce resource. It’s also frustratingly hard to manage because it’s subjective, non-fungible, and a moving target. Skills that were highly prized just a few years ago have become obsolete under a new paradigm, or even a single product release, as the industry has seen with recent model releases.

For the last couple of years, a pervasive narrative has taken hold that is increasingly proving false:

1. We will no longer need engineers
2. Software will become cheap and abundant.

Instead, what has played out is running up against constraints from the physical world, manifested recently in the form of painful token costs. But a subtler, less understood constraint has proven just as stubborn: *engineering talent itself*.

A recurring question in the software industry is where engineers should focus their attention. A close cousin of that question is where complexity lives in a system. That answer has shifted as computing has evolved. In the era of command-line operating systems, for instance, front-end engineering didn't exist as a distinct role. The web and later mobile changed that, demanding deep knowledge of JavaScript, responsive design, single-page apps, and more.

Back-end systems followed their own trajectory. For decades in the late 20th century, database technology stayed largely the same; relational databases dominated, and there was little innovation beyond the core concepts of SQL, schemas, and their relationships. Data reporting was simple, so its share of total IT spend stayed low.

Then, in the early 2000s, complexity exploded with NoSQL, cloud databases, graph databases and other horizontal scaling paradigms. Once again the back-end became an expensive focus of engineering talent.

AI is no different. It's true that writing imperative code line by line now needs little attention in almost all cases. That is remarkable, because since the dawn of computing, programming has been the single greatest bottleneck. But new checkpoints have emerged, and the engineer's attention is needed elsewhere. Specifically, the objective now is to engineer systems that get better results from AI while reducing token consumption.

The first step into this territory was prompt engineering, which developed into context engineering, where a little up-front planning to craft refined instructions yielded noticeably better responses in both accuracy and cost. Over time, these techniques have grown more sophisticated and more standardized.

Zooming out, a clear barbell pattern has emerged: the pre and post-processing steps around an LLM are becoming increasingly important. Those steps matter greatly because an LLM is an expensive digital gauntlet. Before sending a payload into an LLM for heavy processing, up front refinement (harness engineering) and evaluation of the output (LLMOpps) provide a more reliable system.

Harness engineering consists of managing historical context, caching, tool integrations, external data services, retry logic, and any other steps that augment and orchestrate the messages flowing to and from the LLM. LLMOps handle the other side of the equation, measuring accuracy, token burn, security, and other metrics that can be continuously evaluated from the runtime environment. Together, they form an iterative feedback loop where the outputs from LLMOps become inputs that update the harness.

Complexity and the need for engineering specialization go hand in hand. As models, tooling, and problems grow more complex, new constraints will replace old ones. As AI automates programming, engineering efforts will continue to shift from writing code to architecting the systems around models.

We are at the very beginning stages, but just as we have seen with harness engineering and LLMOps, we should continue to expect an explosion of paradigms and roles that don't yet exist. In short, the need for systems engineers isn't going away. If anything, demand will increase and be deployed in new and unique ways as AI continues to mature.

This is the kind of shift the engineers at Improving help enterprise teams navigate. If you'd like to discuss what it means for your own systems, our [AI Experts](https://www.improving.com/expertise/ai/) are a good place to start.
