---
type: Reference
title: "Callback Pattern to the Rescue"
resource: "https://www.devlinliles.com/callback-pattern-to-the-rescue/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

If you have ever gotten stuck with an interface that has callbacks you don't like or don't want at your implementation layer, the Callback / Chain of Responsibility pattern can save the day.

Imagine the following login credential resolution scenario:

- If the user is already logged in, use those credentials
- If the user has a token from another system, use those credentials
- If the user is domain authenticated, use those credentials
- Otherwise, ask the user for their login credentials

This chain can be achieved by composing handlers so that when it hits the deepest level needed, it succeeds and returns.

## Step 1: Define the Interfaces

```csharp
namespace Core.Interfaces
{
    public interface ICallbackHandler
    {
        ICallBack[] Handle(params ICallBack[] callBacks);
    }
}

namespace Core.Interfaces
{
    public interface ICallBack
    {
        bool Handled { get; set; }
    }
}
```

## Step 2: Define the Callback (Data Only)

```csharp
using System.Windows.Forms;
using Core.Interfaces;

namespace Infrastructure.CallBacks
{
    public class WarningCallBack : ICallBack
    {
        public readonly string WarningDescription;

        public WarningCallBack(string warningDesc)
        {
            WarningDescription = warningDesc;
        }

        public bool Handled { get; set; }
    }
}
```

## Step 3: Define the Handler

The behavior is brokered to the client-application-specific implementation by the handler.

```csharp
public class Handler : ICallbackHandler
{
    public ICallBack[] Handle(params ICallBack[] callBacks)
    {
        List<ICallBack> unhandledCallBacks = new List<ICallBack>();
        foreach (ICallBack callBack in callBacks)
        {
            callBack.Handled = Handle((WarningCallBack)callBack);
            if (!callBack.Handled)
            {
                unhandledCallBacks.Add(callBack);
            }
        }
        return unhandledCallBacks.ToArray();
    }

    private bool Handle(WarningCallBack warningCallBack)
    {
        MessageBox.Show(warningCallBack.WarningDescription, "Warning",
            MessageBoxButtons.OK, MessageBoxIcon.Warning);
        return true;
    }
}
```

By returning the unhandled callbacks, you can compose these handlers into a cache stack or a handler stack — each handler either resolves the callback or passes it along to the next.

This saved me a lot of time and ugliness in my code this morning. Thanks to David O'Hara and Craig Neuwirt.
