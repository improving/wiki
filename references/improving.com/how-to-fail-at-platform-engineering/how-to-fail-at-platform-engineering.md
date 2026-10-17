---
type: Reference
title: "How to Fail at Platform Engineering"
resource: "https://www.improving.com/thoughts/how-to-fail-at-platform-engineering/"
author: "Atulpriya Sharma"
published: '2025-11-26'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

A team of DevOps professionals working at DevOpsX had high expectations from the platform their organization just launched. The platform had promised to revolutionize workflows related to Git, CI/CD, testing, and a few others that the team used along with simplifying the entire process.

The organization launched it with much fanfare, but the platform turned out to be a disappointment. The platform’s complexity and non-intuitive design proved to be confusing to the developers who found it difficult to devise a workflow. Whether it was creating or triggering a pipeline or managing deployment environments, the platform proved to be a roadblock.

While this is a hypothetical scenario, this can very well happen in real life too. Even the most promising platforms built with the latest tools and technologies can falter. As per the [State of Platform Engineering Report 2023](https://www.puppet.com/resources/state-of-platform-engineering), 32% of respondents feel that poor communication between teams can lead to the failure of the platform.

In this blog post, we’ll delve into the reasons that lead to the failure of platforms. Or, in other words, how to fail at platform engineering.

## 6 Reasons Why Developer Platforms Fail

### Product Misfit

Product misfit refers to the situation where the platform’s design and functionality do not match the needs and expectations of its target audience, i.e., developers for whom the platform is built. A few reasons why product misfit occurs could be:

- When developers are not involved in the process of building platforms, the end result is often a platform with features that the developers don’t need or use at all. This leads to a significant portion of the platform’s capability going unused.
- A platform that doesn’t cater to the needs of the developers often fails to align with the goals of the organization. This leads to a slowdown in the development process, lesser interest from the higher-ups, and even financial bottlenecks in some cases.

For example, a platform was designed to automate CI/CD integrations. However, it failed to consider the multi-cloud environments that the development teams used, and hence, the platform had compatibility issues with these complex setups. This misfit can lead to great complexity and slower deployments.

To overcome the issue of product misfit, the best thing is to involve developers in the early stages of building the platform. Conduct surveys and interviews to understand the needs of the developers that will form the base of your platform.

![Asset - Image 1 - How to Fail at Platform Engineering](images/AdobeStock_649621323.jpeg)

### Overly Complex Design

One of the common reasons why platforms fail is because of the unnecessary complexity they bring. The platform engineering team builds the platform with tons of features, aiming to solve all the use cases, which adds an element of confusion among the developers and sometimes even hides the actual purpose of the platform. Deviation from the industry standards and best practices can also aggravate the issue.

A platform built for flexibility and versatility often comes with a lot of customization options. However, the overwhelming number of options adds to the overall complexity of the platform. Further, if such a platform used non-standard scripting languages to configure those settings, it could lead to a steeper learning curve for the developers.

As they say, “Go by the book”, building platforms with simpler interfaces following industry standards is a great way to keep things simple.

### Swiss Knife Syndrome

When platform engineer teams set out to build platforms, they often want to build a platform that solves all the problems, which eventually turns out to be the biggest problem. While the intent of building an all-in-one platform is great, it often leads to a bloated platform filled with an array of features.

This results in a challenging user experience as users often struggle to navigate through the platform and find the things they need. Further, such a platform also has issues integrating with other platforms, which is often a critical part of any platform.

For instance, such an all-in-one platform would want to have the capability of integrating with all the CI/CD tools. However, in the process of doing that, the platform will introduce a lot of complexities in terms of configurations, which will make it difficult for developers to connect to their preferred platform.

Instead of focusing on building platforms that solve all the problems, it’s better to focus on building a platform that solves one problem completely. Building specialized platforms that cater to the needs of your developers will help in overcoming the Swiss knife syndrome.

One way to achieve that is by treating your platform as a product, which can help avoid this problem as you keep your developers’ requirements at the center and build the platform around them.

### Insufficient Documentation

Complete documentation is vital for all products, including your platforms. Without this, developers will face hurdles in troubleshooting issues and navigating their way through the platform. There might be situations where the developers attempt to decipher complex processes independently, leading to cognitive load.

Moreover, inadequate, incomplete, and outdated documentation can lead to inefficiency and may even lead to a huge influx of support tickets, causing unnecessary disruptions.

For instance, a developer required a custom cloud instance for a specialized project. However, the platform’s documentation didn’t provide a comprehensive guide on how to request such a custom instance. Frustratingly, the developer had to reach out to colleagues and conduct extensive research to understand the process, which led to a significant waste of time.

To prevent such situations, it’s important to have up-to-date documentation. If required, have a dedicated team that ensures the upkeep of the documentation.

*(Pro Tip: Adding a search feature to the documentation can help save valuable time.)*

![Asset - Image 2 Why Successful Software Projects Require More Than Technical Skills](images/AdobeStock_127521194.jpeg)

### Siloed Development

The two major stakeholders in platform engineering are the developers and the platform engineering team. While the former uses the platform, the latter builds and maintains it. More often than not, both these teams are working in silos and seldom have visibility into what the other team is doing.

Platform teams may build features without insights into developers’ evolving needs, while development teams might struggle to align their work with the platform’s capabilities. This disconnect often leads to inefficiencies, duplicated efforts, and a failure to fully harness the platform’s potential.

To avoid such mishaps and foster robust collaboration, organizations can enable common collaboration channels where both the platform and development teams can interact, share ideas, and solve problems. There can also be regular meetings to discuss ongoing projects and share updates and concerns.

### Stagnant Platform

Change is the only constant. This is a common phrase that all of us are familiar with. This applies to everything, even platforms. A platform that was launched with fanfare and loaded with all the bells and whistles needs to keep up with the changing requirements of the teams.

For instance, if the platform fails to provide the latest updates for tools and services it provides, the development team will find it difficult to use and eventually will stop using the platform.

The platform should also be constantly evolving in terms of the features and services it provides. Anything that helps a developer improve their work should be considered and provided via the platform.

For instance, if the development team uses MongoDB service for their applications, the platform needs to ensure that the latest version of the service is available to the users. If the platform fails to provide this, the developers will find it difficult to keep their applications up-to-date.

One of the best ways to keep your platform up-to-date is by having a roadmap. That way, you know what features you need to add to your platform. Also, having regular interaction with the development team can help the platform team understand the changing requirements of the developers and pick the most impactful items first.

## Summary

In this blog post, we discussed some of the common reasons why a platform could fail. Whether you’re developing or using a platform, it’s imperative to understand and address the unique needs of your developers. You can overcome most of these challenges by treating your platform as a product. By applying the product mindset to your platform, you chalk out a clear path for your platform and its future.

Exploring Platform Engineering? [Learn more about what we do at Improving by reaching out to us.](https://improving.com/contact)
