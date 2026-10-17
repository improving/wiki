---
type: Reference
title: "LINQ, Lambdas, and the Learning Curve"
resource: "https://www.devlinliles.com/linq-lambdas-and-the-learning-curve/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Been away for a while working on a 107,000-hour project. It isn't done, but I am making time to blog and do my technical mentorship, because I have come to realize that there will always be high-priority projects. You have to take the time to train and mentor during those projects regardless. Now on to the show.

I know that LINQ has received a massive welcome from the community and I have to say it is deserved. On the whole it is a great addition to the language. I do not, however, like one part of it: verbose LINQ. I realize that it is more SQL-like and is perceived to shorten the learning curve, but I disagree. Lambdas are where the true power of LINQ sits, and using the verbose syntax seems to focus you on learning LINQ one way so that you have to re-learn it another way later.

I am going to focus on the lambda side of LINQ, simply out of preference. Keep an eye out for the verbose vs. lambda death match — that is a post for another time.

## Breaking Down the Lambda

Lambda statements are actually fairly simple once you break them apart.

```csharp
SomeList.Where(c => c.Id == someInt);
```

The above is the lambda equivalent of this foreach block:

```csharp
foreach (Item item in SomeList)
{
    if (item.Id == someInt)
        SomeOtherList.Add(item);
}
```

Let's break down the lambda to make it a bit more clear.

`c =>` — This declares that the item in the list we are looking at will be held in the local variable named `c`. This is no different from naming the variable in a foreach loop `c`. You can name your lambda variables more intuitively, and I would encourage you to do so. Something like:

```csharp
SomeList.Where(menuItem => menuItem.Id == someInt);
```

Once the object is declared you have access to all of its members. That is how we can use the `Id` property to check against a Boolean expression. Filtering based on some Boolean expression is the most common use for lambdas, but not the only one.

## Selecting and Transforming

```csharp
List<SubMenu> submenus = SomeList.Select(menuItem => new SubMenu()
{
    ParentMenuId = menuItem.Id
});
```

In this example we have created a SubMenu object from every item in the list. LINQ lets us change the output type of the selection at will. This is very useful when you are creating items from other items. The equivalent foreach block would be:

```csharp
List<SubMenu> SubMenus = new List<SubMenu>();

foreach (MenuItem item in SomeList)
{
    SubMenu subMenu = new SubMenu();
    subMenu.ParentMenuId = item.Id;
    SomeOtherList.Add(subMenu);
}
```

The power here is real. I have the ability to replace entire loops with a single line. The hit to readability is a concern, but lambdas lend themselves to so many applications and are central to LINQ, so they should be part of every developer's core toolset. Name your lambda variables intuitively and you will get a lot of great mileage out of LINQ without losing readability.
