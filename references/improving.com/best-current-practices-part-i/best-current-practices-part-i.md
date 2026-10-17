---
type: Reference
title: "Best Current Practices, Part 1"
resource: "https://www.improving.com/thoughts/best-current-practices-part-i/"
author: "Daniel Scheufler"
published: '2023-02-01'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

When entering a new technology or approaching a new design challenge, we usually want to start with tried-and-true paths. There’s no need to reinvent the wheel but knowing which practices to apply and when they are feasible can be difficult. The typical advice one would get is to find and follow the best practices. But what do we mean by “Best Practices”?

A best practice is usually defined as the current opinion of most professionals in the industry about the best approaches, tools, and techniques to apply to common problems. Considering that time continues to march forward and new technologies are constantly developed, how can we ever hope to figure out the true best practice?

I think it’s best if we take a step back. Since our environment continually changes and new technologies always appear, the best practice cannot be some static thing. Instead, we should probably consider the best *current *practices. After all, the best professionals change their opinions as new information becomes available. Thus, over time, we can expect the best current practices to shift and change as the industry learns to leverage its tools against today's challenges. (Remember at one point, the Monolith was a best practice.)

### Best practices are always time-bound

The best way to accomplish something 20 years ago is not going to be as effective today, so the best current practices should be expected to change over time. New tools, new options, and new constraints exist today.

Before the advent of the Web, the best way to serve information to a large group of people might have been a newsletter or a bulletin board! There is however a curious second-order effect that technology has on its best practices. The scope of solutions we consider can sometimes be limited by our tools. Remember the old proverb:

“To a man with only a hammer, the world is full of nails”

So, while it is always prudent to attempt to learn from the wisdom and failures of others, we must keep in mind that every past event did not have the same tools available for it. The tools we have today MUST be able to change the solutions we consider. Dr. Goldratt, who developed an industrial theory called the Theory of Constraints, pointed to the need for manufacturing to carefully re-evaluate the real constraints which impact our systems today.

It is not enough to merely insert computers where the paper was once used. Instead, when considering how to design or migrate a process, we need a deeper knowledge of what the business actually needs in order to leverage computer systems to their full utility. Blindly following a best practice without considering its context and time means we ignore options to maximize value for our clients.

### The best current practice depends on your context

Best current practices often have some implicit context baked into their advice. That is, have some assumed context for where the practices are best suited. For example, Microservices are best in the assumption that an organization expects to reduce redundancy through reuse.

Commonly, the best current infrastructure practices assume something about an organization's communication structures. It is common to refer to Conway’s Law when considering organizational changes, such as team structures in these contexts. But with these implicit contexts come some unspoken assumptions.

Let’s take Netflix for example. What kind of culture and technical maturity did Netflix have or develop to make their approach to microservices feasible? Not every organization has the operational maturity to support microservices scaled out to support millions upon millions of requests every hour. So, what kind of benefit could we reasonably expect from running Netflix’s [Chaos Monkey](https://www.gremlin.com/chaos-monkey/the-origin-of-chaos-monkey/) in an organization that is not primed to understand or respond to the kind of failures that the tool is designed to produce?

Without surfacing these assumptions, simply following the best current practices can lead an immature organization into an untenable position. So, surfacing the assumptions, or at least considering them before selecting a practice to follow, is absolutely necessary for success! While we ought to leverage the best current practices to expedite our own delivery, to do so blindly will be to take on hidden risks. This commits us to certain paths of action that we may not be able to accomplish. All micro-service architectures assume a degree of maintenance and flexibility to maintain.

Moreover, these architectures need a reasonably mature ops organization to keep all those plates spinning and tuned up. Our technical choices commit us to certain patterns of communication and certain mental models when considering and adapting to future situations.

### Teasing out the assumptions

So, what can be done to tease out the assumptions inherent in our best practices? It is best to consider any best current practice as a decision-making rule or principle. *It is there to advise, not dictate. *As with any decision-making rules, ask questions about its core principles. Questions like the following:

- When does this principle/rule apply?

- When does it NOT?

- At what limit should this principle give way to another?

- What does applying this principle commit us to in the future? Or In order to follow through on this principle... what are we committing ourselves to?

When viewing any practice in this way, it is usually appropriate to start looking at all of the best current practices as a known set of trade-offs that work out favorably for the taker. The value of articulating the assumptions is in improved decision-making.

Pablo Picasso is credited with saying “Learn the rules like a pro so you can break them like an artist.” Best current practices can and should be learned deeply! Although, we must understand their context and conditions to know when and if we should apply them to our specific circumstances!

In conclusion, it is sensible to follow the best practices. However, under certain circumstances, assuming intentional consideration has been made about trade-offs, it can be beneficial to opt for a non-best current practice. Remember, learning the right time to do this takes some finesse and experience.

For best results, get the choices and rationales evaluated by respected peers before implementing them. Come back next time, and we can discuss some specific circumstances when teams can benefit from not following the best practices in part 2 of the blog series.

To learn more about best practices, [reach out to us](https://improving.com/contact/).
