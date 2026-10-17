---
type: Reference
title: "Object Repository: Extending the Standard Repository Pattern"
resource: "https://www.devlinliles.com/object-repository-extending-the-standard-repository-pattern/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I have found that there are often times I use the same queries against an object set, but end up writing the same or very similar LINQ statements against my context. This can be solved by using an object-specific repository. Below is the implementation over Entity Framework 4.1 using the AdventureWorks sample.

## Setup

Start with a plain console application and add an `EntityContext` folder. Then add a new ADO.NET Entity Data Model — name it `AdventureWorks.edmx`. Use the wizard to connect to the local AdventureWorks database. Then add a `Repository` folder for repository implementations. This follows the patterns from the Repository Patterns and POCO Separation posts.

## The Generic Repository

```csharp
using System;
using System.Data.Objects;
using System.Linq;
using ObjectRepository.EntityContext;

namespace ObjectRepository.Repository
{
    public class EntityFrameworkRepository : IRepository
    {
        private readonly ObjectContext _context;

        public EntityFrameworkRepository(ObjectContext context)
        {
            _context = context;
        }

        public IQueryable<T> AsQueryable<T>() where T : class
        {
            return _context.CreateObjectSet<T>();
        }

        public void SaveChanges()
        {
            _context.SaveChanges();
        }

        public void Delete<T>(T item) where T : class
        {
            _context.DeleteObject(item);
        }

        public void Add<T>(T item) where T : class
        {
            _context.CreateObjectSet<T>().AddObject(item);
        }

        public void Attach<T>(T item) where T : class
        {
            _context.CreateObjectSet<T>().Attach(item);
        }

        public void Detach<T>(T item) where T : class
        {
            _context.Detach(item);
        }
    }
}
```

This gives us the base to use, and we could use it as-is:

```csharp
using ObjectRepository.EntityContext;
using ObjectRepository.Repository;

namespace ObjectRepository
{
    class Program
    {
        static void Main(string[] args)
        {
            IRepository repository = new EntityFrameworkRepository(new AdventureWorksEntities());

            var longRunningProducts = repository.AsQueryable<Product>()
                .Where(x => x.DaysToManufacture > 3);
        }
    }
}
```

## The Object-Specific Repository

If we need to use that same "long running products" query in multiple places, repeating that LINQ gets old fast — and we have no control over the magic number `3`. Instead, wrap it in a product-specific repository:

```csharp
using System.Linq;
using ObjectRepository.EntityContext;

namespace ObjectRepository.Repository
{
    public interface IProductRepository
    {
        IQueryable<Product> GetLongRunningProducts();
    }

    public class ProductRepository : IProductRepository
    {
        private readonly IRepository _repository;

        public ProductRepository(IRepository repository)
        {
            _repository = repository;
        }

        public IQueryable<Product> GetLongRunningProducts()
        {
            return _repository.AsQueryable<Product>()
                .Where(x => x.DaysToManufacture > 3);
        }
    }
}
```

Now our usage becomes:

```csharp
using ObjectRepository.EntityContext;
using ObjectRepository.Repository;

namespace ObjectRepository
{
    class Program
    {
        static void Main(string[] args)
        {
            IRepository repository = new EntityFrameworkRepository(new AdventureWorksEntities());
            IProductRepository productRepository = new ProductRepository(repository);
            var longRunningProducts = productRepository.GetLongRunningProducts();
        }
    }
}
```

Now no matter where you use the long-running products query, you get the same result. No one has to remember the magic `3`, and if it changes, it only changes in one place. This also allows you to wrap the queries in unit tests and integration tests for performance validation — but that is another post.
