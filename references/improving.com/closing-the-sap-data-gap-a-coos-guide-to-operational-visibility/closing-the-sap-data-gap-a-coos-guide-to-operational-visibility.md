---
type: Reference
title: "Closing the SAP Data Gap: A COO’s Guide to Operational Visibility"
resource: "https://www.improving.com/thoughts/closing-the-sap-data-gap-a-coos-guide-to-operational-visibility/"
author: "Sean Antonello"
published: '2026-05-01'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

A COO’s job is to keep the business running. That means seeing problems coming, not just responding to them. But in a lot of organizations, operational intelligence is still locked up in people’s heads or in systems that don’t talk to each other. The result is a leadership team that is perpetually reactive, making decisions based on institutional knowledge instead of data.

That gap has a real cost, and it shows up most clearly in organizations that run SAP.

### **Where Operational Decisions Break Down**

Even organizations that run wall-to-wall SAP still have operational systems that are non-SAP. That data lives in those systems, or it gets pushed into a third-party tool, a data lake, or a data warehouse. The challenge for a COO is figuring out how to merge that data and understand how an operational decision is actually translating across to finance. Without that connection, visibility is limited and joining the data is a slow, manual exercise.

The cost of that gap goes beyond frustration. When pricing or procurement decisions are still driven by institutional knowledge rather than data, organizations become reactive. The biggest impact shows up in margin erosion. When you don’t have visibility into how procurement decisions are affecting finance, you’re leaving money on the table. And if competitors have more information available, they’re going to act more quickly.

There are also hidden people costs. An analyst spending half their day taking data, manipulating it, and trying to join it manually is not an edge case. It’s a pattern that plays out across organizations every day.

### **What Solving It Actually Looks Like**

In a recent engagement focused on price optimization, Improving worked with a client that had operational data living in a Databricks Lakehouse and financial data living in S/4HANA. The goal was to marry those two data sets together in a way that gave the business real-time access to both.

That was done using SAP Business Data Cloud, which enabled a zero-delta copy approach. Rather than moving data through batch jobs, BDC shares data directly, giving users real-time access without creating a separate, stale copy of the information. From there, Databricks was used to run AI and large language modeling to predict where price optimization would be most impactful.

### **Why a Dashboard Isn’t Enough**

A dashboard gives you a window into what’s happening. But a window doesn’t let you act. The typical pattern looks like this: an analyst or COO opens a dashboard, sees an anomaly, logs into a separate system to investigate, makes a fix, waits for the process to rerun, then checks the result. It sounds manageable, but there’s a lot of movement happening in that workflow, and each step introduces delay.

Building an application directly in BTP changes that dynamic. Instead of jumping between systems, a user can take action from the same place where they’re seeing the anomaly, and that action pushes directly back into S/4HANA without the user having to navigate there themselves. The insight sits inside the workflow, not beside it. That distinction is the difference between a reporting project and an actual transformation initiative.

This applies across operational activities, not just pricing. Procurement is another clear example. Anywhere people are currently jumping out of one system and into another to address something, embedding that intelligence into the workflow removes the friction and creates a more structured way to operate.

### **How Decisions Change When Visibility Improves**

When a COO has this kind of visibility built directly into their applications and reporting layer, the basis for decisions changes. They stop relying on stale data and institutional knowledge. Instead, they use AI modeling to make proactive decisions, see where optimization opportunities exist, and understand the impact those decisions will have on the financial statements in a single click.

### **How Long Does It Take?**

The honest answer is that it depends on where the complexity lives. The right starting point is an assessment to identify where the heaviest challenges are and which use cases will deliver the most value. From there, a roadmap of six, twelve, or eighteen months can get an organization operating in a much more proactive way.

Specific use cases, like the procurement example, can be delivered in ten to twelve weeks. Standard content such as Improving’s pre-configured portals that live inside BTP can help accelerate early wins. Within twelve to eighteen months, an organization can look quite different, with reporting and analytics, planning and embedded applications working together rather than in parallel.

### **Ready to Move from Reactive to Proactive?**

Improving helps COOs and operations leaders connect SAP and non-SAP data, embed intelligence into the workflows where decisions actually happen, and build the operational visibility needed to stop reacting and start leading. If your team is still stitching data together manually, [let’s talk about where to start. ](https://improving.com/contact)
