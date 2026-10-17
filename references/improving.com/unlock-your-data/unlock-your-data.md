---
type: Reference
title: "Unlock Your Data"
resource: "https://www.improving.com/thoughts/unlock-your-data/"
author: "Olivier Aubin"
published: '2021-12-22'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Like many of us, you may have been out shopping over the last few weeks and ended up with a fistful of paper receipts. When you get home, do you carefully flatten out the receipts and place them in different folders based on your personal budget categorization, or do you throw them in a pile to be picked through later if an exchange or return is necessary?

If you’re an online merchant, do you know which products to suggest to a shopper after they’ve placed a few items in their cart? If one item isn’t found, do you know which items a shopper substituted? Are you able to track items added then removed from a cart, to make data-driven decisions about your product offerings?

![Body Image #1 - Unlock Your Data](images/ca146e79-b66d-4a31-af6c-bfc1f517794f_freestocks-spP6LqxN0-g-unsplash.jpg)

Enterprise data management has historically been like that person who carefully curates their shopping receipts when they get home so that their budget tracking and filing system is actively maintained. Similarly, the online merchant may only store a record of the final purchased items. Structured data and relational databases are designed to support these exact use cases. We design the data schema upfront for today’s business case, curate and validate incoming data, and store the information in a manner consistent with our master design.

In my previous article, [*Think Differently about Data*](https://improving.com/thoughts/think-differently-about-data), we looked at the potential of data to accelerate your business growth. As small and large enterprises alike shift to large-scale data from disparate sources, upfront design of a data schema is neither practical nor desirable. Akin to putting our shopping receipts in a pile for later use, we want to capture data now without knowing every use case, reporting requirement, or best relational model for that data.

In this article, we will look at data management and data processing concepts to enable deeper data insights.

## Ingesting Data

The term “unstructured data” is widely used, though I find it doesn’t truly capture the nuance of how data storage is evolving. Unstructured data doesn’t mean a jumble of incomprehensible characters. Each datum has structure. The data stream from a source system or IoT device will provide consistently formatted data over time. A better term may be “uninterpreted data” because it makes it clear that we are not interpreting or transforming the data prior to storage, and it leaves open the question of the level of structure in the data. Incoming data will conform to the schema inherent to the source system. However, we do not impose a destination or storage schema.

Consider the pile of store receipts. They will have different formats and text layouts, though they fundamentally contain the same information about items, prices, and payment methods. Traditional structured storage would lead to a design where each receipt is parsed and individual datum are stored in a relational database. Purchase metadata such as time of purchase, clerk name, and store location would be discarded. To ensure you can leverage the potential value in the data, you want to store it in its original form to avoid assumptions about which subset of the data may or may not be valuable.

Along with the data itself, storing metadata is important to provide broader context to future users. Metadata may include the time stamp when the information was received, identifiers for the originating system, and the schema of the incoming datum. This metadata will provide the information needed to correctly interpret the data when it is time to process it.

![Body Image #2 - Unlock Your Data](images/d3840052-4fac-4a7b-b3bd-4324304a4d2a_blake-wisz-tE6th1h6Bfk-unsplash.jpg)

## Storage Concepts

Big Data is a widely used term, but it does not have a clear definition for what constitutes as “big”. For some organizations, a few terabytes of data may represent a significant increase from their historical storage needs. Other companies hand out petabytes of storage to their developers like candy on Halloween. The concept of Big Data is less about the size of the data itself, and more about the type of data and how it is stored. Planning for the ingestion of data should focus on selecting a scalable solution to your forecasted needs for several years.

While most traditional database engines and relational models can scale for smaller organizations, they quickly reach their limit due to the centralized database engine and the need to organize and index the data in a structured way. The underlying storage may support significant growth, but the rate of ingestion and processing is limited.

A data warehouse is a popular approach to curating data for a broader user base with a specific business case in mind. This structured and curated data is accessible to many users and readily consumed by existing tools for specific reporting needs. It is not intended to support future needs in a flexible manner. A data warehouse incurs high up-front costs to implement, with intended usage patterns unclear or potentially misaligned with user needs.

This is where data lakes come into play. The scalability of this storage can be considered nearly unlimited for most organizations. Data is stored in smaller nuggets, akin to files on a hard drive. Unbounded by a centralized processing engine or update of an index, storing new data comes with very little overhead. The data itself can be JSON, Protocol Buffers, PDF documents, or any other convenient format.

Processing data, which means reading through all the individual datum in the lake, can be done using parallel algorithms as the data itself is distributed across a vast storage array in the backend of the data lake. This data processing paradigm defers the complex curation and interpretation task to a time when there is a specific and clear business need, all the while preserving a breadth of valuable data.

## Break Out of Silos

In our example of an online merchant, there should be server logs for a software developer to troubleshoot issues. These logs are likely rotated off every few days and are stored in a text-based format that isn’t intended to support complex queries. What if we streamed these logs into a data lake, storing one event for each page view or user request?

![Body Image #3 - Unlock Your Data](images/d5b7a1d4-97fd-4b20-a284-bf020fd77ca3_pickawood-gf8e6XvG_3E-unsplash.jpg)

The **explicit** data comprises timestamped events about products viewed, products added to the shopper’s cart, products removed, and completed transactions.

The **implicit** data represents shopping patterns. The aggregate data of all products and transactions can answer questions like how long a shopper spends on the e-commerce site, the churn in a cart before a transaction is completed, similar products that are compared prior to purchase, and correlated product purchases.

The silo of server logs has now been cracked open to deliver business value. From here, we can continue breaking down the silos of the business. Logistics and delivery information can be added to the data lake. Order picking and packing information could also be ingested.

## Unlock Your Data

Establishing a strategy for data ingestion, storage, and processing is essential. The focus should be on **flexibility** to support future use cases, and **scalability** over the coming years as increasingly diverse data shows up in higher volumes. A single common storage platform isn’t necessary, nor is a well-defined data schema that encompasses all datum.

Store the data in the simplest format and as close to its original format as possible. As you develop new business use cases to interpret the data, those requirements will drive and justify the additional investment in building the data processing pipeline. Reporting and data analytics that require structured data can be enabled when needed by curating the necessary subset of data from the lake and storing them in a suitable format or database.

![Body Image #4 - Unlock Your Data](images/656ef160-ba8e-4969-8df6-8e139319aeed_visual-stories-micheile-Sk5_J81j1Ks-unsplash.jpg)

Implementing data curation and analysis when it is known to have business value ensures that effort is spent only when and where it is needed. As common use cases emerge, you may find efficiencies in sharing semi-structured intermediate formats and derived values. Follow an agile approach, deferring decisions that do not need to be made now.

The most successful businesses leverage their data. Strategically growing your business and differentiating yourself means unlocking the potential of your latent information. [Reach out](https://improving.com/contact) to our team at Improving for strategic advice and project delivery.
