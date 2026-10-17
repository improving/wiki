---
title: "VSIX Installer: Fixing the PkgDefProjectOutputGroup Error"
type: "Source Summary"
description: "A Visual Studio extension build error traced to URL-encoded semicolons in the .csproj IncludeOutputGroupsInVSIX element."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, legacy-dotnet, devlinliles.com]
sources:
  - "references/devlinliles.com/vsix-installer-fixing-the-pkgdefprojectoutputgroup-error/vsix-installer-fixing-the-pkgdefprojectoutputgroup-error.md"
---

# VSIX Installer: Fixing the PkgDefProjectOutputGroup Error — Summary

**Original source**: `references/devlinliles.com/vsix-installer-fixing-the-pkgdefprojectoutputgroup-error/vsix-installer-fixing-the-pkgdefprojectoutputgroup-error.md`

## Summary

While editing a `.vsixmanifest` for a Visual Studio extension, the author hit the build error "The target 'PkgdefProjectOutputGroup' does not exist in the project." Rebuilding and cleaning changed nothing. Manually inspecting the project file revealed that the semicolons separating output groups in `IncludeOutputGroupsInVSIX` had been URL-encoded as `%3b`, so MSBuild could no longer parse the target list. Replacing the encoded separators with literal semicolons fixed the build immediately.

## Key Claims

- The error message is misleading: the "missing target" is a symptom of a malformed `IncludeOutputGroupsInVSIX` value, not a genuinely absent project target.
- The root cause was URL-encoded semicolons (`%3b`) inside the `.csproj` element.
- Fix: change `%3b` back to `;` in `IncludeOutputGroupsInVSIX`.
- The author spent about 15 hours debugging the extension and found very few search results for this error.

## Relevance

A concrete debugging note for [Visual Studio](/entities/visual-studio.md) extension packaging, useful when MSBuild target-resolution errors point away from the real cause.

## Quality

Practitioner blog post by Devlin Liles. Short, first-hand, single-case fix with an exact before/after snippet; the author admits the cause of the encoding is unknown.

## Entities Mentioned

- [Visual Studio](/entities/visual-studio.md) — the IDE whose extension packaging failed

## Concepts Covered

- None.

## Related Sources

- [CodeRush vs. ReSharper: Six Months Later](/sources/coderush-vs-resharper-six-months-later.md)
- [Comments vs. Well-Written Code](/sources/comments-vs-well-written-code.md)
