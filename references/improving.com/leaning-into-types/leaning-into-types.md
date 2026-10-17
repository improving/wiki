---
type: Reference
title: "Leaning Into Types"
resource: "https://www.improving.com/thoughts/leaning-into-types/"
author: "Ahmed Hammad"
published: '2024-01-10'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

*In this article, I use F#-inspired pseudocode for my examples. However, many of these strategies can work with a bit of elbow grease in other languages.*

Types help us catch errors, design our interfaces, and create readable code. However, we can get even more out of them if we consider replacing our flags with types. Let's dive in with a security example. Whenever we read a string from an untrusted source, it may have code injected into it. Therefore, we must sanitize the string before use. Let's say we code this in the most straightforward way:

```fsharp
let readQuery (source:Datasource) : string = ...
let someLogic (x:string) : Results = ...
someLogic (readQuery …)
```

This leaves us with no protection against using unsanitized strings. For instance, if `readQuery` returns a string with malicious code injected in it, `someLogic` would use it, to disastrous effect. We want to ensure that `someLogic` can’t use an unsanitized string. This is a job for types, but WHAT types? For instance, what if we wrap our string in a type and have a sanitization flag, along with the appropriate code, like so?

```fsharp
type ExternalString = {
      value: string;
      isSanitized: bool;
}

let sanitize (x:string) : ExternalString = {
      value = …;
      isSanitized = true;
}

let readQuery (source:Datasource) : string = …
let someLogic (x:ExternalString) : Results = …
let results = someLogic (sanitize (readQuery …))
```

This approach requires us to add logic to `someLogic` to check the sanitization flag before using the string. That’s extra work and we may forget to do it. However, what if instead of using a flag, we made sanitized strings a different type?

```fsharp
type SanitizedString = Sanitized of string
let readQuery (source:Datasource) : string = …
let sanitize (x:string) : SanitizedString = Sanitized (...)
let someLogic (x:SanitizedString) : Results = …
let results = someLogic (sanitize (readQuery …))
```

Now `someLogic` only accepts the type `SanitizedString`. And since the only way to get that is by calling `sanitize`, this ends up requiring sanitizing the string before use.

Rather than setting a flag to indicate that the string has been sanitized, we make sure that sanitized strings are a different type entirely. The key insight is that a flag often marks data as a different type. So why not just create a new type entirely?

Now this catches cases where we forget to call string sanitization. Also, by not requiring that we check a sanitization flag in our logic, it eliminates errors arising from forgetting to do that as well. It’s not bulletproof, but there are fewer ways we can get in trouble.

We don’t need algebraic data types for this. We could declare a new record, class, etc…as a wrapper for a sanitized string in any language with decent type checking. But what follows is (as far as I know) unique to languages that support algebraic types.

Languages that support algebraic data types (like F#) will also check if we missed some cases. For example, let’s say we want to alter our sanitization function so that it checks our string and if it has malicious code, it tags it as such, otherwise it marks it as a safe string. Now we’re dealing with 2 types. Also, if a string is malicious, we don’t care what’s in it, we just want to indicate a malicious string was received. In fact, we don’t want to keep it as we want to avoid the possibility that someone may mistakenly use it. This now gives us this:

```fsharp
type SanitizedString =
      | Safe of string
      | Malicious
```

In addition to our other changes, `someLogic` needs to handle this:

```fsharp
let someLogic (x:SanitizedString) : Results =
      match x with
      | Safe x -> ...
```

But when I try to build in F#, I get this:

`Incomplete pattern matches on this expression. For example, the value 'Malicious' may indicate a case not covered by the pattern(s)`

Yes, I forgot to add the logic to handle the case of `Malicious`! And because I declared it as an algebraic data type, F# saw this and informed me of it. I wouldn’t get that checking with a run-of-the-mill statement over a flag. So I fix the code:

```fsharp
let someLogic (x:SanitizedString) : Results =
      match x with
      | Sanitized x -> ...
      | Malicious -> ...
```

Now all's right with the world.

So the use of types also helped check the completeness of our logic. Incidentally, there’s at least one language (Idris) that goes one step further and generates the skeleton covering all your cases for you if you ask. Again, it uses algebraic data types to know all the possibilities.

Now let's look at a non-security example. Imagine we're writing code to process job applicants. These applicants have a variety of states, with additional data that varies with each state. For instance, a job applicant who...

1. Submitted a resume must include the resume.

2. Has an interview scheduled must have a date and time for the interview.

3. Is Rejected has a reason for the rejection.

4. Received a job offer has a salary offer accompanying it.

These are the only legal states; so for instance, a rejected applicant cannot have a salary offer. This means we can't do this:

```fsharp
type Resume = ...
type RejectionReason = ...

type StatusType =
      | SubmittedResume
      | ScheduledInterview
      | Rejected
      | MadeOffer

type ApplicantStatus = {
      firstName: string;
      lastName: string;
      ...
      statusType: StatusType;
      resume: Resume;
      offer: decimal;
      rejectionReason: RejectionReason;
      interviewDate: DateTime;
}
```

This will allow illegal states and we'd need to add logic to handle those states. Instead, we can prevent even representing such states with this:

```fsharp
type Resume = ...
type RejectionReason = ...

type Applicant = {
      firstName: string;
      lastName: string;
      ...
}

type ApplicantStatus =
      | SubmittedResume of Applicant * Resume
      | ScheduledInterview of Applicant * DateTime
      | Rejected of Applicant * RejectionReason
      | MadeOffer of Applicant * decimal
```

Each status has a tuple accompanying it, and only one type of tuple is allowed for any status. As you can see, this type enforces the states listed above without a single line of logic; it's all done through the type system. We had to think a bit more about our types, but we recouped our effort with less logic we had to write and errors reported at build time and for all code paths.

In conclusion, having a strong type system isn't enough. We must choose to use the type system even when we don't have to and we must think carefully about our types. One tip for doing this is to replace flags with types. Leaning more strongly into types turns our type system into a better ally, rather than the barrier too many developers think it is.
