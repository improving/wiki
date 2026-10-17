---
type: Reference
title: "How to Get Better Scaling via Parallel Data Transfer using Upgraded Spark Connector"
resource: "https://www.improving.com/thoughts/how-to-get-better-scaling-via-parallel-data-transfer/"
author: "Alex Le"
published: '2022-09-20'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Improving Vancouver's Alex Le wrote about the Upgraded Spark Connector between Vertica and Apache Spark in this [article](https://www.vertica.com/blog/unleash-the-power-of-vertica-and-apache-spark-using-the-upgraded-spark-connector/).

## **What is Apache Spark?**

[Apache Spark](https://spark.apache.org/) is a distributed compute engine that provides a robust API for data science, machine learning or working with big data. It is fast, scalable, simple, and supports multiple languages, including Python, SQL, Scala, Java, and R. Backed by the Apache 2.0 license and supported by a huge open-source community, it is the go-to tool for big data computations.

## Vertica and Spark

Spark fits naturally into a workflow with Vertica. For example, Vertica acts as a Data Warehouse and Spark is the “user” of the data. Common use cases for Spark include processing data from Vertica to enrich a model or transform data upstream before storing it in Vertica.

## The Vertica Spark Connector

The [Vertica Spark Connector](https://github.com/vertica/spark-connector) is an open-source project developed to facilitate data transfer between Spark and Vertica in parallel to have an advantage with scaling as compared to JDBC/ODBC when transferring large amounts of data between Spark and Vertica. Since the connector uses the Spark DataSource V2 API, it is able to integrate directly into Spark SQL query planning and optimizations. The connector also supports additional options specific to Vertica, making it the preferred way to connect Spark to Vertica.

The Vertica Spark Connector is open-source and actively maintained by Vertica to support the latest Spark 3 releases. It is considered an upgrade from the [older](https://www.vertica.com/blog/introducing-the-hpe-connector-for-apache-sparkba-p237553/) connector, which has been deprecated.

Some common usages of the connector are:

- Massive data ingestion into Vertica in parallel
- Integrate Vertica into existing Spark ETL pipelines
- Machine learning using VerticaPy and Apache Spark“

…continue reading about the Upgraded Vertica Spark connector [here](https://www.vertica.com/blog/unleash-the-power-of-vertica-and-apache-spark-using-the-upgraded-spark-connector/) and checkout the Features, Examples, and how to setup the solution.
