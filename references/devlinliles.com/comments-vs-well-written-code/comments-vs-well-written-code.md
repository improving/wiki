---
type: Reference
title: "Comments vs. Well-Written Code"
resource: "https://www.devlinliles.com/comments-vs-well-written-code/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

*Originally from my old blog. Mike Pitts was the lead on the conversation, and clarified in comments (since lost) that he preferred well-written code but that in lieu of that, comments helped.*

The conversation started today about a developer leaving our team and needing to knowledge-transfer his part of the code base to other team members. The lead programmer on the project told him to stop working on new development and start commenting his code so that the people coming in after him would understand what he had been doing.

Personally, the first thing I do when opening an unfamiliar code base is press `Ctrl+M, Ctrl+O` and start looking around. (That's the Visual Studio shortcut for "minimize all outlining" — you get to see method declarations and that's about it.) This collapses blocks of comments so they're not intrusive. I never re-expand them. The idea that you need comments to understand code is, to me, a big red flag for bad code. Well-named variables are much more intuitive for learning a new code base than comments.

I have never sat down to learn an entire code base in one sitting. I am normally working on a small part or a bug fix and need to find something very specific. To that end, a well-named class/method/property is much more helpful when you use Edit → Find than having to sort through all the comments for the information you need.

Also, I am sure almost everyone has opened a piece of code that had a `form1` or `class1` class. Those names that Visual Studio generates are not supposed to stay that way. Here is how you avoid it:

1. Go to "Add Class"
2. **DON'T CLICK OK**
3. Look at the bottom of the dialog and type in something intuitive
4. Go drink something with an umbrella and retire to the happy place of understandable class name land

To prove my point:

**The commented-but-poorly-named version:**

```csharp
//This is a class that handles
//calculating tax for sales in
//several states
public class class1
{
    //Calc sales total for a couple states
    //AR - tax 9.5%
    //NM - tax 5.5%
    //TX - tax 8.5%
    public decimal calc(decimal a, string n)
    {
        //The quick red fox jumped over the lazy brown dog.
        //The quick red fox jumped over the lazy brown dog.
        //The quick red fox jumped over the lazy brown dog.
        //The quick red fox jumped over the lazy brown dog.
        switch(n)
        {
            case "AR":
                return a * 1.095;
                break;
            case "TX":
                return a * 1.0875;
                break;
            case "NM":
                return a * 1.055;
                break;
        }
    }
}
```

**The well-named, comment-free version:**

```csharp
public class MultiStateSalesTaxCalculator
{
    public decimal ARKANSAS_STATE_SALES_TAX = 0.095;
    public decimal TEXAS_STATE_SALES_TAX = 0.095;
    public decimal NEW_MEXICO_STATE_SALES_TAX = 0.095;

    public decimal CalculateSalesTotalWithTaxByState(decimal SubTotal, string stateAbbreviation)
    {
        switch(stateAbbreviation)
        {
            case "AR":
                return SubTotal + (SubTotal * ARKANSAS_STATE_SALES_TAX);
                break;
            case "TX":
                return SubTotal + (SubTotal * TEXAS_STATE_SALES_TAX);
                break;
            case "NM":
                return SubTotal + (SubTotal * NEW_MEXICO_STATE_SALES_TAX);
                break;
        }
    }
}
```

The second version needs no comments. The class name tells you what it does, the constants tell you the rates, and the method name tells you exactly what it calculates. Good code documents itself.
