---
type: Reference
title: "Unleashing Feature Flags onto Kafka Consumers"
resource: "https://www.improving.com/thoughts/unleashing-feature-flags-onto-kafka-consumers/"
author: "Matthew Schroeder"
published: '2022-05-31'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Feature Flags are a tool to strategically enable or disable functionality at runtime. They are often used to drive different user experiences but can also be useful in real-time data systems. In this post, we’ll walk through using feature flags to pause and resume a Kafka Consumer on the fly.

You may be wondering, why not just shut down the consumer(s) to “pause” processing? This approach is 100% effective and accomplishes the end goal of stopping consumption. However, there are downsides when dealing with a large-scale consumer architecture.

- **Rebalances **- depending on the layout of your consumer group and the number of partitions, the rebalance process that is triggered when a consumer leaves the group can be painful and time-consuming.
- **Lack of Granularity **- if the consumer is reading multiple topics, you shut down consumption of everything. There is no in-between.
- **Responsive Processing **- to re-enable processing, all of the consumers have to start back up and rebalance partitions. With 100+ consumer instances, this can be time-consuming.

Before getting into how to incorporate Feature Flags we should look at the functionality that already exists in the Kafka client libraries to dynamically pause and resume processing. We’re already closer to the end goal than you may have realized.

## Pausing Kafka Consumers

The Kafka Consumer client has the functionality to fetch assigned partitions, pause specific partitions, fetch currently paused partitions, and resume specific partitions. These methods are all you need to pause and resume consumption dynamically.

Let’s look closer at these operations.

- KafkaConsumer.assignment(): returns the currently assigned topic partitions in the form of a Set of TopicPartition. The TopicPartition contains two primary properties, the topic name as a String and the partition as an int.
- KafkaConsumer.pause(Set of TopicPartition): suspends fetching from the provided topic partitions. Consumer polling will continue, **which is key to keeping the consumer alive **and avoiding rebalances. However, future polls will not return any records from paused partitions until they have been resumed.
- KafkaConsumer.paused(): returns the topic partitions that are currently assigned and in a paused state as a result of using the pause method.
- KafkaConsumer.resume(Set of TopicPartition): resumes fetching from the provided topic partitions.

### Option 1: Pause the World

The simplest way to pause processing is to pause everything. The snippet below illustrates this.

`*// get all assigned partitions for the consumer Set<TopicPartition> assignedPartitions = consumer.assignment(); *`

`*// pause all assigned partitions Set<TopicPartition> pausedPartitions = consumer.pause(assignedPartitions); *`

`*// resume all paused partitions consumer.resume(consumer.paused()); *`

`*// you could also resume the consumer.assignment() since everything is paused consumer.resume(consumer.assignment()); *`

### Option 2: Selective Pause

It’s helpful to have the big red button to shut down all processing shown previously but it would be more helpful if we could control things at a more granular level.

The next snippet shows what pausing the partitions for a single topic might look like.

`*// assume consumer is subscribed to demo.topic.name && another.topic.name String pausedTopic = "demo.topic.name"; *`

`*// // PAUSE // *`

`*// filter out the assigned partitions for the topic being paused *`

*`Set<TopicPartition> partitionsToPause = consumer.assignment() .stream() `*

*` .filter(tp -> pausedTopic.equals(tp.topic())) .collect(toSet()); `*

*`Set<TopicPartition> pausedPartitions = consumer.pause(partitionsToPause); `*

*`// // RESUME // `*

*`// filter out the paused partitions for the topic being resumed Set<TopicPartition> partitionsToResume = consumer.paused() `*

*` .stream() .filter(tp -> pausedTopic.equals(tp.topic())) .collect(toSet()); `*

*`consumer.resume(partitionsToResume); `*

## Unleash the Flags

After seeing the last snippet, you can probably guess how Feature Flags enter the picture to dynamically supply the “pausedTopic” variable from the snippet.

With a simple Feature Flag naming convention such as topic_{topic-name-here} , the application can pull all of the flags and filter out only those that it cares about.

The pseudo-code below shows what this might look like.

`*// two topics that this consumer cares about List assignedTopics = ["demo.topic.one", "demo.topic.two"] *`

`*// all of the feature flags List flags = [ *`

`* "topic_demo.topic.one", "ui-feature-flag", "topic_important.topic" *`

`*] *`

`*// the flags that this consumer actually cares about List assignedTopicFlags = toggles *`

`* .stream() .filter(t -> t.startsWith('topic_') && assignedTopics.contains(getTopicName(t)) .collect(toList()); *`

`*// assignedTopicFlags = ["topic_demo.topic.one"] *`

Now that we can picture how this works, let’s look at integrating Unleash, an open-source Feature Flag solution. You can substitute any feature flag product in place of Unleash.

## Unleash

There are many Feature Flag options on the market but Unleash is an open-source feature management platform that has worked well for me. It’s gained enough traction that Gitlab now offers it as a built-in service and as of Gitlab 13.5, it’s available in all tiers. A full list of capabilities can be found here.

Connecting applications to Unleash is simple. Select the Unleash SDK that aligns with your application and configure the Unleash URL and Instance ID. If you’re using Gitlab, there are clear instructions on integrating feature flags with your application.

Below is an example of configuring the Unleash client in a Java Spring Boot application.

*/** * Configure the client that connects to Unleash if unleash.enabled is "true" **/ @Bean @ConditionalOnProperty(value = "unleash.enabled", havingValue = "true") Unleash defaultUnleash() { *

* UnleashConfig config = UnleashConfig.builder() .unleashAPI("<http://unleash-api.com>") .instanceId("asdf-123") .appName("unleash-demo") .environment("development") .fetchTogglesInterval(10) *

* .subscriber(new Log4JSubscriber()) .build(); *

* return new Unleash(config); } *

*/** * If unleash.enabled is false, the above bean will not be created. * In this scenario, the FakeUnleash client will be injected into the * app context for use. This is helpful for local development. **/ @Bean @ConditionalOnMissingBean(Unleash.class) Unleash fakeUnleash() { *

* return new FakeUnleash(config); } *

## Fetching Feature Flags

We’ve looked at the pause/resume functionality and how a simple feature flag naming convention can be used to target the topics that should be paused/resumed. Now let’s tie the two together and look at strategies for fetching and applying the toggles.

### Option 1: Poll Loop

The simplest option is to integrate the feature flag checks right into the poll loop. Unleash will be refreshing the flag states in a background thread so each check will be hitting cache when looking at the latest values and seeing what, if anything, needs to be paused. The benefit of this approach is that everything happens right on the polling thread which is important since the consumer is not thread-safe.

`*// simplified consumer try { *`

`* while (true) { // fetch latest flag values and apply accordingly applyFeatureFlags(consumer); *`

`* ConsumerRecords<String, String> records = consumer.poll(100); for (ConsumerRecord<String, String> record : records) { *`

`*// logic *`

`*} *`

`*} } finally { *`

`* consumer.close(); } *`

### Option 2: UnleashEvent Subscriber

Unleash has an internal eventing design that makes it easy to subscribe to the events that get triggered after refreshing the toggles. This will be the most up-to-date representation of the flag states because the event is fired immediately after the cache is updated.

As mentioned in option 1, Consumers are not thread-safe, so you have to handle consumer operations appropriately and run the consumer pause operations on the polling thread.

The main benefit of this is that it doesn’t clutter the poll loop with responsibilities. Polls continue to happen and if things are paused, they won’t fetch records. If things are active, they will fetch records.

*`/** * Custom subscriber that will be notified on all UnleashEvents. * The extended Log4JSubscriber will log out the events that are not * handled in this extension. **/ public class KafkaUnleashSubscriber extends Log4JSubscriber { `*

* **`@Override public void on(@NotNull UnleashEvent event) { `*

*` // many events come through here, we only care about responses if (event instance of FeatureToggleResponse) { `*

*` // event has ALL toggles, filter out those you care about `*

*` // apply toggles to consumer `*

*` } `*

*` } `*

*`} `*

## Don’t Forget the RebalanceListener

The final piece that needs to be accounted for is the **ConsumerRebalanceListener**. With multiple consumers running in a group, each will be responsible for pausing their assigned partitions. If a consumer dies, their assigned partitions will automatically rebalance to the other consumers in the group. However, the consumer receiving the newly assigned partitions has no awareness of their previous state (paused/active) so they will be active after the assignment.

The RebalanceListener is your hook in this rebalance lifecycle to pause partitions before consumption begins and avoid accidentally consuming a topic that should be paused.

With all of the components that have been built already, it should be pretty simple to create a listener that ties it all together and keeps partitions paused if they need to be.
