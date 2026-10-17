---
title: "Comments vs. Well-Written Code"
type: "Source Summary"
description: "Argues that well-named classes, methods, and variables make code self-documenting, so comments signal bad code."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, other, devlinliles.com]
sources:
  - "references/devlinliles.com/comments-vs-well-written-code/comments-vs-well-written-code.md"
---

# Comments vs. Well-Written Code — Summary

**Original source**: `references/devlinliles.com/comments-vs-well-written-code/comments-vs-well-written-code.md`

## Summary

Prompted by a lead who told a departing developer to "start commenting his code," Devlin Liles argues that needing comments to understand code is a red flag for bad code. He prefers well-named classes, methods, properties, and variables, which he finds far more intuitive for learning an unfamiliar codebase — especially when hunting for something specific via search. He illustrates the point with a side-by-side C# example: a poorly named, heavily commented `class1` versus a comment-free `MultiStateSalesTaxCalculator` whose names carry the meaning.

## Key Claims

- His first move on an unfamiliar codebase is collapsing comments (Visual Studio's "minimize all outlining" shortcut) and never re-expanding them.
- Learning a codebase is usually a targeted task, so a well-named member is more useful than comments when searching.
- Auto-generated names like `form1` and `class1` should never stay; type an intuitive name when adding a class.
- In the example, the well-named version needs no comments — the class name, constants, and method name document it.
- Good code documents itself.

## Relevance

Informs [code readability](/concepts/code-readability.md) and naming as the primary documentation mechanism in the [Visual Studio](/entities/visual-studio.md) era.

## Quality

Practitioner blog post by Devlin Liles, noted as originally from his old blog. Persuasive and example-driven but opinion-led; the worked example is illustrative and contains a deliberately sloppy commented version.

## Entities Mentioned

- [Visual Studio](/entities/visual-studio.md) — source of the outlining shortcut and auto-generated class names

## Concepts Covered

- [code readability](/concepts/code-readability.md) — naming and self-documenting code over comments

## Related Sources

- [VSIX Installer: Fixing the PkgDefProjectOutputGroup Error](/sources/vsix-installer-fixing-the-pkgdefprojectoutputgroup-error.md)
