---
title: "Amazon Timestream"
type: "Entity"
description: "AWS time-series database with a Prometheus connector that turns it into a scalable remote store for metrics."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, observability, cloud, aws]
sources:
  - "/sources/introducing-the-amazon-timestream-for-liveanalytics-prometheus.md"
---

# Amazon Timestream

Amazon Timestream is AWS's managed time-series database. Improving's writing covers it through the Timestream for LiveAnalytics Prometheus Connector, which lets [Prometheus](/entities/prometheus.md) use Timestream as remote storage and escape its local disk limits.

## Key Claims

- The connector translates between Prometheus and Timestream using Prometheus' `remote_write` and `remote_read` protocols.
- It can run locally, in Docker, or as an [AWS Lambda](/entities/aws-lambda.md) function; a one-click CloudFormation stack creates the Lambda behind API Gateway and IAM roles in about five minutes.
- Stated benefits include serverless scalability, SQL-based querying, correlation with other Timestream data, and lower storage costs for longer retention.
- Prometheus requires an IAM access key rather than a role because of a Prometheus limitation, and TLS is not covered by the walkthrough but is recommended for production.
- [Grafana](/entities/grafana.md) is named as a query and visualization option over the stored metrics.

## Related

- [Prometheus](/entities/prometheus.md) — the monitoring system using Timestream as remote storage
- [observability](/concepts/observability.md) — monitoring data at scale
- [metrics logs traces](/concepts/metrics-logs-traces.md) — time-series metric storage
- [infrastructure as code](/concepts/infrastructure-as-code.md) — the CloudFormation one-click deployment
