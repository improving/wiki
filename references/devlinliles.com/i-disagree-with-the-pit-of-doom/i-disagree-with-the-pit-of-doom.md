---
type: Reference
title: "I Disagree with the Pit of Doom"
resource: "https://www.devlinliles.com/i-disagree-with-the-pit-of-doom/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I got a link from a friend to Ayende's post [Architecting in the Pit of Doom: The Evils of the Repository Abstraction Layer](http://ayende.com/blog/4784/architecting-in-the-pit-of-doom-the-evils-of-the-repository-abstraction-layer?ref=devlinliles.com). I read it and can see the points made, but I disagree with it in multiple places. So in the interest of starting a great conversation with some really smart people like Ayende and Amir Rajan, here are my counterpoints.

I am going to skip over the overview that Ayende does in the first few paragraphs. The architecture overview is fairly on point and accurate.

---

## 1. "The whole purpose of a repository is to provide an in-memory collection interface to a data source"

I would disagree about the purpose of the repository abstraction. The purpose is *both* to give an in-memory collection interface to data *and* to give a testable abstraction over data. I understand that NHibernate and Entity Framework both give an in-memory collection-based abstraction, but they are both opinionated in how they structure the unit of work and data access. If I want to deal with data in a way that abstracts the base implementations away, I cannot take those opinions.

I understand that the normal argument is that I should choose a data access architecture up front and stick with it. That, however, excludes the idea that I will be dealing with multiple versions of data access in a single application — something like a non-relational store for front-side caching and a relational store for transactional recording. In this case, having a standard application architecture for querying and returning data matters for testability, maintenance, and consistency.

## 2. IQueryable\<T>

On this we agree. I return `IEnumerable<T>` to prevent the explosion of joins onto returned queries.

## 3. "Specification not pulling its weight"

I would agree that the example used is anemic. The Specification pattern really shines when it gives you the ability to step around issues that would normally mean departing from the standard querying syntax. Something like the examples in my earlier HighwayData posts — "Getting Started with HighwayData + Entity Framework" and "HighwayData Dynamic Filters" *(original links removed — no longer available due to age)*.

The other portion is allowing you to both test and reuse queries — not across types, but across a single type. With paging, ordering, and sorting as specification extensions, you extend a single query object. The specification starts to shine when you add pre/post query interception, projection, SQL logging, and many other extensions that are not surfaced in every data access implementation.

## 4. "This sort of design implies there is value in sharing queries across different parts of the application — and that premise is usually false"

I reuse queries across multiple applications and find it has a lot of power. The advantages to testability are real. A well-formed abstraction that includes projections, sorts, filters, paging, and included paths allows you to compose extensions onto a tested query without rewriting the same LINQ each time. This allows for performance tweaks to poorly written queries without having to hunt down varying different implementations of similar queries.

## 5. "Reading from a database is a common operation and should be treated as such"

I agree, but I think I have a different idea of how to treat common operations. I want my common operations to be fast, testable, and easily changed. I cannot look at database operations — which have far-reaching performance implications — as something that can be ignored and passed off under an approach that cannot be unit tested in isolation.

## 6. "How the abstraction falls down"

I would say that all abstractions fall down when you need some specific piece of the underlying architecture to solve a problem. The answer is not to re-architect or re-implement the behavior, but to know where the abstraction needs to stop. In Highway.Data, we decided to allow for the scenario Ayende outlines by giving you the choice to hit the underlying implementation if you need to — that's what the [advanced query support](https://github.com/HighwayFramework/Highway.Data/blob/master/src/Highway.Data.EntityFramework/QueryObjects/AdvancedQuery.cs?ref=devlinliles.com) is for.

## 7. "Avoid needless complexity"

I agree — needless complexity should be avoided. I disagree that this means we don't need any constraints around how we pull data. In a world that is becoming more and more data-centric, we should want more performance, testability, and extensibility, not less.
