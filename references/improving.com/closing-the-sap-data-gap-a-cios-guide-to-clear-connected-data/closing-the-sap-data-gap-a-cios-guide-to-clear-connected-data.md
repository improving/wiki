---
type: Reference
title: "Closing the SAP Data Gap: A CIO’s Guide to Clear, Connected Data"
resource: "https://www.improving.com/thoughts/closing-the-sap-data-gap-a-cios-guide-to-clear-connected-data/"
author: "Sean Antonello"
published: '2026-05-01'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Most CIOs are navigating the same tension right now. There’s pressure to modernize, add AI capability, and get more out of SAP data, but there’s always the risk of destabilizing the core systems the whole business runs on. It’s a real tension, and the way organizations typically try to resolve it often makes things worse.

### **The Most Common Mistake**

Historically, organizations built custom processes directly inside their core ERP. In the ECC era, that was essentially the only option. With S/4HANA, there’s a different model available, one built around the concept of clean core, but many organizations are still defaulting to old patterns.

The problem shows up in one of two ways. Either customizations are still being built directly inside core ERP, or they’re being built in a completely independent system that has no real connectivity to SAP. Both create the same outcome: teams spending significant time managing integration and making disconnected processes work together.

### **What Clean Core Actually Means**

Clean core is talked about a lot right now, but what it means in practice is straightforward. Customizations shouldn’t live inside core ERP. They slow things down, make systems more cumbersome, and most visibly, they make upgrade cycles long and painful. The more customization sits inside core, the more work an upgrade requires.

SAP’s recommended approach is to build those customizations in BTP, the Business Technology Platform. Everything in the SAP Business Suite, including S/4HANA and Business Data Cloud, sit on top of BTP. It enables integration, custom and no-code app development within the SAP ecosystem, and standard connections between systems.

The practical benefit is significant. When you develop in BTP rather than in core, an S/4 upgrade doesn’t touch those processes at all. You reduce the technical debt inside your core ERP, simplify upgrade cycles, and avoid the freezes that prevent users from self-serving while an upgrade is in progress. There’s also a licensing angle: if users are accessing S/4 only because a custom workflow lives there, moving that workflow to BTP removes the need for those seats entirely.

### **A Real Example: The xi.Orion Vendor Portal**

Improving built a portal called xi.Orion to support vendor and supplier relationships. The scenario it addresses is common: customer-facing teams fielding a constant stream of questions from vendors about invoice payment status, purchase requisitions, and purchase orders. It’s a high-volume, low-value interaction that consumes significant internal bandwidth.

xi.Orion was built inside BTP, following the clean core approach. Vendors can self-serve, load a purchase requisition (PR) or purchase order (PO), use Joule, SAP’s AI, to ask about PR or PO approval status, and check when invoices are set to be paid. When a vendor submits a PR directly through the portal, it initiates an approval workflow without those external users ever touching core ERP. That also creates a more secure environment since vendors have no access to the internal system itself.

The back-and-forth email process is replaced. The burden on internal teams is reduced. And none of it required customizing S/4HANA.

### **Where Fabric, Databricks, and Snowflake Fit**

Even SAP shops don’t run wall-to-wall SAP. SAP has recognized that, and the ecosystem has opened up significantly. Business Data Cloud now includes standard connectors to non-SAP systems for operational data, with direct access to Databricks, Snowflake, and Microsoft Fabric. A zero-delta copy approach for Fabric is expected to reach general availability in the second half of this year.

What this means for a CIO is flexibility. You can keep your SAP investment intact, preserve the semantic layer and the master data relationships that live inside SAP, and still join that information with operational data from outside the SAP network. That combination of rich, business-centered SAP data with external operational data has historically been difficult to achieve. The current tooling is making it much more accessible.

### **What to Do If You’re Mid-Migration**

For organizations in the middle of an S/4HANA migration, there are two things worth addressing before the migration gets too far along.

The first is clean core. It might feel like something to deal with later, but it’s often more cost effective to move custom processes to BTP during the migration rather than after. Identifying the heaviest processes early and planning to move them out of core before go-live is a better use of the moment.

The second is data and analytics, which tends to be treated as an afterthought in ERP migrations. Organizations go live and then discover their users have no reports or defined reporting strategy. Defining the data and analytics program early, before go-live, means users are ready with the reporting they need from day one.

### **What Eighteen Months of Progress Looks Like**

With a clear roadmap, an organization eighteen months into this work would have S/4HANA in place with BTP services handling integration, replacing older middleware like PI/PO. Clean core philosophy would be in practice, with custom processes moved to BTP applications. Business Data Cloud would connect operational data from a data warehouse or lake of choice to SAP data, with SAP Analytics Cloud on top for both reporting and forecasting.

The result is self-service reporting across the organization, planning and forecasting that runs in a more automated way, and a materially cleaner core. The goal is to complete the loop: clean data in, intelligence out, and nothing broken in the middle.

### **Ready to Start?**

Improving helps CIOs navigate SAP modernization, adopt clean core practices, and build a connected data landscape that supports both operations and analytics. Whether you’re mid-migration or looking at what comes next, [let’s talk about where to begin. ](https://improving.com/contact)
