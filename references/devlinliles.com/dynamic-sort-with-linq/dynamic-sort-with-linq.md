---
type: Reference
title: "Dynamic Sort with LINQ"
resource: "https://www.devlinliles.com/dynamic-sort-with-linq/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

*Brought over from my old blog. Also worth checking out: *[*Dynamic LINQ Part 1*](https://weblogs.asp.net/scottgu/dynamic-linq-part-1-using-the-linq-dynamic-query-library/?ref=devlinliles.com)* by ScottGu.*

We have all at one time or another gotten a user request for sorting based on column names. If you are using a pre-built control it most likely handles this; if it is home-grown it will probably need some work. You could write a sort for every column, or you could write one that takes the column name as a string and sorts based on that. LINQ, however, doesn't like string-based property access. If you want string-based sorting you must either write a nasty switch statement or use a sort extension like this one.

## The Extension

```csharp
public static class LinqSortExtensions
{
    private const string Ascending = "ASC";

    public static IOrderedQueryable<T> OrderBy<T>(this IQueryable<T> source, string property, string direction)
    {
        return direction == Ascending ? source.OrderBy(property) : source.OrderByDescending(property);
    }

    public static IOrderedQueryable<T> OrderBy<T>(this IQueryable<T> source, string property)
    {
        return ApplyOrder(source, property, "OrderBy");
    }

    public static IOrderedQueryable<T> OrderByDescending<T>(this IQueryable<T> source, string property)
    {
        return ApplyOrder(source, property, "OrderByDescending");
    }

    public static IOrderedQueryable<T> ThenBy<T>(this IOrderedQueryable<T> source, string property, string direction)
    {
        return direction == Ascending ? source.ThenBy(property) : source.ThenByDescending(property);
    }

    public static IOrderedQueryable<T> ThenBy<T>(this IOrderedQueryable<T> source, string property)
    {
        return ApplyOrder(source, property, "ThenBy");
    }

    public static IOrderedQueryable<T> ThenByDescending<T>(this IOrderedQueryable<T> source, string property)
    {
        return ApplyOrder(source, property, "ThenByDescending");
    }

    static IOrderedQueryable<T> ApplyOrder<T>(IQueryable<T> source, string property, string methodName)
    {
        var props = property.Split('.');
        var type = typeof(T);
        var arg = Expression.Parameter(type, "x");
        Expression expr = arg;
        foreach (var pi in props.Select(prop => type.GetProperty(prop)))
        {
            expr = Expression.Property(expr, pi);
            type = pi.PropertyType;
        }
        var delegateType = typeof(Func<,>).MakeGenericType(typeof(T), type);
        var lambda = Expression.Lambda(delegateType, expr, arg);

        var result = typeof(Queryable).GetMethods().Single(
                method => method.Name == methodName
                        && method.IsGenericMethodDefinition
                        && method.GetGenericArguments().Length == 2
                        && method.GetParameters().Length == 2)
                .MakeGenericMethod(typeof(T), type)
                .Invoke(null, new object[] { source, lambda });
        return (IOrderedQueryable<T>)result;
    }
}
```

This allows you to pass in a property name and a sort direction, and supports multiple chained sorts with `ThenBy`. Here are the NUnit tests to verify it works:

## Tests

```csharp
[TestFixture]
public class QueryTests
{
    [Test]
    public void CanSortWithOnlyStrings()
    {
        IQueryable<TestObject> items = new List<TestObject>()
        {
            new TestObject() { id = 1, Test = "Test1" },
            new TestObject() { id = 3, Test = "Test3" },
            new TestObject() { id = 2, Test = "Test2" },
        }.AsQueryable();

        Assert.AreEqual(2, items.OrderBy("id", "ASC").ToArray()[1].id);
    }

    [Test]
    public void CanSortDescendingWithOnlyString()
    {
        IQueryable<TestObject> items = new List<TestObject>()
        {
            new TestObject() { id = 1, Test = "Test1" },
            new TestObject() { id = 3, Test = "Test3" },
            new TestObject() { id = 2, Test = "Test2" },
        }.AsQueryable();

        Assert.AreEqual(1, items.OrderBy("id", "DSC").ToArray()[2].id);
    }

    [Test]
    public void CanSortMultipleTimesAscending()
    {
        IQueryable<TestObject> items = new List<TestObject>()
        {
            new TestObject() { id = 1, Test = "Test1" },
            new TestObject() { id = 3, Test = "Test3" },
            new TestObject() { id = 2, Test = "Test3" },
            new TestObject() { id = 2, Test = "Test2" },
            new TestObject() { id = 2, Test = "Test1" }
        }.AsQueryable();

        var item = items.OrderBy("id", "ASC").ThenBy("Test", "ASC").ToArray()[3];
        Assert.AreEqual("Test3", item.Test);
    }

    [Test]
    public void CanSortMultipleTimesWithMultipleDirections()
    {
        IQueryable<TestObject> items = new List<TestObject>()
        {
            new TestObject() { id = 1, Test = "Test1" },
            new TestObject() { id = 3, Test = "Test3" },
            new TestObject() { id = 2, Test = "Test3" },
            new TestObject() { id = 2, Test = "Test2" },
            new TestObject() { id = 2, Test = "Test1" }
        }.AsQueryable();

        var item = items.OrderBy("id", "ASC").ThenBy("Test", "DSC").ToArray()[3];
        Assert.AreEqual("Test1", item.Test);
    }
}

public class TestObject
{
    public int id { get; set; }
    public string Test { get; set; }
}
```

Enjoy.
