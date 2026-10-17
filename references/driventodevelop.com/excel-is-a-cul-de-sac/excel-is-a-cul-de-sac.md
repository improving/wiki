---
type: Reference
title: "Excel is a Cul-de-sac"
resource: "https://driventodevelop.com/2013/02/28/excel-is-a-cul-de-sac/"
author: "David O'Hara"
published: '2013-02-28'
fetched: '2026-10-17'
tags: [blog, driventodevelop.com]
---

In my recent transition, I've had to become even more intimate with Excel as a tool of my job. Previously I've used Excel
in crazy ways, as a data source for an ODBC connection or a pass thru between disconnected services, but now it's
something to run the business on. That's a knife that cuts both ways though.

## The Current State

Excel is an extremely useful app and the learning curve on it is fairly low. Things you would typically do are easily
found via Google and most C-level folks have been mashing up formulas for a good hunk of time. I can safely say there
are some companies of significant size that are run off of Excel spreadsheets that are passed around via email
(don't even get me started on the lack of Dropbox use). It works fairly well and, while seemingly creating only a small
amount of overhead, gets the job done. But there's a big problem underlying this behavior.

## The Problem

New people. Ok, so the new people aren't the actual problem but they surface the start of the problem. When data is pulled from a
source system into Excel it can be sliced, diced, and manipulated until it says what you need it to but that's it. It's
done. And it was almost always manual. Rarely is the manipulation reproducible by anyone other than the person who just
did it because that would require the use of macros and VBScript and stuff that only developers really grok. Strike #1.

Manipulated data is dead in Excel, like those dead tree requirements docs we have all decided were a less
than ideal way to do things. You can't pull new data into the existing spreadsheet and have it follow the transformation to add
to the output. No, instead you pull new data and start back at square one. Strike #2.

Did you want to use that data in some other system or feed it back into the one that it originally came from? No joy
here. The data cannot be consumed in as easy a fashion as it was put into Excel. Sure you can get a developer to monkey
up an ODBC connection like I did before but that's not something most executives are going to be able to pull off.
Maybe they're able to string together a set of Excel sheets that refer to each other and use the data between them but
that's a tangled and fragile web. And given the prior two issues, we know what sort of overhead maintaining that is
going to be when it comes time to update with new data. Strike #3.

## Conclusions

I'm not against using Excel, heck, I do it on a pretty regular basis. I'm against it's overuse; the crutch that it
becomes when folks just want a one off thing (until it isn't), for just a few people (until there's more), and won't
need again (until they do). When you need something more, step up and move out of your comfort zone, find a tool that
supports what you need and isn't a three strike offender.

# Excel is a Cul-de-sac

[
![David O'Hara](images/Headshot---current.jpg)
](https://driventodevelop.com/author/david/)

[David O'Hara](https://driventodevelop.com/author/david/)

28 Feb 2013

[thoughts](https://driventodevelop.com/tag/thoughts/)
