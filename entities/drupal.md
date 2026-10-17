---
title: "Drupal"
type: "Entity"
description: "Enterprise content management system this corpus argues for running headlessly as an API-first content source."
created: '2026-10-17'
updated: '2026-10-17'
tags: [cms, web, data]
sources:
  - "/sources/drupal-and-your-mvc-framework.md"
  - "/sources/the-evolution-of-wysiwyg-editors-from-html-builders-to-rich-text.md"
---

# Drupal

Drupal is a flexible enterprise content management system that appears in this corpus as a case for decoupling content from presentation. Its default TWIG front end constrains design, so the recommended pattern is headless Drupal: content exposed through authenticated REST endpoints to React or Vue front ends, mobile apps, and third parties.

## Headless Pattern

- Headless Drupal exposes custom REST endpoints, freeing the front end from Regions, Blocks, Views, and TWIG theming constraints, while Drupal still provides its admin and content-moderation UI.
- One source of truth removes duplicated content across environments and lets mobile apps and clients consume the same data.
- Permissions can be scoped by role or organization and down to individual nodes, passed via a user-specific API key in the request header.
- Dedicated endpoints collect front-end engagement metrics and feed ETL/BI pipelines, replacing custom database queries and stored procedures.
- Decoupling adds security through obfuscation: users cannot see the backing system, and custom error handling avoids leaking sensitive details.
- Fits the broader structured-content shift — headless CMS and API-first delivery separating content from presentation.

## Related

- [business intelligence](/concepts/business-intelligence.md) — endpoint-fed reporting
- [ETL](/concepts/etl.md) — pulling content data via REST
- [data integration](/concepts/data-integration.md) — one source feeding many consumers
