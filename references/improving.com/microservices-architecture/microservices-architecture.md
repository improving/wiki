---
type: Reference
title: "Microservices Architecture: Moving Past the Buzz Words"
resource: "https://www.improving.com/thoughts/microservices-architecture/"
author: "Robyn Fuentes"
published: '2021-08-03'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Over the past several years, we have worked with an increasing number of clients asking us to help them get started with microservices because they are either looking to transform their architecture (often a monolith) or planning for a new project. In a lot of these cases, we have found that the term “microservice” is often used because it is the known solution for building scalable systems. However, this term doesn’t always come with a complete understanding of the implications of this new direction.

The intent of this article is to help those considering a microservice architecture understand what parts of the application are most heavily impacted by the new design process, then make an educated decision. We will also cover how cloud offerings can be leveraged in this space, and some basic steps to get started down the road of microservices.

## Advantages and Disadvantages of Microservices

Microservices have significant advantages and disadvantages. Weighing the positives and the negatives will help us determine if the benefit outweighs the cost and if the disadvantages are something your organization can live with long term. Let’s dig into the disadvantages and advantages, and see if microservices are the right answer for your problem space.

## Disadvantages of Microservices

Several of the disadvantages of microservices are intentional to the design. A desire to avoid these disadvantages can lead to larger problems and sometimes land you with a “microservice-monolith”, suffering the worst of both approaches.

When considering each of these disadvantages, think about what patterns and/or processes your team or organization will need to adopt to ensure you are ready to handle them without falling back into old habits. An example of this is how enhanced security measures make access more difficult but can remove the single point of failure in protecting your assets.

### 1. THE STRUCTURAL COMPLEXITY OF THE MICROSERVICE SOLUTION GROWS QUICKLY

In a microservice architecture, adding behaviors to the system and expanding the problems it is solving, means adding additional structures and services to accomplish it.

The maintenance of this structure becomes a growing problem space. A lot of this additional complexity can be handled with the right DevOps foundation and automation tools. But without them, it can become a maintenance nightmare.

### 2. WHEN SHARING OF INFORMATION AND DATA BETWEEN MICROSERVICES BECOMES A CONCERN

When services need data from multiple domains to accomplish a task, we are faced with the implementation of integration patterns (a good topic to explore if deciding to implement microservices).

One of the most common integration patterns is the double retrieval of data or duplicate storage. We end up trading storage space for behavior separation. Trying to avoid this disadvantage can create much larger issues and result in a single point of failure for the entire system.

### 3. MODIFICATION OF CROSS-CUTTING BEHAVIOR INVOLVES MULTIPLE MICROSERVICES

When dealing with cross-cutting concerns like logging, auditing, or security, we need to design a solution that works across multiple services or replicates these behaviors through a shared set of utilities. If we share that set of utilities, we can create constraints on change and deployment.

It becomes important to create utilities with appropriate versioning that doesn’t couple your system unnecessarily to other versions (framework version, for example) or have crippling breaking changes that restrict adoption.

## Advantages of Microservices

Microservice advantages are no less intentional in design than disadvantages.

### 1. SEPARATION OF CONCERNS IS STRUCTURAL

When building complex systems, avoidance of unintended consequences takes significant care and diligence. Often this relies on the knowledge and discipline of the software development team.

With microservices, some of this complexity is structural and can be constrained. API contracts can be versioned and deprecated as needed. Portions of the system can be versioned multiple times faster than others. This structural complexity is also more easily automated with modern DevOps tools.

### 2. SCALE IS TARGETED

Systems built with a microservices architecture can have targeted scale applied to certain functions by scaling the hardware for that set of services. This allows for performance and burst of demand to be more readily handled, often in an automated fashion using modern cloud providers.

### 3. COMPLEXITY CAN BE DISPERSED TO MANY TEAMS

Working with monolith systems is tough, especially for large development groups of multiple teams. The architecture of microservices helps to somewhat compartmentalize this while allowing multiple teams to be working on a large-scale system with more flexibility and less conflict.

This is not to say they are entirely isolated, but it is significantly more so than a single code base of a large application developed as a monolith.

## Where to Start? Maybe the Beginning

When considering a shift in architecture, it is important to look at the decision-making and design processes. If we approach a shift in architecture but don’t change how we design, then we will likely recreate worse problems than we have today. Why worse? Because today we have systems that are based on those processes.

In contrast, the future we are considering will likely have conflicts between the design principles and the implemented processes. The design approach that we lean on heavily for transforming to microservices is Domain Driven Design.

If you haven’t explored Domain Driven Design, please check out [this book by Eric Evans](https://www.amazon.com/dp/0321125215/ref=cm_sw_em_r_mt_dp_9T032QNWW6RCC6JV8SHQ). It gives a great set of tactics and steps to make progress. In short, it is a design structure that helps to decompose large realms of complexity into smaller realms. This has the benefit of limiting the scope of complexity and allows for variation of design in the problem spaces. When we separate the problems into business domains and then separate the domains' connections to the root concepts, each of these domains can be influenced by the others, but not controlled.

The similarity in terminology and responsibility segregation when going from design approach to implementation that Domain Driven Design gives us, allows us to remove communication complexity and get to the root of the issues rapidly.

Without this match-up, the developers are forced to translate the intent into another mental model. That translation comes with effort, confusion, and often a loss of fidelity.

## Key Components of Successful Microservices Teams

When we look at moving to microservices, there are some common themes that we see in successful teams. Let’s dig into those now.

### 1. GOOD AUTOMATION AND DEVOPS PROCESSES

It’s not easy to deploy multiple services in multiple versions and also ensure that reliability is not impacted negatively. Teams that make this concern a first-class citizen of their development process have a significantly higher success rate than most (not just in microservices). The basics of a build and release pipeline into test and production environments can make a world of difference.

### 2. DISCIPLINED DEVELOPMENT TEAMS

Collaboration, design, testing, and ultimately the success of the product, can be summarized in the discipline of the development team. There will be a ton of shortcuts along the way that can degrade the value of the system, and lead to long-term technical debt. If the team cannot see and avoid those shortcuts, they will struggle. This sounds simple, but when the “short way” takes 2 hours and the “right way” takes 6, even a product owner will push for the shortcut.

Most of the time this is a trade-off that is not understood and leads to significant re-work in the future. Design and implementation discipline for a team is a rare thing to find, but when done correctly leads to amazing results.

### 3. TEST, TEST, AND TEST SOME MORE

Decomposing complexity does not remove the complexity, and we need to add more testing than most teams like to do. The definitions that tests convey often find mistakes before they are ever run. The edges and boundary cases of one service become the constraints of the services it interacts with. A solid test suite that is well-maintained and growing will solve many problems before they happen.

### 4. GOOD MESSAGING AND INTEGRATION PATTERNS

Distributed systems are hard to build and understand without clear patterns. This is one of the biggest influences for successful teams. You can get a jump start with the right framework and some knowledge. Take a look at [MassTransit](https://masstransit-project.com/) and [Enterprise Integration Patterns](https://www.amazon.com/dp/0321200683/ref=cm_sw_em_r_mt_dp_Y1H1N27FBBXVSA4SKRNY?_encoding=UTF8&psc=1). Both the framework and the book will help you get started the right way.

If you are feeling the pain of an architectural change gone wrong or want to avoid that pain altogether, feel free to [give us a shout](https://improving.com/contact). We’d love to share our experiences with you.
