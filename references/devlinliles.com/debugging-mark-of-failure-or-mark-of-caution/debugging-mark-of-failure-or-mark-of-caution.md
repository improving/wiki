---
type: Reference
title: "Debugging: Mark of Failure or Mark of Caution?"
resource: "https://www.devlinliles.com/debugging-mark-of-failure-or-mark-of-caution/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I had some awesome conversations over the past several days at ALM Summit that I'll be blogging about over the next few days. One of those conversations was with David Corbin — a great, passionate geek. We were talking about the debugger and code logic validation. Here is how the conversation started. I am paraphrasing because I had a lot of coffee and can't remember the exact phrasing.

---

*David C.:* "What about debugging?"

*Me:* "I view having to debug code as a failure of the developer."

*David C.:* "Debugging is the only way you know if something broke that you didn't test for. Bring me your best code, that you are proud of, and I can change the behavior without breaking the tests. Debugging through and watching the locals, watches, and autos is the only way to know for sure."

*Me:* "What about strict mocking and automated testing? I can write tests that strictly constrain behavior and fail when it is modified."

*David C.:* "If you have a person with first name and last name properties with events on changed for each — write tests for that, and I can come into 90% of my clients and add in the first name setter a call to the last name changed event and that will not break the test."

---

The conversation went on like this for a while, and we had the rest of it on and off through the conference. I posed the following points, and David presented well-reasoned (wrong, but well-reasoned) arguments for debugging.

In the interest of validating my beliefs about how quality code is developed, I am looking for a broad set of responses.

## Ground Rules

1. This is for new development of logic I am programming and want to make sure I haven't broken. No one — including me — will discount the need for debugging as a first choice in a system without tests.
2. The main point is: are automated tests enough, or should developers have to step through line by line to validate unintended consequences?

## My Arguments

**1. Properly written automated tests validate all known requirements in a fast and repeatable way.**

If we assume that has been done (that was the assumption in the conversation), then debugging is needlessly repetitive. My automated tests are much faster, more reliable, and more actionable than stepping through every line while watching the debugging context. They are also an explicit codification of the intent of the system. Debugging, however, is prone to vastly more human error, is not codified, and is time-consuming.

**2. Cost-to-benefit for automated tests is much greater.**

This is a simple time-based evaluation of how much time a good test takes to develop versus how much cumulative time testing plus debugging would take. I don't believe — outside of intentional sabotage — that debugging will find significantly more issues than testing. This is simply based on requirements and repeatability.

Here is my example from our conversation: I am writing a manufacturing interface system that controls a closed system. If a vacuum port is opened during the production cycle at any point other than the allotted time, the whole of the production run is invalidated — $10,000,000 for each mistake. Without modifying the tests, break this example in a way that still passes the tests. Once (if) you have broken that, send it my way via the git repo and a pull request.

[https://github.com/DevlinLiles/DebugVsTesting](https://github.com/DevlinLiles/DebugVsTesting?ref=devlinliles.com)

I look forward to the conversation and the learning.
