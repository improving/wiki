---
type: Reference
title: "Designing for Testing"
resource: "https://www.devlinliles.com/designing-for-testing/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I have had many discussions over the past several years about code and testing. These have ranged from deep debates on the merits of TDD or BDD to discussions around manual test case management. I have learned from all of these, and today had a discussion that made me want to articulate those views in a concise list. Here they are.

## 1. Everyone Owns the UI Automation

Software is a team sport, and your tests are the practice squad. If those are not strong enough to challenge you to do things correctly, you will make mistakes come game time (production).

## 2. Shared Test Code Is Production Code

If we are designing code for the purpose of making tests easier, then it should adhere to our normal standards. Test data factories, simulators, and other common code in our testing toolkit should be held to the same level as our production code — for one unavoidable reason: a craftsman should take pride in his tools, because without them we are just some dude standing in a workshop.

## 3. All Developers Can Read, Write, and Run Tests

This means all developers (testers, coders, etc. — the Scrum.org definition of "Developer") should be able to read, write, and run the tests. Out of sight means it doesn't matter.

## 4. Make It Stupid Easy

Building, deploying, and testing should be stupid easy. It should just be part of the workflow, because that is the only way it will happen consistently. [Psake](https://github.com/psake/psake?ref=devlinliles.com) is a great tool for doing this in a Windows environment. Something like:

Pull code → psake → make changes → psake → pull code and merge → psake → push code. Rinse, repeat.

All of these principles will lead down a path to more supportable code, and probably make you learn along the way.
