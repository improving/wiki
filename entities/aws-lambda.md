---
title: "AWS Lambda"
type: "Entity"
description: "AWS serverless compute, used in Improving's writing as the runtime for a metrics connector."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cloud, serverless, aws]
sources:
  - "/sources/introducing-the-amazon-timestream-for-liveanalytics-prometheus.md"
---

# AWS Lambda

AWS Lambda is AWS's serverless compute service. It appears in this corpus as the deployment target for the Amazon Timestream for LiveAnalytics Prometheus Connector, chosen so the connector scales without a server to manage. Support for the term is thin here, so this page stays deliberately short.

## Key Claims

- The [Amazon Timestream](/entities/amazon-timestream.md) Prometheus Connector can run as a Lambda function behind API Gateway, created by a one-click CloudFormation stack in about five minutes.
- Lambda is chosen for serverless scalability: there is no server to provision or patch for the connector workload.
- The connector can alternatively run locally or in Docker, so Lambda is one deployment option among several.

## Related

- [Amazon Timestream](/entities/amazon-timestream.md) — the database the Lambda-hosted connector writes to
- [observability](/concepts/observability.md) — the monitoring workload being served
- [infrastructure as code](/concepts/infrastructure-as-code.md) — the CloudFormation deployment
- [AWS](/entities/aws.md) — the platform vendor
