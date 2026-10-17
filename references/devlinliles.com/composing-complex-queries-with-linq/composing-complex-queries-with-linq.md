---
type: Reference
title: "Composing Complex Queries with LINQ"
resource: "https://www.devlinliles.com/composing-complex-queries-with-linq/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

We have all had those times where we need to build chains of complex WHERE statements with several OR/AND operations. These make LINQ queries look really complex and most of the time need to be reused in several places. To clean this up and give us the ability to compose complex queries on the fly — say from a UI filter — give the following a try.

## Usage Example

```csharp
public class Test
{
    public void Testing()
    {
        Expression<Func<Product, bool>> isRed = c1 => c1.Color == "Red";
        Expression<Func<Product, bool>> isCheap = c2 => c2.StandardCost < 10.0m;
        Expression<Func<Product, bool>> isClothing = c3 => c3.Class == "Clothing";

        Expression<Func<Product, bool>> isAcceptable = Utility.BuildOrElse(isRed, isCheap, isClothing);

        IQueryable<Product> products = null;
        var query = products.Where(isAcceptable);
    }
}
```

## The Infrastructure

```csharp
public class ParameterRebinder : ExpressionVisitor
{
    private readonly Dictionary<ParameterExpression, ParameterExpression> map;

    public ParameterRebinder(Dictionary<ParameterExpression, ParameterExpression> map)
    {
        this.map = map ?? new Dictionary<ParameterExpression, ParameterExpression>();
    }

    public static Expression ReplaceParameters(Dictionary<ParameterExpression, ParameterExpression> map, Expression exp)
    {
        return new ParameterRebinder(map).Visit(exp);
    }

    protected override Expression VisitParameter(ParameterExpression p)
    {
        ParameterExpression replacement;
        if (map.TryGetValue(p, out replacement))
        {
            p = replacement;
        }
        return base.VisitParameter(p);
    }
}

public static class Utility
{
    public static Expression<T> Compose<T>(this Expression<T> first, Expression<T> second, Func<Expression, Expression, Expression> merge)
    {
        // build parameter map (from parameters of second to parameters of first)
        var map = first.Parameters
            .Select((f, i) => new { f, s = second.Parameters[i] })
            .ToDictionary(p => p.s, p => p.f);

        // replace parameters in the second lambda expression with parameters from the first
        var secondBody = ParameterRebinder.ReplaceParameters(map, second.Body);

        // apply composition of lambda expression bodies to parameters from the first expression
        return Expression.Lambda<T>(merge(first.Body, secondBody), first.Parameters);
    }

    public static Expression<Func<T, bool>> And<T>(this Expression<Func<T, bool>> first, Expression<Func<T, bool>> second)
    {
        return first.Compose(second, Expression.And);
    }

    public static Expression<Func<T, bool>> Or<T>(this Expression<Func<T, bool>> first, Expression<Func<T, bool>> second)
    {
        return first.Compose(second, Expression.Or);
    }

    public static Expression<Func<T, bool>> OrElse<T>(this Expression<Func<T, bool>> first, Expression<Func<T, bool>> second)
    {
        return first.Compose(second, Expression.Or);
    }

    public static Expression<Func<T, bool>> BuildAnd<T>(params Expression<Func<T, bool>>[] conditions)
    {
        return conditions.Aggregate<Expression<Func<T, bool>>, Expression<Func<T, bool>>>(
            null, (current, expression) => current == null ? expression : current.And(expression));
    }

    public static Expression<Func<T, bool>> BuildOr<T>(params Expression<Func<T, bool>>[] conditions)
    {
        return conditions.Aggregate<Expression<Func<T, bool>>, Expression<Func<T, bool>>>(
            null, (current, expression) => current == null ? expression : current.Or(expression));
    }

    public static Expression<Func<T, bool>> BuildOrElse<T>(params Expression<Func<T, bool>>[] conditions)
    {
        return conditions.Aggregate<Expression<Func<T, bool>>, Expression<Func<T, bool>>>(
            null, (current, expression) => current == null ? expression : current.OrElse(expression));
    }
}
```

Adapted and extended from: [LINQ to Entities: Combining Predicates](https://learn.microsoft.com/en-us/archive/blogs/meek/linq-to-entities-combining-predicates?ref=devlinliles.com)
