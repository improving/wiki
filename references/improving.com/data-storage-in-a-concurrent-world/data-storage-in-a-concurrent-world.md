---
type: Reference
title: "Data Storage in a Concurrent World"
resource: "https://www.improving.com/thoughts/data-storage-in-a-concurrent-world/"
author: "Michael Perry"
published: '2024-12-18'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

On a flight from DFW to Guadalajara I looked out the window. In the distance, I saw a flash of lightning toward the south. A moment later, I saw a flash from behind the plane, toward the north. It occurred to me that a traveler passing me going the opposite direction might disagree on which bolt of lightning struck first, assuming that we were both traveling very fast.

### Race Conditions

In a computer system, it takes much less than moving at relativistic speeds to get a disagreement. All you need to do is load data into a browser. Presuming that it takes about 20 seconds for a user to act on that data, there's a very good chance that sometimes, someone else will disagree about the order of their relative actions.

When I was booking this flight, I chose a seat. Surely other people were booking the same flight at the same time. Glancing around the airplane, I see about one hundred and twenty of them. What are the odds that two of us would simultaneously load up the same seating chart? What are the odds that we would both pick the same seat? Probably not great. But certainly not zero. Given how many people book flights daily, it's bound to happen.

![Asset - Image 1 Data Storage in a Concurrent World ](images/AdobeStock_595026718.jpeg)

### Causality

The key to understanding the order of events in either relativity or computing is the same: causality. One flash of lightning did not cause the other. My seat selection did not cause someone else's. Those two events are not causally related. People can therefore disagree on their relative order. But they do have a common cause.

The cause is that we both reserved the same flight segment. If two people select seat 15C on different flight segments, there's no issue. It's only seats within the same segment that matter. The seat selection is causally related to the segment.

### Data Partitioning

To resolve the issue, software architects partition the data. In this case, they'll define a partition based on flight segment. This partition allows the system to ensure the following:

- Events are well-ordered
- Only one processor is managing an event for this partition at any given time
- The data is co-located to allow locking

With well-ordered seat selection and a single processor per flight segment, the problem becomes simple. Look up the co-located record for the seat. Lock it. If it is not assigned, assign it. Then unlock and go to the next seat selection in the partition. Some actions require partitioning the data according to flight segment. Seat selection, first-class upgrades, and standby are just a few.

![Asset - Image 2 Data Storage in a Concurrent World ](images/AdobeStock_273572779.jpeg)

Other actions are not causally related to the flight segment. Some of these are payment, car rental, and travel insurance. Understanding these causal relationships is the key to selecting the right partition. As data flows through a computer system, it will move from one store to another. It will be partitioned according to different properties along the way. Different observers may disagree on the overall order of events. However, within the appropriate partitions, the order of events can be determined.

At scale, lightning always strikes twice. Be prepared for it.

If you'd like to work with Improving to ensure your organization is prepared for events like these, [reach out to us.](https://www.improving.com/contact)
