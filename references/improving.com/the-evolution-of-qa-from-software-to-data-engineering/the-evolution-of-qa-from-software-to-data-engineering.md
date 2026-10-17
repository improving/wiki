---
type: Reference
title: "The Evolution of QA: From Software to Data Engineering"
resource: "https://www.improving.com/thoughts/the-evolution-of-qa-from-software-to-data-engineering/"
author: "Federico Silva"
published: '2025-10-08'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

In modern AI, what differentiates one model from another is not mainly the architecture or the dataset size, but the *quality* of the data. As the saying goes, *garbage in, garbage out*. No algorithm can compensate for flawed inputs. From analysts to ML engineers, everyone depends on clean, consistent, and reliable data.

Quality assurance is now central to this work. It validates pipelines, transformations, and persistence so that data scientists and engineers can trust the outputs. In this sense, *data quality engineering* has become the foundation of all data-driven systems, from dashboards and reports to predictive models and AI applications.

## **How QA Has Entered Data Engineering**

### **Beyond Frontend and Backend**

Traditional QA in software engineering focused on front-end interactions and backend APIs, typically moving from user interface to API to database. But event-driven architectures and platforms such as Kafka have expanded the scope of QA to an almost unrecognizable level. Testers now verify that producers send valid messages with the correct schemas, that consumers process events in the right order, that lag and retries are monitored, and that downstream persistence results in usable records. These concerns are the daily work of data engineers, and QA has clearly already crossed into that field.

### **QA in the AWS Ecosystem**

Cloud platforms are now an essential part of QA. In [Amazon Web Services](https://aws.amazon.com/free/?trk=48ebaf74-0ade-44c7-b8c2-12a0e7718d21&sc_channel=ps&ef_id=CjwKCAjw6P3GBhBVEiwAJPjmLgpYie8GjcnCAG8p0LSQXcI3EcPs9fzRoa7go8fj4bsRKHlkN10ZsxoC-xoQAvD_BwE:G:s&s_kwcid=AL!4422!3!651751059777!e!!g!!amazon%20web%20services!19852662197!145019195737&gad_campaignid=19852662197&gbraid=0AAAAADjHtp9fHV1y8Bc0YYgIuHFvmvcXm&gclid=CjwKCAjw6P3GBhBVEiwAJPjmLgpYie8GjcnCAG8p0LSQXcI3EcPs9fzRoa7go8fj4bsRKHlkN10ZsxoC-xoQAvD_BwE), testers validate ingestion, object creation, and lifecycle rules in S3. They confirm correct message delivery in SQS, check that Lambda functions produce the right outputs and perform the right transformations, and validate persistence and query results in DynamoDB. They also rely on CloudWatch to detect failures or lag through metrics and logs. Each of these services is part of the broader story of data correctness: delivery, transformation, and observability at every step.

### **QA in Data Lakes, Warehouses, and Pipelines**

Modern QA extends across the entire data lifecycle. In data lakes, it validates ingestion from multiple sources, schema conformity, and partitioning. In ETL/ELT pipelines, it ensures that transformations are correct, idempotent, and free from corruption. In data warehouses, it checks that aggregated and structured outputs match expectations.

Even deceptively simple extract-and-load pipelines can fail when hidden transformations occur. Encryption may produce unreadable outputs if keys or formats are mismanaged. Compression and decompression can break integrity if algorithms differ. Encoding mismatches can introduce subtle errors. QA must therefore validate not only the movement of data but also its integrity at every transformation point.

![Image 1 - The Evolution of QA: From Software to Data Engineering ](images/CORRECT_BLOG_IMAGE_SIZE__12_.png)

## **Reconceptualizing QA as Data Quality Engineering**

### **Functional Testing as Data Testing**

My claim is that functional testing has always been about data correctness. Look at it in this way: all software instructions are reduced to the four CRUD operations: Create, Read, Update, Delete. A form that does not persist indicates a Create defect. A search that produces wrong results is a Read defect. An edit that does not save is an Update defect. A delete action that leaves ghosts is a Delete defect. **Almost every functional bug is ultimately a *****data***** bug.**

Even classical API testing can be understood as pipeline validation. The server queries the database to extract data, serializes it into a chosen format, and delivers it to the client. This is essentially an ETL process. This exemplifies how testers have always been validating data pipelines, even when they did not describe them in those terms.

### **Non-Functional Testing as Quality on Top of Data**

Performance and security do not directly alter data, but they protect and support it. Data correctness, consistency, and completeness form the base of quality. Performance and security sit on top, ensuring that correct data remains reliable and usable.

### **Conclusion**

QA has always been about data. What has changed is the scope. Once limited to CRUD validation, it now extends to event streams, cloud services, and machine learning pipelines. Functional correctness ensures reliable data, while non-functional testing secures and scales it.

The future of QA is inseparable from data engineering. Testing is no longer just about code quality, but about data pipelines, transformations, and reliability. Those who fail to recognize this shift will lag behind the industry standards. Partner with our world-class data engineers and turn QA into a true driver of growth and reliability. Let’s build the next generation of data systems together. [Reach out today!](https://improving.com/contact)
