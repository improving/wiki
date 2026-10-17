---
type: Reference
title: "RhinoMocks and Constrained Expectations"
resource: "https://www.devlinliles.com/rhinomocks-and-constrained-expectations/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Here are some tests to illustrate how to leverage RhinoMocks constraints. Notice that it is easier to get a passing test on failing code with a stub.

With the `Matches()` method, you can use any predicate or method call that returns a boolean. You cannot, however, use a lambda with a method body (e.g., `() => {}`). That will not compile.

```csharp
[TestClass]
public class Tests
{
    [TestMethod]
    public void Should_Allow_Constraint()
    {
        // Arrange
        var mock = MockRepository.GenerateStrictMock<ITestExerciser>();
        mock.Expect(x => x.DoSomething(Arg<List<ITest>>.Matches(c => c.First() is Test)))
            .Return("TestPass");
        var tester = new Tester(mock);

        // Act
        var result = tester.DoIt();

        // Assert
        mock.VerifyAllExpectations();
        Assert.AreEqual("TestPass", result);
    }

    [TestMethod]
    public void Should_Enforce_Constraint_On_Strict_Mock()
    {
        // Arrange
        var mock = MockRepository.GenerateStrictMock<ITestExerciser>();
        mock.Expect(x => x.DoSomething(Arg<List<ITest>>.Matches(c => c.Any(t => t is Test))))
            .Return("TestPass");
        var tester = new Tester(mock);

        // Act
        var result = tester.DoItWrong();

        // Assert
        mock.VerifyAllExpectations();
        Assert.AreEqual("TestPass", result);
    }

    [TestMethod]
    public void Should_Allow_Manual_Enforce_Constraint_On_Stub()
    {
        // Arrange
        var mock = MockRepository.GenerateStub<ITestExerciser>();
        mock.Expect(x => x.DoSomething(Arg<List<ITest>>.Matches(c => TestSomething(c))))
            .Return("TestPass");
        var tester = new Tester(mock);

        // Act
        var result = tester.DoItWrong();

        // Assert
        mock.AssertWasCalled(x => x.DoSomething(Arg<List<ITest>>.Matches(c => c.Any(t => t is Test))));
        Assert.AreEqual("TestPass", result);
    }

    private bool TestSomething(List<ITest> tests)
    {
        return true;
    }
}

public class Tester
{
    private ITestExerciser _testExerciser;

    public Tester(ITestExerciser testExerciser)
    {
        _testExerciser = testExerciser;
    }

    public object DoIt()
    {
        return _testExerciser.DoSomething(new List<ITest>() { new Test() });
    }

    public object DoItWrong()
    {
        return _testExerciser.DoSomething(new List<ITest>() { new TestBase() });
    }
}

public class TestExerciser : ITestExerciser
{
    public object DoSomething(List<ITest> args)
    {
        return null;
    }
}

public interface ITestExerciser
{
    object DoSomething(List<ITest> args);
}

public class Test : TestBase { }

public class TestBase : ITest
{
    public int Id { get; set; }
}

public interface ITest
{
    int Id { get; set; }
}
```
