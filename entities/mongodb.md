---
title: "MongoDB"
type: "Entity"
description: "Document database used in this corpus for deployment automation and as the setting for a SCRAM SHA-256 authentication deep dive."
created: '2026-10-17'
updated: '2026-10-17'
tags: [database, security, platform]
sources:
  - "/sources/making-sense-of-scram-sha-256-authentication-in-mongodb.md"
  - "/sources/platform-engineering-companies.md"
  - "/sources/how-to-fail-at-platform-engineering.md"
---

# MongoDB

A document database that appears in this corpus both as a component of a large deployment-automation case and as the subject of a detailed authentication explainer. It is treated as an example of a service that platform teams must keep current and secure, not as a data-platform centerpiece.

## Authentication

- SCRAM SHA-256 is the default authentication mechanism in MongoDB and suits applications where databases hold sensitive information.
- Authentication uses four messages: client-first (username and a client nonce), server-first (salt, iterations, and a server nonce), client-final (client proof), and server-final (server proof).
- The client proof is derived through a salted password hash (HMAC-SHA-256 iterated `iterations` times), a client key, the auth message, a stored key, and a client signature, XORed with the client key.
- The server can store the salted password hash instead of the raw password, and the mechanism guards against message replay.

## In Platform Delivery

- A McKesson case automated deployment of its Drug Serialization Repository across 29 distribution centers with GitHub Actions, Kubernetes, Confluent Kafka, and MongoDB, cutting deployment time per location from 4–6 hours to 33 minutes.
- Stagnant platforms fall behind when they do not keep current service versions available; MongoDB is cited as the kind of service whose version currency matters.

## Related

- [application-security](/concepts/application-security.md) — secure authentication mechanisms
- [secrets-management](/concepts/secrets-management.md) — storing a salted hash rather than the raw password
- [platform-engineering](/concepts/platform-engineering.md) — internal platforms that must keep services current
