---
type: Reference
title: "Kafka Schema Evolution With Java Spring Boot and Protobuf"
resource: "https://www.improving.com/thoughts/kafka-schema-evolution-with-java-spring-boot-and-protobuf/"
author: "Scott Strzynski"
published: '2023-02-07'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

*In this blog, I will be demonstrating Kafka schema evolution with Java, Spring Boot, and Protobuf. This app is for tutorial purposes, so there will be instances where a refactor could happen. I tried to keep it simple and understandable. The code consists of two Kafka producers and two consumers. In a real-life situation, your consumer would possibly be in another app. *

*To run this app locally you will need to have a local Kafka/Zookeeper/Schema registry running. Code is available at *[*http://github.com/hal90210/spring-kafka-protobuf*](https://github.com/hal90210/spring-kafka-protobuf)* *

### Description

This app is a simple example of posting messages on a website and allowing comments on those posts. It is an incomplete app in that once a message is consumed, nothing happens. An actual app could persist to a database, or write to a KTable and later join the message to comments posting a large canonical model to a different topic. Both of those are outside the scope of this blog.

What I will demonstrate is how to evolve your domain model using Protobuf. I will start with a v1 of the schema, then add and remove fields, publish both versions of the message to a topic, and have two different consumers handle both messages safely.

Note: I have included the generated Java files from the Protobuf compiler, but you would normally have a separate repo and build process for that.

### The Schema

- WebsiteMessage
- Author
- Comment

### The Code

In this app, there are two Rest Controllers that handle Post requests for schema v1 or v2. Depending on the endpoint, either WebsiteMessageProducer.java or WebsiteMessageProducerV2.java is called to produce and publish a Protobuf message to Kafka.

Both consumers, WebsiteMessageListener.java, and WebsiteMessageListenerV2.java listen to the same topic with different group ids.

### Protobuf Message Definitions

Using an IDL (Interface definition language), Protobuf allows you the ability to create simple or complex message schemas. In this example app we will model a website that allows people (author.proto) to post messages (websiteMessage.proto) and other people to comment (comment.proto) on that post. This is a simple schema but it points out a few important features of Protobuf.

##### *websiteMessage.proto*** **

`syntax = "proto3"; `

`option java_package = "com.improving.springprotobuf.generated.v1.model"; `

`option java_outer_classname = "WebsiteMessagePayload"; `

`import "google/protobuf/timestamp.proto"; `

`import "comment.proto"; `

`import "author.proto"; `

` message WebsiteMessage { `

` string id = 1; `

` string content = 2; `

` AuthorMessage author = 3; `

` repeated CommentMessage comments = 4; `

` string topic = 5; `

`} `

This definition has a couple of required fields, syntax, and message.

The syntax field indicates what version of Protobuf you are using; in this case proto3.

The message field is the schema definition of your message. It can contain scalar variable types, custom messages, Protobuf message types, repeated variables (Lists), or enum variables. See full definition: [https://developers.google.com/protocol-buffers/docs/proto3](https://developers.google.com/protocol-buffers/docs/proto3)

The custom messages can be included in the same file or imported from other files. For your messages in external files, the import uses a relative path to the current file.

Each var declares a type, a name, and an internally used index within that message. This index cannot be changed once you start producing messages with it. It is the value that is serialized in the message instead of the field name. I will talk about modifying your schema in a later section.

The repeated type just indicates the field can contain 0 to n of the specified types in a list-like structure.

##### Options

Options allow you to help define the structure of the generated Java classes.

`**option java_package = “com.improving.springprotobuf.generated.v1.model";**`` `

Tells the protoc what package the generated classes belong to.

`**option java_outer_classname = “WebsiteMessagePayload";**`` `

The top-level message is contained in an Outerclass, protoc will default the name of this outer class to*yourMessageName*OuterClass.java. Use this option to change it to whatever you want, as you will need to reference it in your code.

### Protobuf Generated Java Classes

Adding the protoc block to our build.gradle enables the protobuf compiler to build java classes that represent the schema from the .proto files during the gradle build task.

`protobuf { `

` // Configure the protoc executable `

` protoc { `

` artifact = 'com.google.protobuf:protoc:3.0.0' `

` generatedFilesBaseDir= "$projectDir/src" `

` } `

`} `

This config will add the java classes to the src/java directory of your project.

Note: For IntelliJ users, you may get errors in the .proto files dealing with imported files. To fix this you will have to modify where the IDE looks for these files.

##### On a Mac

- Go to IntelliJ IDEA > Preferences > Language & Frameworks > Protocol Buffers
- Uncheck Configure automatically
- Add this pathfile:///your path to the project/spring-kafka-protobuf/src/main/proto
- Click Ok

You can store your .proto files anywhere, but the protoc compiler expects them to be under src/main/proto

##### WebsiteMessageProducer.java

This is the v1 Kafka message producer. It imports the Protobuf-generated Java classes

**import com.improving.springprotobuf.generated.v1.model.Comment.CommentMessage;**

**import com.improving.springprotobuf.generated.v1.model.Author.AuthorMessage;**

**import com.improving.springprotobuf.generated.v1.model.WebsiteMessagePayload.WebsiteMessage;**

The generated classes give you the ability to create objects by using the builder pattern. Here the code creates an Author and a WebsiteMessage publishing it with a kafka template.

// **Would normally look up author by id, but this is just an example app**

`AuthorMessagemessageAuthor =AuthorMessage `

` .newBuilder() `

` .setFirstName(message.getAuthor().getFirstName()) `

` .setLastName(message.getAuthor().getLastName()) `

` .setId(UUID.randomUUID().toString()) `

` .build(); `

` AuthorMessagecommentAuthor =AuthorMessage `

` .newBuilder() `

` .setFirstName("Darth") `

` .setLastName("Maul") `

` .setId(UUID.randomUUID().toString()) `

` .build();`

`CommentMessage comment = `

`CommentMessage `

`.newBuilder() `

`.setContent("Great post”) `

`.setAuthor(commentAuthor) `

.build();

// Shows adding a comment

` WebsiteMessagewMsg = WebsiteMessage `

` .newBuilder() `

` .setId(UUID.randomUUID().toString()) `

` .setContent(message.getContent()) `

` .setAuthor(messageAuthor) `

` .setTopic("test-topic") `

` .addComments(comment) `

` .build(); `

##### ***WebsiteMessageListener.java***** **

The consumer uses the same generated Java classes to deserialize the Kafka message. The type of the message is com.google.protobuf.DynamicMessage. The Protobuf generated classes allow you to instantiate an instance from a byte array as demonstrated below.

import com.improving.springprotobuf.generated.v1.model.WebsiteMessagePayload.WebsiteMessage;

import com.google.protobuf.DynamicMessage;

import com.google.protobuf.InvalidProtocolBufferException;

...

`@Service `

`public class WebsiteMessageListener implements MessageConsumer { `

` @KafkaListener(topics = "website-messages", groupId= "group_id_v1") `

` public void processEvent(ConsumerRecord&lt;String, DynamicMessage&gt; record) { `

` WebsiteMessagemessage=null; `

` try { `

` message =WebsiteMessage `

` .newBuilder() `

` .build() `

` .getParserForType() `

` .parseFrom(record.value().toByteArray()); `

` } catch (InvalidProtocolBufferException e) { `

` e.printStackTrace(); `

` return; `

` } `

` `

` logger.info(String.format("#### -&gt; Consumingmessage -&gt; %s", message.toString())); `

` logger.info(String.format("#### -&gt; Topic -&gt; %s", message.getTopic())); `

` } `

`} `

### Schema Evolution

To demonstrate schema evolution, I cheated a little. I modified the import name in the .proto files to generate two separate packages a v1 and v2. This simulates two different apps using two different versions of the generated classes.

##### **Changes**

I deleted the topic field from WebsiteMessage.To make sure no one uses the field number/name you must add them to the reserved block.

I also added an Enum field named Version. Enums must always have a zero value, it is the default value if none is provided. Here I named it UNKNOWN, but it could be named anything.

`syntax = "proto3"; `

`option java_package= "com.improving.springprotobuf.generated.v2.model"; `

`option java_outer_classname= "WebsiteMessagePayload"; `

`import "google/protobuf/timestamp.proto"; `

`import "comment.proto"; `

`import "author.proto"; `

` message WebsiteMessage { `

`reserved 5; `

` reserved "topic"; `

` string id = 1; `

` string content = 2; `

` AuthorMessage author = 3; `

` repeated CommentMessage comments = 4; `

` Version version= 6; `

`} `

`enum Version { `

` UNKNOWN = 0; `

` V1 = 1; `

` V2 = 2; `

`} `

### Forwards and Backwards Compatibility

The changes I made and the subsequent Java code below demonstrate both forward and backward compatibility.

Forward compatibility is when a producer creates a message with an older version of the schema and a consumer using a newer version of the schema can safely deserialize the message. See WebsiteMessageProducer.java producing a v1 message and WebsiteMessageListenerV2.java consuming that message with a v2 schema.

Backward compatibility is when a producer creates a message with a newer version of the schema and a consumer using an older version of the schema can safely deserialize the message. See WebsiteMessageProducerV2.java producing a v2 message and WebsiteMessageListener.java consuming that message with a v1 schema.

***WebsiteMessageProducerV2.java***

This producer will demonstrate using a newer version of the schema. In this class, we add the version field from the v2 schema

`import com.improving.springprotobuf.generated.v2.model.Author; `

`import com.improving.springprotobuf.generated.v2.model.Comment.CommentMessage; `

`import `

`com.improving.springprotobuf.generated.v2.model.WebsiteMessagePayload; `

`import `

`com.improving.springprotobuf.generated.v2.model.WebsiteMessagePayload.Version; `

`... `

`@Service `

`public class WebsiteMessageProducerV2 implements MessageProducer { `

...

// Would normally look up author by id, but this is just an example app

`AuthorMessagemessageAuthor =AuthorMessage `

` .newBuilder() `

` .setFirstName(message.getAuthor().getFirstName()) `

` .setLastName(message.getAuthor().getLastName()) `

` .setId(UUID.randomUUID().toString()) `

` .build(); `

` Author.AuthorMessagecommentAuthor =Author.AuthorMessage `

` .newBuilder() `

` .setFirstName("That") `

` .setLastName("OneCommenter") `

` .setId(UUID.randomUUID().toString()) `

` .build(); `

` CommentMessage comment =CommentMessage.newBuilder().setContent(“First!").setAuthor(commentAuthor).build(); `

` CommentMessage comment2 =CommentMessage.newBuilder().setContent("Oops I guess I wasn't first").setAuthor(commentAuthor).build(); `

// Shows adding multiple comments in one method call

` WebsiteMessagewMsg=WebsiteMessage `

` .newBuilder() `

` .setId(UUID.randomUUID().toString()) `

` .setContent(message.getContent()) `

` .setAuthor(messageAuthor) `

` .setVersion(Version.V2) `

` .addAllComments(Arrays.asList(comment, comment2)) `

` .build(); `

` `

` this.kafkaTemplate.send(TOPIC, wMsg.getId(), wMsg); `

` } `

`} `

### Running Locally

There is a docker-compose.yaml that will start zookeeper, kafka, schema registry and the app in their respective containers. You will need to build the jar first. So run

- ./gradlew clean build
- docker-compose build
- docker-compose up -d

Logging

docker logs -f spring-kafka-protobuf_app_1

Posting Json to create Kafka messages

There are two controllers that will handle the v1 and v2 messages.

##### V1 Post

`curl -X POST http://localhost:8080/v2/message/publish \ `

` -H 'Content-Type: application/json' \ `

` -d '{"content": "Look at this is a v2 message", `

` "author": { `

` "firstName": "Scott", "lastName": "Strzynski" `

` } `

` }' `

Let’s look at what each consumer logs. Since this message has a v1 schema, we expect the topic to appear, and no Version because that is a v2 concept.

To show backwards/forwards compatibility, both consumers listen on the same topic with different consumer group ids.

Here the v1 consumer prints out the deserialized Protobuf message and includes the v1 field topic:

WebsiteMessageListener :#### Consuming message

`id: "176bfa8d-474e-49c4-8c24-ad54c8b03b1e" `

`content: "hey this is a v1 message" `

`author { `

` id: "07312922-5398-43e1-93b5-9fa12a24502c" `

` firstName: "Scott" `

` lastName: "Strzynski" `

`} `

`comments { `

` content: "Great post" `

` author { `

` id: "60ca4a5f-2058-4652-a584-2d28a1e2c822" `

` firstName: "Darth" `

` lastName: "Maul" `

` } `

`} `

`topic: "test-topic" `

Here, the V2 listener displays forward compatibility, since the v2 schema topic has been removed, it does not display it. Also, since in v2 Version was added, but not set in the v1 producer, it displays the default zero value.

**WebsiteMessageListenerV2** :#### Consuming message

`id: "176bfa8d-474e-49c4-8c24-ad54c8b03b1e" `

`content: "hey this is a v1 message" `

`author { `

` id: "07312922-5398-43e1-93b5-9fa12a24502c" `

` firstName: "Scott" `

` lastName: "Strzynski" `

`} `

`comments { `

` content: "Great post" `

` author { `

` id: "60ca4a5f-2058-4652-a584-2d28a1e2c822" `

` firstName: "Darth" `

` lastName: "Maul" `

` } `

`} `

**WebsiteMessageListenerV2** :#### Message Version: UNKNOWN

V2 Post

In this post, the v2 controller will handle the post request and build a V2 message with Version, and without topic.

`curl -X POST http://localhost:8080/v2/message/publish \ `

` -H 'Content-Type: application/json' \ `

` -d '{"content": "Look at this is a v2 message", `

` "author": { `

` "firstName": "Scott", "lastName": "Strzynski" `

` } `

` }' `

You can see in the logs that the correct Version is now being displayed and there is no topic field.

**WebsiteMessageListenerV2** :#### Consuming message

` id: "33518693-f76a-4bf7-8bf7-0b9b4de6c56a" `

`content: "Look at this is a v2 message" `

`author { `

` id: "85a8a789-c30d-495e-a187-d702610a8150" `

` firstName: "Scott" `

` lastName: "Strzynski" `

`} `

`comments { `

` content: "First!" `

` author { `

` id: "71b0534e-eb0d-478c-b5f3-46984ae1715d" `

` firstName: "That" `

` lastName: "OneCommenter" `

` } `

`} `

`comments { `

` content: "Oops I guess I wasn\'t first" `

` author { `

` id: "71b0534e-eb0d-478c-b5f3-46984ae1715d" `

` firstName: "That" `

` lastName: "OneCommenter" `

` } `

`} `

version: V2

The v1 listener displaying backward compatibility does not display this version and an empty string is the value for the topic.

**WebsiteMessageListener** :#### Consuming message

`id: "33518693-f76a-4bf7-8bf7-0b9b4de6c56a" `

`content: "Look at this is a v2 message" `

`author { `

` id: "85a8a789-c30d-495e-a187-d702610a8150" `

` firstName: "Scott" `

` lastName: "Strzynski" `

`} `

`comments { `

` content: "First!" `

` author { `

` id: "71b0534e-eb0d-478c-b5f3-46984ae1715d" `

` firstName: "That" `

` lastName: "OneCommenter" `

` } `

`} `

`comments { `

` content: "Oops I guess I wasn\'t first" `

` author { `

` id: "71b0534e-eb0d-478c-b5f3-46984ae1715d" `

` firstName: "That" `

` lastName: "OneCommenter" `

` } `

`} `

**WebsiteMessageListener** :#### Topic:

### Schema Registry

The Protobuf schema is added to schema registry like Avro.

http://localhost:8081/subjects

`[ `

`"author.proto", `

`"comment.proto", `

`"google/protobuf/timestamp.proto", `

`"website-messages-value" `

`] `

http://localhost:8081/subjects/website-messages-value/versions

`[ `

` 1, `

` 2 `

`] `

http://localhost:8081/subjects/website-messages-value/versions/2

`{ `

` "subject": "website-messages-value", `

` "version": 2, `

` "id": 4, `

` "schemaType": "PROTOBUF", `

` "references": [ `

` { `

` "name": "google/protobuf/timestamp.proto", `

` "subject": "google/protobuf/timestamp.proto", `

` "version": 1 `

` }, `

` { `

` "name": "comment.proto", `

` "subject": "comment.proto", `

` "version": 1 `

` }, `

` { `

` "name": "author.proto", `

` "subject": "author.proto", `

` "version": 1 `

` } `

` ], `

` "schema": "syntax = \"proto3\";\n\nimport \"google/protobuf/timestamp.proto\";\nimport \"comment.proto\";\nimport \"author.proto\";\n\noptionjava_package = \"com.improving.springprotobuf.generated.v2.model\";\noptionjava_outer_classname = \"WebsiteMessagePayload\";\n\nmessageWebsiteMessage {\n reserved 5 to 6;\n reserved \"topic\";\n\n string id = 1;\n string content = 2;\n .AuthorMessage author = 3;\n repeated .CommentMessage comments = 4;\n .Version version = 6;\n}\nenum Version {\n UNKNOWN = 0;\n V1 = 1;\n V2 = 2;\n}\n" `

`} `

### Conclusion

Using Protobuf provides the developer the ability to build an evolvable schema like Avro. Different from Avro, it uses an IDL instead of a JSON. Spring Boot and Gradle provide a good framework to allow the developer to write applications quickly and not worry about problems from a changing schema.
