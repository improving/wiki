---
type: Reference
title: "Java Enums for Better Code"
resource: "https://www.improving.com/thoughts/java-enums-for-better-code/"
author: "Paul Nienaber"
published: '2025-03-21'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Enums have been around for a while, and they mostly get used as they were first conceived in C: As a set of distinct, named values used for things like branching based on a previously named and stored condition case. But Java enums are more than a simple set of distinct values with names, and we can leverage this to improve single-source-of-truth adherence in our code.

Java enums are essentially fully-fledged objects with an optional constructor and member variables. This plus a unique feature that normal classes lack provides a useful idiom for simple, obvious, and highly maintainable code where we want to do things like handling data types based on a string type name or even a class name.

## Scattered Code

Far too often code ends up containing a set of handlers (code or simply metadata) as objects or plain methods, and a separate list allowing lookup or conditional calling of those entities. Taking advantage of the `.values()` static method and the enum class's `static` block, we can reduce the lookup mapping and its separate target entities to a single source of truth so our code is both more readable and safer to modify.

```java
enum DataMapper { 

  JSONBLOB("json", MyStruct.class, 

      (OpaqueDataContainer x) -> x.getJson()); 

  BASE64BINARY("base64", byte[].class, 

      (OpaqueDataContainer x) -> Base64.getDecoder().decode(x.getBase64)); 

 

  private static Map<String, DataMapper> externalTypeNameMap; 

  private final String externalTypeName; 

  private final Class<?> conversionResultType; 

  private final Function<OpaqueDataContainer, Object> mapper; 

 

  static { 

    ExternalTypeNameMap = new HashMap<>(); 

    For (DataMapper m : DataMapper.values()) { 

      ExternalTypeNameMap.put(m.externalTypeName, m); 

    } 

  } 

 

  private DataMapper( 

      String externalTypeName, 

      Class<?> conversionResultType, 

      Function<OpaqueDataContainer, Object> mapper) { 

    this.externalTypeName = externalTypeName; 

    this.conversionResultType = conversionResultType; 

    this.mapper = mapper; 

  } 

 

  Class<?> getConversionResultType() { 

    return conversionResultType; 

  } 

 

  Object getMappedValue(OpaqueDataContainer d) { 

    return mapper.apply(d); 

  } 

 

  DataMapper get(String externalTypeName) { 

    Return  

} 
```

For other mapper interfaces (e.g. providing a key for extracting the data), you can use other functor types from `java.util.function`, or write your own interface as needed.

Note in the example that via an extra member `conversionResultType` you can trivially handle return type polymorphism coupled to the various mapping-input types with a cast in the calling code:

```java
OpaqueDataContainer d = getOpaquePolymorphicDataSomehow(); 

DataMapper m = DataMapper.get(d.getTypeName()); 

someOtherOverloadedHandler(d.getNativeType().cast(m.getMappedValue(d))); 
```

The` .values()`-based lookup table can also be used elegantly in simpler situations, for example a config parameter string lookup.

```markup
enum MyConfigParam { 

  PEPSI("cola"), 

  ROOTBEER("rootbeer"); 

 

  private final String configString; 

  private static Map<String, MyConfigParam> configStringMap; 

 

  static { 

    configStringMap = new HashMap<>(); 

    for (MyConfigParam p : MyConfigParam.values()) { 

      configStringMap.put(p.configString, p); 

    } 

  } 

 

  static MyConfigParam getByConfigString(String configString) { 

    return configStringMap.get(configString); 

  } 

 

  @Override 

  public String toString() { 

    return configString; 

  } 

} 
```

This approach does come with some very minor caveats—which can be easily addressed...

## Implementation Details

### Variable Scope

Enum definition parameter lists cannot reference static variables of the enum class itself, so constants and similar should most commonly be addressed by putting these values inside a containing class, whether another application class or simply a utility container class.

### Reuse, Reduce

As the context for the enum declaration parameters isn’t procedural and Java lacks any facility to reuse expression or return values, a common gotcha here is that using the same value more than once in constructing an enum value requires duplicating the expression or call that produces it —when we were just working to avoid unnecessary code duplication. It's easy to use a mapper-function factory lambda to allow reuse of data such as other enum property values (remember, we're avoiding multiple sources of truth). If it's more appropriate you can use this for only *some* of your enum objects by providing and using an additional constructor. Building on the first example above:

```java
ENCODEDPOJO("binarypojoblob", Object[].class, 

    (Class<?> c) -> 

      (OpaqueDataContainer x) ->x.unpackPojoAs(c)); 

 

private DataMapper( 

    String externalTypeName, 

    Class<?> conversionResultType, 

    Function<Class<?>, Function<OpaqueDataContainer, Object>> mapperFactory) { 

  this.externalTypeName = externalTypeName; 

  this.conversionResultType = conversionResultType; 

  this.mapper = mapperFactory.apply(conversionResultType); 

} 
```

Compared to the regular constructor, here we instead use a factory lambda, allowing the constructor to provide the `conversionResultType` context which is then captured in the closure and eliminating the value being written out in multiple places.

### A Lint Trap (Recycle)

A similar gotcha arises when you want to reuse an object or value in the handler Lambda. This may be necessary either to avoid instantiating a parser or factory object every single time the `mapper` is called, or to avoid duplication of the same data or call expression.

It’s tempting to address this need for value reuse by making the value a statically initialized static member in your outer class. However, it's discouraged (and enforced by some linters) not to access a non-const static member of an outer class, and the member of the outer class also cannot be both const and programmatically derived (in its `static` block). It's simple to reuse your lambda factory interface to do this or create another parameter-less factory interface if you desire.

```java
FORMATTEDDATETIME("timestamp", Date.class, 

    (Class <?> ignored) -> { 

      DateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss"); 

      return (OpaqueDataContainer x) -> df.parse(x.getString()); 

    }); 
```

Here we’ve taken the same factory interface as before, ignoring the `Class <?>` parameter as it’s unused for the lambda-generation logic in the factory.

### Class Preservation

If you use class object as keys in a lookup table, and you dynamically load and unload any of those classes, you may have another problem: Having them referenced as map keys stores a reference to the class and not its hashcode so the class cannot be unloaded until it's removed from the map. You might consider strongly tying together the class unloading and enum lookup map updating code to enforce the consistency required for the unloads to work.

### Better Code

With some simple but unorthodox use of enums, you can take maintenance tripwires out of your code, and make it easier to grok the whole picture of your converter handler or other functional mapping. I don't know about you, but I don't plan on suffering from hardcoded lookup tables again if I can avoid it.

Ready to enhance your code with innovative techniques? [Reach out to Improving for expert guidance and support.](https://www.improving.com/contact)
