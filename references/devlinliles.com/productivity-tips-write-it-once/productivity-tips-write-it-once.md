---
type: Reference
title: "Productivity Tips: Write It Once"
resource: "https://www.devlinliles.com/productivity-tips-write-it-once/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Over the years I have built up a very large list of templates, snippets, and extensions for the sole purpose of quickly building out code in a quality way. I find that targeted usage of code generation makes me far more productive because I am able to express intended code very quickly and with fewer typographical errors. All of this relies on learning patterns and then leveraging them — much like [CodeRush Templates](https://community.devexpress.com/blogs/rorybecker/archive/2010/09/14/coderush-templates-101.aspx?ref=devlinliles.com) or [ReSharper Mnemonics](https://resharper-plugins.jetbrains.com/packages/mnemonics/?ref=devlinliles.com).

## Try This Exercise

Create a `Person` class with an integer `Id`, a first name, a last name, and a method that returns the full name by combining the first and last with a space. Simple, right? How long would it take you?

**Target output:**

```csharp
public class Person
{
    public int Id { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }

    public string FullName()
    {
        return string.Format("{0} {1}", FirstName, LastName);
    }
}
```

For me, generating this code took **19 seconds** using the following keystrokes (no mouse):

- `c<tab>` — generates the class scaffold
- `Person<enter>` — names the class
- `pi<tab>Id<enter>` — creates and names the `Id` integer property
- `ps<tab>FirstName<enter>` — creates and names the first name string property
- `ps<tab>LastName<enter>` — creates and names the last name string property
- `ms<tab>FullName<enter>` — creates and names the `FullName` method
- `return string.Format("{0} {1}", FirstName, LastName);` — fills in the body

## The Same Approach for Tests

Being a TDD guy, I also wrote the test using the same template system:

- `ts<tab>FullNameShouldReturnFirstSpaceLast<enter>` — generates the test body and names the test method
- `Person<enter>` — sets the type for the target
- `FullName<enter>` — sets the method under test
- `Is.EqualTo("Devlin Liles")` — sets the NUnit assertion
- Navigate up and fill in `target.FirstName = "Devlin"` and `target.LastName = "Liles"`

**Target output:**

```csharp
[Test]
public void FullNameShouldReturnFirstSpaceLast()
{
    // Arrange
    var target = new Person();
    target.FirstName = "Devlin";
    target.LastName = "Liles";

    // Act
    var result = target.FullName();

    // Assert
    Assert.That(result, Is.EqualTo("Devlin Liles"));
}
```

## The Bigger Picture

Make sure you are leveraging every ounce of productivity out of your tools so that slinging lots of high-quality code becomes second nature. The goal isn't typing speed — it's reducing friction between intent and implementation.
