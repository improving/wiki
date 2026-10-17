---
type: Reference
title: "Why Your Power BI Reports Are Slow — And How a Custom Connector with Query Folding Can Fix It"
resource: "https://www.improving.com/thoughts/why-your-power-bi-reports-are-slow/"
author: "Steve Lord"
published: '2025-04-30'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Have you ever been on vacation and realized you packed too much stuff? The kind of stuff you take just in case, but you know you’ll never use?

You’ve arrived at your destination. You’ve waited ages for your cases to come off the carousel. You had to lug them across the parking lot to your transportation, while others breeze by with their hand luggage and then get the best spot on the bus. It is only a beach holiday after all, and not a world cruise! Then you get to your resort and try to find your swimwear and towel, remembering it was packed at the bottom. If only you had been better organized before leaving home!

Packing and folding problems exist in [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi) too, and similarly, slow things down.

![Asset - Image 1 - Why Your Power BI Reports Are Slow — And How a Custom Connector with Query Folding Can Fix It](images/AdobeStock_491802655.jpeg)

### Folding solutions

Power BI query performance can be a bit like figuring out what to take on vacation and the order to place everything in the bag. The concept in Power BI of only taking what you need is called Query Folding. It’s the art of making your data smaller. Query Folding leads to better performance and lower costs.

Why? Because Query folding will push down transformations, aggregations, and joins to the data source, where they can be executed more efficiently. That’s where you’ve set up indexes and partitioning already. It makes sense to let your data source do the heavy lifting.

Right? This, in turn, reduces the load on Power BI and improves processing speed because less data is received and prepared by Power BI.

### Limitations of standard connectors

Standard connectors and database drivers are ok for normal, simple use cases. However, when dealing with large or complex data sources, standard connectors and drivers may not support query folding. Instead, Power BI will try to do it for you, and it will do that by pulling all your data across. This will put more memory and processing load on Power BI.

Power BI may not know what type conversions your data source can support, and once again convert it for you, possibly incorrectly. Further, your data source interface may be an API, for which there is no connector.

This is where custom connectors and drivers provide a solution to better performance and data conversion.

### Use case with a painful plot twist

Consider a sales report. What I really need is a report of total sales by month and by region, period.

I start creating the report, and I’m going to do it all in Power BI. Why not? I don’t need to think too much and I’ll test it with a few rows of data. Life is good! So, maybe I do need that entire measures table in case I later want to calculate sales by day. Or I need the stores table so I can produce sales by individual store.

*Wait! *

Once I scale the data and see how slowly my report is running, I realize, with a little foresight, pulling all those millions of rows into a Power BI capacity and aggregating there wasn’t such a good idea.

Maybe I can get the data source to do that crunching for me? Just give me the 12 rows of month-end sales totals by region.

We probably have a really cool SQL script we run directly on the data source already, and know it works. Now I have to translate that into M language! Is Power BI going to do that as efficiently? Plus, I am consuming vast amounts of storage, which I am paying for twice, once in my data source and again in Power BI. Why would I do that?

![Data Analysis and Visualisation with Microsoft Power BI - Thumbnail](images/BI-1.jpeg)

### A Custom Connector Solution

Data Folding seems like a great idea. How can I determine what gets pushed down?

That’s the tough part. Power BI needs to know what it can push down to the data source and what it has to do for you. How does it do that? The connector and the database driver work in tandem to tell Power BI what the data source can support: aggregations, joins, type conversions, etc.

In addition, some queries get too complex to write in M language. If it’s easier to write a native query, then the connector has to support that, but not all do.

A custom connector with a compatible database driver can provide a solution. It provides full control over interactions with the data source. It can optimize how data is fetched. It can provide native query support.

### Conclusion

At Improving, we write custom connectors and database drivers. We can drill down to your data source, but we don’t stop there. We can implement data sources too.

Using Power BI custom connectors with Query Folding, native query support, and compatible drivers can result in faster reports and lower costs than off-the-shelf solutions.

Now it's time to grab that small bag, get that prime spot on the bus, and be first on the beach!

To learn more about Query Folding and how it can optimize your Power BI reports, [contact Improving today](https://www.improving.com/contact)!

You can also check out these references:

**[*https://learn.microsoft.com/en-us/power-query/query-folding-basics*](https://learn.microsoft.com/en-us/power-query/query-folding-basics)* *

**[*https://learn.microsoft.com/en-us/power-query/native-query-folding*](https://learn.microsoft.com/en-us/power-query/native-query-folding)* *
