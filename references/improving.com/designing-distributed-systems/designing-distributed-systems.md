---
type: Reference
title: "Designing Distributed Systems"
resource: "https://www.improving.com/thoughts/designing-distributed-systems/"
author: "Tim Rayburn"
published: '2021-09-22'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Nearly everything we do these days with computers, from Teams messages and video chats to buying up the latest hot Cryptocurrency like DOGE or SHIB, happens exclusively because of interconnected computers. At Improving we believe that "Our success is a result of our collective involvement", and it's true, our modern era exists because of *distributed systems*.

Despite this, most people have very little idea how groups of computers get work done together. This article is going to seek to explain some of these basic ideas, and how they are truly similar to how humans communicate (though computers are faster).

![Virtual Meeting](images/Designing_Distributed_Systems_-_Body_Image.jpg)

When it comes to computers talking to one another, the first and most important concept is to determine if the communication method is synchronous or asynchronous. When we first taught computers how to communicate, we started with synchronous communication. We taught them how to "pick up the phone" and talk to another computer. This is the model of communication behind the World Wide Web, and it works. We knew about the power of the telephone, so surely letting computers talk to one another that way would be better than anything else we could think of, right?

![Open Mailbox](images/Designing_Distributed_Systems_-_Body_Image_-2.jpg)

However, the most powerful form of communication for computers is not modeled off the phone, but shockingly the good ole Postal Service. Mail delivery is asynchronous. You write a message and send it off, never knowing if you'll get a response. Sure, you *hope* you will, especially if it’s a bill to someone who owes you money. In that case, you may even *expect *that you would get a response.

Asynchronous communication is so powerful for computers because of how fast they are. Someone can answer one phone call at a time, but they can't answer 1,000,000 phone calls at a time. With asynchronous communication, you can let the messages just pile up and get back to them later. If you think about it, voicemail is just an asynchronous fallback for the telephone when the recipient is too busy to handle the call.

From these two basic forms of communication, the letter and the phone call, we've managed to create vast systems which allow for incredibly amazing experiences. Let’s look at some technologies we use every day, and how the information above works to accomplish its goals:

### Large Sale Commerce

If you've only got 50 Widgets you can sell and everyone wants them, then you better have good systems to handle the demand. From Ticketmaster's sales of the next Usher concert to Hasbro's sale of limited-edition Magic: The Gathering cards, this is a very common problem.

While it may seem like this is an ideal case of synchronous processing, this ends up being all about asynchronous communication. When you indicate you want to add something to your cart, you don't get an immediate "sure" back from these platforms. Instead, they send a request to temporarily lock up the inventory for you. Then, you've got a small window of time to check out before they release that product back into the inventory. This is all handled via asynchronous messaging.

### Streaming Media

Between Netflix, Spotify, Amazon's Prime Video, and others, these services are now the lion's share of network traffic on most networks. A popular technology conference several years ago tracked that its attendees had downloaded 11 terabytes of data from Netflix in just the three days of that conference.

Shockingly enough, almost all of these services deliver this data in a synchronous fashion. Since each consumer is at a different point in the data stream, it is simply best handled as thousands upon thousands of individual "phone calls" with the various consumers. It is the only way to ensure the highest quality experience for their customers. Now, internally these systems are vastly asynchronous, but that final mile is synchronous.

![People Pointing at Laptop](images/Designing_Distributed_Systems_-_Body_Image_-3.jpg)

So why do we need to know this? Because the most robust solutions out there are blended models. There isn't one right answer that fits all situations. Synchronous communication provides a very customized experience but does so at the expense of compute and network consumption. Asynchronous handles peak demand very well, at the cost of a small amount of overhead on every communication.

As you work with your technologists to discuss new software designs, keep in mind these trade-offs. Discuss what is most important for you and for your business. Ticketmaster never wants to sell the same seat twice, because that is considered failing for them. As such, the cost of the asynchronous system avoiding that problem for them is worth the trade-off. Netflix never wants your video to stop for buffering because that is failing for them too.

In distributed systems, as in all things, there must be balance. Discuss your business goals with your technology team. Trust that they will listen and propose a system that addresses the experience you want your users to have. [Reach out to us](https://improving.com/contact) if you want to learn more about these systems or would like to build a technology team for your organization.
