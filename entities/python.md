---
title: "Python"
type: "Entity"
description: "The dominant language for data and AI work, used across ETL pipelines, Spark jobs, and cloud data platforms."
created: '2026-10-17'
updated: '2026-10-17'
tags: [language, data, ai]
sources:
  - "/sources/key-fundamentals-of-ai-development.md"
  - "/sources/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md"
  - "/sources/single-node-kubernetes-on-raspberry-pi.md"
  - "/sources/unveiling-the-future-of-ai-at-google-cloud-next-24.md"
  - "/sources/business-transformation-through-microsoft-fabric-new-era-of-data.md"
---

# Python

Python is the dominant language for data and AI work in this corpus, appearing wherever pipelines, machine learning, or notebooks are discussed. It is treated as the default language of AI development and the glue of data engineering.

## Where It Appears

- Named among the common AI languages (with Java and C++), used with frameworks such as TensorFlow, PyTorch, and Keras.
- Runs PySpark jobs in a sub-second, 10TB/day on-prem ETL pipeline built on Kafka, Spark Structured Streaming, and Hive.
- Google's JAX is a NumPy-based Python framework for accelerator-oriented array computation, claimed to outperform TensorFlow and PyTorch for training speed.
- Microsoft Fabric lakehouses are built through Spark notebooks in Python/R, and Azure Synapse notebooks support Python, C#, R, and SQL over Spark.
- Even a minimal ARM64 Kubernetes sample pod on a Raspberry Pi used `arm64v8/python:3.6`.

## Related

- [Java](/entities/java.md) — the other common enterprise and AI language
- [Apache Spark](/entities/apache-spark.md) — distributed engine that runs Python (PySpark)
- [Apache Hive](/entities/apache-hive.md) — the query layer at the end of the Python-fed pipeline
- [AI literacy](/concepts/ai-literacy.md) — understanding the tools built in Python
- [Microsoft Fabric](/entities/microsoft-fabric.md) — platform whose notebooks run Python
