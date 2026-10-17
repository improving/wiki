---
type: Reference
title: "CodeRush vs. ReSharper: Six Months Later"
resource: "https://www.devlinliles.com/coderush-vs-resharper-six-months-later/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

*Originally from my old blog. Note: I have since changed my opinion on some of these points.*

It has been a crazy journey of bouncing back and forth between these two tools, but I wanted to loop back and document it.

## Community / Plugins

- **CodeRush** — This tool has a ton of merit. It has a great community that seems to be slightly more active in extensions and plugins than ReSharper. There are also some plugins in this community that I believe should be part of the core product.
- **ReSharper** — The community is there and has a decent number of plugins. There were none that I "had to have." I am currently writing a plugin to address what I perceived as a lack in the templates.

## Usability

- **CodeRush** — I am of two minds on this. One says that the fact that CodeRush tries not to override existing Visual Studio shortcuts is nice when I am on a machine that doesn't have it — I'm not lost. The other says that is a rare case easily outweighed by wanting a single place to go for refactorings.
- **ReSharper** — I have found the ReSharper approach of a single set of key bindings that *after prompt* take over fits me better. They have also cleaned up some of the rough edges on the built-in Visual Studio features — the Extract Interface dialog is a great improvement.

## Code Generation

- **CodeRush** — CodeRush just wins this one. The mnemonic templates that are context-aware are a huge win. Being able to generate a property with the same two keystrokes but have the generated code differ based on whether my class implements an interface is powerful.
- **ReSharper** — They have good templates, but they fall short of the power of CodeRush's templates. I use Live Templates heavily but saw a gap. I am working on a plugin to bring mnemonic template behavior to ReSharper.

## Refactoring

- **CodeRush / Refactor Pro** — They have all the expected things, but it feels a little disjointed with the bookmark navigation. Hitting Escape moves me around in code and I never got used to it. It may have needed more time, but after several months it still got in my way.
- **ReSharper** — All the expected things again, but I love the ability to dive deep into code with a couple of keystrokes. ReSharper makes navigation feel like a normal part of the workflow instead of something you have to learn separately.

## File Generation

- **CodeRush** — This is the one major gap in CodeRush's core product. The ability to generate a new file (class, interface, enum, struct, or folder — especially folder) from the solution explorer, name it, and have the file created immediately. This seems like a rather large missing use case.
- **ReSharper** — Has everything listed above, and when combined with live file templates I can quickly drop in large chunks of functionality without having to restructure them as a separate step. This was a game changer for me.

## Customer Support / Install / Licensing

- **CodeRush** — Unified installer with account-based licensing. Enough said. This is how it should look.
- **ReSharper** — Email and phone-based support is getting better, but I would still love to see an automated over-the-wire license model.

## Conclusion

**ReSharper** — This decision came down to ease of refactoring, the power of the templates, my current plugin work, and the file/solution-level refactorings.

I have been and will continue to use and recommend ReSharper for the foreseeable future. But one thing this exercise made clear is that I need to re-evaluate often to make sure I am using the best tool available.

I want to make it clear that both are great products from great companies. I have both because they were kind enough to give me copies for free in exchange for honest feedback. My default position remains: "I don't care which one you use, but use one of them." It will make you faster and help you write better code.
