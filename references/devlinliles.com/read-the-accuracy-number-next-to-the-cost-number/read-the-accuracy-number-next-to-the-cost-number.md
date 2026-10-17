---
type: Reference
title: "Read the Accuracy Number Next to the Cost Number"
resource: "https://www.devlinliles.com/read-the-accuracy-number-next-to-the-cost-number/"
author: "Devlin Liles"
published: '2026-09-30'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Before a routing savings percentage goes into a client deck, find the accuracy number sitting next to it. Without one, the percentage is a marketing claim with a decimal point.

That test matters this week because model routing just went from a heuristic Improving has been recommending clients build for themselves into a packaged feature shipping inside a frontier model release. NVIDIA's NeMo Switchyard, launched alongside Nemotron 3.5 Lightning on August 11, sits in front of a request and decides whether it needs the fast, cheap model or the slower, more capable one. It's the same move we walked through in July's webinar, Controlling AI Coding Costs Without Losing Productivity: most coding requests don't need the frontier model, and a router that can tell the difference cuts spend without anyone feeling a quality drop. What changed this week is that the routing layer now ships out of the box, and a set of partners, LangChain, Cognition, Ramp, and Classmethod's DevelopersIO team, have already published what it saved them.

Those disclosures are worth reading closely, especially for what sits next to the percentage. A router is a classifier making a bet on every request: this one is easy enough for the cheap model, send it there. Every classifier has an error rate, and the one worth worrying about here is a quality problem before it's ever a cost problem. Sending an easy request to the expensive model wastes a few cents and nobody notices. Sending a hard request to the cheap model produces a worse answer that ships anyway, and a pure cost-savings number has no way to show that it happened. The routing layer can be saving real money and quietly degrading a meaningful slice of output at the same time, and the top-line percentage will look identical either way.

The accuracy or quality metric has to travel with the cost number: same slide, same paragraph, same sentence. Footnotes and follow-up posts are too late. A savings figure without a stated accuracy delta next to it is reporting half the experiment.

The second question is what that accuracy number was measured against. A benchmark built from Cognition's autonomous agent traffic and a benchmark built from Ramp's fintech coding tickets are not describing the same task distribution, and neither one is describing a given client's ticket queue. Routing accuracy is a property of a router paired with a specific workload. A partner's disclosed number says something true about their own traffic and considerably less about what happens once that router meets a different mix of legacy code, security-sensitive changes, and routine boilerplate.

The third question is where in the distribution that accuracy number was measured. An aggregate figure can look strong while hiding a much worse failure rate on the hardest requests: the security-sensitive refactor, the cross-service change, the bug that only shows up under load. Those are the requests where a wrong answer costs the most, and they are also the requests a router is most likely to misjudge if it was tuned to look good on average. A headline accuracy number identical to another can describe a very different reality once it gets broken out by task difficulty.

Put those checks together and the discipline is straightforward to describe, even if it takes real engineering time to build. A routing claim needs a stated accuracy metric next to the cost figure. That metric needs to be measured on something closer to the client's actual workload than the vendor's own traffic. And it needs to hold up on the hard requests specifically, the ones an average across everything routed that week will quietly paper over. None of this is a knock on NeMo Switchyard or on the partners who published numbers this week. It is the same standard Improving applied in July, now aimed at a routing layer that ships by default instead of one a team has to build itself.

The cost number is easy to produce and easy to headline. The accuracy number requires holding out real requests, running them through both paths, and comparing the answers, which is slower and less flattering work to publish. That asymmetry is probably why the accuracy number goes missing more often than the cost number does. It is worth asking for anyway, every time a routing claim shows up in a deck.
