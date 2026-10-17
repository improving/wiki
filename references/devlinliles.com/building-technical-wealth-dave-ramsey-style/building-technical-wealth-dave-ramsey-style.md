---
type: Reference
title: "Building Technical Wealth — Dave Ramsey Style"
resource: "https://www.devlinliles.com/building-technical-wealth-dave-ramsey-style/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

*Updated with great feedback from Richard Hundhausen and Charles Bradley*

I was sitting today in the Professional Scrum Developer Train the Trainer event when the topic of technical debt and building technical wealth the Dave Ramsey way came up. I loved this analogy, and wanted to flesh it out. There are some standard approaches here that Ramsey frames very well for dealing with building financial wealth — below is my version of those applied to the technical debt problem.

## Defining the Problem

**Technical Debt** — I define technical debt as: "The eventual consequences of continually trading craftsmanship for short-term velocity." For legacy code, it is all the built-up issues with a code base.

**Technical Wealth** — I define technical wealth as the flexibility of a solution to change as it delivers value to the customer without massive change costs.

## **Stop Creating More Debt**

"Stop creating new debt by creating a very high quality definition of done for your team. Use this [Definition of Done](https://www.scrum.org/resources/definition-done?ref=devlinliles.com) for all work going forward. There is no use in resolving old tech debt until you learn how to stop creating new tech debt. Don't go for a perfect Definition of Done — just one that minimizes the amount of new tech debt created down to a very small or zero amount."

— Charles Bradley, Scrum.org Trainer

## The Seven Baby Steps — Developer Edition

### Baby Step 1: Build a Safety Net of Tests

A safety net of basic acceptance tests focused on the main business process flows will give you a thin net to start improving the code base. These tests should be automated. If you have to use manual testing for now, be sure to take time in step 3 to automate them. Focus on the most business-critical flows for your safety net — just like picking the highest-interest debt to pay off first, it matters what you cover.

*Recommended reading: *[*Working Effectively with Legacy Code*](http://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052?ref=devlinliles.com)* — Michael Feathers*

### Baby Step 2: Fix Problems Inside the Safety Net

List out your currently known issues by area. Keep this list visible, and when a backlog item for the current sprint touches an area with one of those issues, incrementally work on it. Make sure you have a safety net in that area first.

*Recommended reading: *[*Refactoring to Patterns*](http://www.amazon.com/Refactoring-Patterns-Joshua-Kerievsky/dp/0321213351?ref=devlinliles.com)* — Joshua Kerievsky*

### Baby Step 3: Build Coverage Through Changes

Once you have understood and implemented the first two baby steps, start increasing code coverage by including unit testing in every change. When we touch the code base we have to wrap what we intend to change in a test, and then make the change. This is the Boy Scout Rule *(original link removed — no longer available due to age)* in action.

*Recommended reading: *[*The Art of Unit Testing*](http://www.amazon.com/Art-Unit-Testing-Examples-Net/dp/1933988274?ref=devlinliles.com)* — Roy Osherove*

### Baby Step 4: Invest in Automated Behavior Testing

When you reach this step, you have built solid applications and made positive improvements. Continue building technical wealth by adding behavior tests and limiting implementations to the business value requested.

*Recommended reading: *[*ATDD by Example*](http://www.amazon.com/ATDD-Example-Test-Driven-Development-Addison-Wesley/dp/0321784154?ref=devlinliles.com)* — Markus Gärtner*

### Baby Step 5: Invest in Skill Sets and the Future

By this point, you should have already started Baby Step 4 — investing in automated behavior testing — *before* you invest in skill sets. Whether you are working on your own skills or those of other team members, you need to do it now. This can be reading blogs, podcasts, or books.

*Recommended reading: *[*Seven Languages in Seven Weeks*](https://pragprog.com/titles/btlang/seven-languages-in-seven-weeks/?ref=devlinliles.com)

### Baby Step 6: Design for the Future, Implement for Today

Now it is time to begin applying your time and intelligence toward enhancing the application's technical capabilities and the value you can deliver. Learn practices and patterns for the growth of capabilities.

*Recommended reading: *[*Design Patterns*](https://www.dofactory.com/net/design-patterns?ref=devlinliles.com)* (Gang of Four)*

### Baby Step 7: Build Wealth and Give

It is time to build great business velocity and continue to leave a great code base for the application. Build wealth — and share what you have learned.

*Recommended reading: *[*Clean Code*](http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882?ref=devlinliles.com)* — Robert C. Martin*

---

Taking these steps helps us accomplish the goals of our business, increase our morale, and live the life of good software craftsmen.
