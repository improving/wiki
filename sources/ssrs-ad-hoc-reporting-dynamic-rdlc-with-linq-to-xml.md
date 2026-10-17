---
title: "SSRS Ad-Hoc Reporting: Dynamic RDLC with LINQ to XML"
type: "Source Summary"
description: "A technique for building ad-hoc SSRS reports by loading a blank RDLC and injecting sub-report nodes dynamically with LINQ to XML."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, legacy-dotnet, devlinliles.com]
sources:
  - "references/devlinliles.com/ssrs-ad-hoc-reporting-dynamic-rdlc-with-linq-to-xml/ssrs-ad-hoc-reporting-dynamic-rdlc-with-linq-to-xml.md"
---

# SSRS Ad-Hoc Reporting: Dynamic RDLC with LINQ to XML — Summary

**Original source**: `references/devlinliles.com/ssrs-ad-hoc-reporting-dynamic-rdlc-with-linq-to-xml/ssrs-ad-hoc-reporting-dynamic-rdlc-with-linq-to-xml.md`

## Summary

A hands-on .NET post solving SSRS's inflexibility in application-integration scenarios, where datasets and fill/get methods otherwise have to be hard-coded per report. The approach starts from a blank RDLC with a templated header and footer, loads it into an `XDocument` via a file stream, locates the body's `ReportItems` node with [LINQ](/entities/linq.md) to XML, and injects new node packages (tables, sub-reports, graphs) before packaging the document back to a `MemoryStream` and handing it to the `ReportViewer` control exactly like a static report.

## Key Claims

- Loading preset report segments dynamically into a report definition avoids hard-coding datasets and fill/get methods per report.
- The `ReportItems` node inside the `Body` is the insertion point for the report's guts; a namespace-qualified `XElement` subtree adds tables, sub-reports, or graphs.
- The memory-stream position must be reset to zero before handing off, or the read starts at the end and produces an invalid RDLC error.
- Sub-report width changes with paper orientation, `Top` shifts by how many reports are inserted, and height is set to a quarter inch because sub-reports auto-expand.
- Sub-report data sources are supplied in the `SubreportProcessing` event handler; errors are handled in the `ReportError` handler.

## Relevance

A legacy .NET implementation technique for dynamic reporting; it demonstrates LINQ to XML manipulation of a document format, not an architectural pattern.

## Quality

Practitioner blog post by Devlin Liles. Includes a complete, copy-pasteable code sample with the full `_Default` page class; its caveat is that it is a narrow how-to with no discussion of limits or alternatives.

## Entities Mentioned

- [LINQ](/entities/linq.md) — used to XML to locate and inject report nodes.

## Concepts Covered

- None.
