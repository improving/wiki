---
type: Reference
title: "Claude and Notion Just Automated My Entire Product Workflow"
resource: "https://www.improving.com/thoughts/claude-and-notion-product-workflow-automation/"
author: "Fletch Fletcher"
published: '2025-09-17'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Recently, I've been messing around with this “MCP thing” (Model Context Protocol we keep hearing about, but don’t understand), and in short, it is changing everything about how I handle product management. Everything. For the past quarter, I've been working with Notion, AI tools, and Agentic AI solutions to create practical tools for my fellow consultants. My focus has been on saving time, money, and resources—not just for ourselves, but also for our clients and Improving. This isn't a theoretical exercise or sandbox project; I'm developing real tools that deliver genuine value.

## ((The Challenge: Turning Vision into Actionable Tasks))[[#005596]]

Product managers know the drill. We spend way too much time getting the perfect requirements to the development team. Trying to get all the user stories mapped out, functional requirements documented, the whole nine yards. Then comes the part that makes you want to bang your head against the wall - manually turning all that into actual trackable tasks in the “highly controlled” tool the business manages. I'm talking about going through every single requirement, breaking it down, setting dates, figuring out priorities, organizing it all in your task management system, etc. It's so tedious, and often, we usually end up missing requirements and being inconsistent.

Well, not anymore.

## ((Enter MCP - Connect The Dots))[[#005596]]

Anthropic released something called Model Context Protocol, and it basically lets Claude talk directly to my tools. In this case, only one specific Notion workspace.

If I’m being honest, setting it up was way easier than I thought it would be:

**((1.))[[#5BC2A7]] Installed the MCP server** - just used npm, and it took roughly 5 minutes

**((2.))[[#5BC2A7]] Got the Notion integration token** – standard; nothing fancy

**((3.))[[#5BC2A7]] Connected Claude to my workspace** - now Claude can read and write to my databases

**((4.))[[#5BC2A7]] Tested it out** - I immediately knew this was going to be big

The whole setup? Took maybe 30 minutes. But the implications hit me right away. Claude could now actually DO stuff with my project management workflow, not just talk about it.

I need to thank Matthias Frank for his insight and the specific instructions to get Claude working with Notion MCP. Full post here: https://matthiasfrank.de/notion-mcp-setup/

## ((Setup - 2 Notion Databases: Projects & Tasks))[[#005596]]

This step can be a bit tricky, and you can go down a rabbit hole quickly, so I’ll not try to explain the “how to” in this post. Instead, let me highlight this game-changer I discovered: the "Priority Journaling System." Credit goes to Matthias Frank (not crazy about the name, but the concept? Totally transformed my workflow). And to be clear I’m talking about the journal not the man.

Here's the magic: I create a separate page for Claude to check when figuring out my weekly tasks. It is highly flexible, and I can tweak it daily, weekly, or whatever best suits my needs, and Claude uses this as its decision framework. A practical example: I have Claude automatically categorize database items with labels like home, work, or class.

Then I can pop in anytime and adjust priority percentages. Maybe this week I need 60% focus on class, 30% on work, and just 10% on home tasks. Claude then uses this breakdown when evaluating what gets assigned when.

So, is setting up Notion databases easy? My honest take - it depends, mostly on how familiar you are with Notion. The good news? With Notion AI, you can chat your way through creating a database pretty painlessly. I knocked out two completely new databases in about half an hour.

## ((The Rise Of Templates: Claude & The “PRD”))[[#005596]]

I had this 5-page PRD (Product Requirements Doc) I’m using to do a Proof of concept on something called "TaskFlow AI" (I'm building an AI project management thing – very meta). Instead of spending my entire weekend breaking it down into tasks, I just told Claude: "Extract everything from this PRD - user stories, functional requirements, UX steps, action items, all of it. Then add them to my task database with proper dates and categories."

What happened next took days for me to really process.

## ((My Tools Did My Work For Me))[[#005596]]

This wasn't just copy-paste. Claude actually understood what it was reading:

- **6 user stories for two different personas** - properly categorized
- **12 functional requirements** across three development phases - with realistic timelines
- **6 UX journey steps** that actually mapped to the user flow
- **5 edge cases** I probably would have forgotten about
- **10 milestone items** with dates that actually made sense

But here's the kicker - it didn't just dump everything in randomly. It:

- Applied my "Test" and "PRD" tags automatically
- Set priorities based on MVP vs. enhanced vs. advanced features
- Mapped my 9-month timeline to actual start and due dates beginning August 1st
- Added contextual notes so I'd remember what each task was about

### **The Results: 39 Tasks In 10 Minutes**

**Ten minutes**. That's it.

What normally takes me hours of tedious work, was done in ten minutes. And it was more consistent and thorough than I would have been doing it manually.

## ((Why This Actually Matters))[[#005596]]

I've been doing product management for years. I know all the tools, all the methodologies, and all the best practices. But this felt different because:

### No More Context Switching

I didn't have to jump between documents, copy things, remember what I was doing. Everything happened in one conversation with Claude while it was simultaneously organizing my database.

### Actually Accurate

Human error has a real impact, folks. I miss things, I'm inconsistent with naming, I make scheduling mistakes. Claude’s involvement even met my high standards.

### It Gets It

This wasn't just following instructions. Claude made smart decisions about priorities and timelines based on understanding the actual content and structure of my PRD.

### Ready To Go

The output wasn't just organized data - it was a complete project plan ready for assignment we can start executing immediately.

### Still Validating

Although I can run this in a steady state, I try to ensure continued improvement and value, so I am evaluating the following assumptions to be answered over the next quarter. Is this true?

- "Typical PRD breakdown: 4-6 hours → With Claude: 10 minutes (96% time savings)"
- "Manual process accuracy: ~85% → Claude automation: ~98%""Previous workflow: 15
- steps, 3 different tools → New workflow: 1 conversation"

## ((What We Actually Gain (Is This True?)))[[#005596]]

**Time Savings**: 6+ hours weekly back in your calendar

**Accuracy Improvement**: Eliminate human error in task breakdown

**Consistency**: Standardized formatting and categorization every time

**Completeness**: AI catches edge cases you'd typically miss

## ((What This Means For The Rest Of Us))[[#005596]]

I think we're looking at a fundamental shift in how we work. Not AI replacing us, but AI handling the tedious work so we can focus on the stuff that actually matters.

The combo of Claude's intelligence + MCP's direct tool integration creates workflows that are:

- **Way faster** - minutes instead of hours
- **More accurate** - no human oversight errors
- **Actually smart** - understands relationships and context
- **Immediately useful** - structured for action, not just organization

## ((Getting Started))[[#005596]]

If you're thinking about trying this:

**((1.))[[#5BC2A7]] Look at your repetitive tasks** - what takes forever that shouldn't?

**((2.))[[#5BC2A7]] Get MCP set up with your main tools** (Notion, Jira, etc.)

**((3.))[[#5BC2A7]] Start simple** - don't try to automate everything at once

**((4.))[[#5BC2A7]] Build from there** - once you see what's possible, you'll think of more use cases

The technical barrier is way lower than you think, but the productivity gains are substantial.

## ((The Bottom Line))[[#005596]]

What started as me just trying to convert a PRD into actionable tasks in the tools of my choice turned into a glimpse of how AI can actually change how we work.

The tools are here now. The question isn't whether this will change product management - it's how quickly we adapt to use it.

Want to try this yourself? The setup is easier than you think, and once you experience it, you'll wonder how you ever managed projects without it. Do it.

If you want help or support in your experiments, you can reach me at fletch.fletcher@improving.com and I’ll be a coach, a shoulder, or a cheerleader!
