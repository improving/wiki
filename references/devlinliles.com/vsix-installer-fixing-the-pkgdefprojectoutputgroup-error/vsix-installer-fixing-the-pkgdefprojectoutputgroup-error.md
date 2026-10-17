---
type: Reference
title: "VSIX Installer: Fixing the PkgDefProjectOutputGroup Error"
resource: "https://www.devlinliles.com/vsix-installer-fixing-the-pkgdefprojectoutputgroup-error/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I spent about 15 hours this weekend debugging various parts of a Visual Studio Extension. It will ship soon, but the one issue that took the most time and had the fewest Google/Bing results — so I decided to post it here.

I was editing the `.vsixmanifest` file when I started getting this error:

The target 'PkgdefProjectOutputGroup' does not exist in the project.

I double-checked all my edits and corrected a couple of things. Rebuilding, cleaning — nothing worked. That is when I manually edited the project file and found that for some reason the semicolons had been URL-encoded.

**Before (broken):**

```xml
<IncludeOutputGroupsInVSIX>BuiltProjectOutputGroup%3bBuiltProjectOutputGroupDependencies%3bGetCopyToOutputDirectoryItems%3bSatelliteDllsProjectOutputGroup%3b</IncludeOutputGroupsInVSIX>
```

**After (fixed):**

```xml
<IncludeOutputGroupsInVSIX>BuiltProjectOutputGroup;BuiltProjectOutputGroupDependencies;GetCopyToOutputDirectoryItems;SatelliteDllsProjectOutputGroup;</IncludeOutputGroupsInVSIX>
```

And magically the problem goes away. Not the best error message in the world, and I am not sure why it got encoded — but if you see this error, check your `.csproj` for `%3b` in the `IncludeOutputGroupsInVSIX` element.
