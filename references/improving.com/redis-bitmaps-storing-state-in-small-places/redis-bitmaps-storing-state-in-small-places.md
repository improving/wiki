---
type: Reference
title: "Redis Bitmaps: Storing State in Small Places"
resource: "https://www.improving.com/thoughts/redis-bitmaps-storing-state-in-small-places/"
author: "Aaron Burk"
published: '2022-05-03'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Redis is a popular open source in-memory data store that supports all kinds of abstract data structures. In this post and in an accompanying example Java project, I am going to explore two great use cases for one of those data structures: bitmaps. The two use cases: determining “done” in an asynchronous system and collecting distinct activity metrics.

*The source code for the example Java project is available on GitHub here:* https://github.com/burkaa01/redis-bitmap

## What is a bitmap?

In a bitmap each individual bit in a bit array (0 or 1) is used to represent state. This unlocks the potential to represent a lot of state in an extremely little amount of space (something really worth exploring when space is at a premium and there is a large amount of state to represent).

For Redis Bitmaps, Redis uses strings to store this binary data and provides a set of commands that treat these binary strings as bitmaps. These commands make it possible to set and get any bit in a Redis string with constant time complexity (another appealing reason to explore the following potential use cases).

## First use case: done in an asynchronous system

First, suppose there is an asynchronous task made up of a fixed number of steps. Each step processes in parallel and you must track when each step completes to determine when the task is “done”.

With a Redis Bitmap, keyed by the string task id, you can track the state of each step by flipping a bit (from 0 to 1) at the offset corresponding to each step number when the step is done. If the bit where the offset equals the total number of steps in the task is flipped first, then the task as a whole is done when all bits before that end offset bit have been flipped as well.

For instance, if a task has 4 steps, then flipping the bit at offset 4 (from 0 to 1) results in the following initial state: **00001000** (in this example offsets and step numbers are zero-based)

Now, when step number 2 is done, the state looks like this: **00101000**

When steps 0 and 3 are done, the state looks like this: **10111000**

And finally when step number 1 is done, the state looks like this: **11111000** (and because all bits before the end bit at offset 4 have been flipped – the task is done)

Now, let’s check out the example Java project I mentioned (https://github.com/burkaa01/redis-bitmap). For both use cases it all begins in the **trigger-app**. In the **trigger-app** there is a **triggerDone** method (and API definition) in **TriggerController.java** that will trigger an example task. The **count** request parameter represents the number of steps in the triggered example task.

The first time the project interacts with the Redis Bitmap (via the Jedis client) is in that **triggerDone** method. This is where the bit offset equaling the total number of steps in the task is flipped (just as described above):

*// set "last" bit to true, initializing an end of steps marker for this task*

*// before this task is considered done, all bits before this "last" bit must also be set to true*

Jedis jedis = **new** Jedis(redisConnectionInfo);

jedis.setbit(taskId, count, **true**);

Then the method goes on to issue requests for each individual step in parallel to the API defined in **done-app**. In the example step by step state walkthrough above, there was one important bit of logic I glossed over: how exactly do you determine all bits before our end bit have been flipped?

That logic is in the **isDone** method in **DoneController.java** and it looks like this:

**privatestaticboolean** isDone(Jedis jedis, String task) {

*// get the index of the smallest false bit for use in determining if the task is done*

Long leftMostZero = jedis.bitpos(task, **false**);

*// count the number of true bits aka the number of steps that are done*

**long** count = jedis.bitcount(task);

*// check if done*

` ``**boolean**`` done = (leftMostZero == ``**null**`` || leftMostZero < 0 || leftMostZero == count); `

` ``**if**`` (done) { `

` LOGGER.info("Done with all {} steps for task: {}", count - 1, task); `

` } `

` ``**return**`` done; `

`} `

Three things make this determination possible:

1. The Redis BITPOS command that will return the position of the first bit set to 0
2. The Redis BITCOUNT command that will count the number of set bits
3. The fact that in the **trigger-app** the first bit flipped was the bit where the offset equals the total number of steps

Put all three of those things together and you know if you do not find a BITPOS 0 or if that BITPOS 0 equals the BITCOUNT, the task is done.

Let’s take a final look at that initial example step by step state walkthrough:

In the initial state, BITPOS 0 is 0 and BITCOUNT is 1 (the task is not done): **00001000**

When steps 0, 2, and 3 are done, BITPOS 0 is 1 and BITCOUNT is 4 (the task is still not done): **10111000**

But finally, when step number 1 is done, BITPOS 0 and BITCOUNT both equal 5 (the task is done!): **11111000**

## Second use case: collecting distinct activity metrics

On to the second use case: collecting distinct activity metrics. The first use case outlined how to flip a bit at a unique position given an identifier (bits were flipped when each step was done) and the BITCOUNT command was used for the **isDone** check for the task as a whole. Those two commands are all you will need to count and track the number of unique users in this use case.

Let’s take a look at **DistinctController.java** from the example project in the **distinct-app**. This example is rather simple, our API takes in the int **userId** and we set the corresponding bit like so:

*// set bit to true, which accounts for the distinct user*

jedis.setbit(REDIS_KEY, userId, **true**);

And if the bit was already flipped at this **userId** offset (i.e. this user is not new/unique) the count logged below stays the same:

*// count the number of true bits aka the number of distinct users*

**long** count = jedis.bitcount(REDIS_KEY);

LOGGER.info("{} distinct users", count);

Just like in the prior use case, if you want to try this use case out for yourself, look in **TriggerController.java**. The **triggerDistinct** method (and API definition) will trigger a variable amount of “userId” activity and the **distinct-app** will track the number of unique users accordingly.

## In conclusion

I want to emphasize that Redis Bitmaps don’t fit every problem, but I do think it is a clever tool to have in the toolbox when time and space (especially space) is at a premium and you have a lot of state to track. Hopefully this post, the provided example Java project (https://github.com/burkaa01/redis-bitmap), and a couple mock use cases were enough to illustrate that.

Have a question about this Tech Tuesday topic? Reach out.
