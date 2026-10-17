---
type: Reference
title: "Natively Compiled Java on Google App Engine"
resource: "https://www.improving.com/thoughts/natively-compiled-java-on-google-app-engine/"
author: "Brendon Anderson"
published: '2022-06-14'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Google App Engine is a platform-as-a-service product that is marketed as a way to get your applications into the cloud without necessarily knowing all of the infrastructure bits and pieces to do so. Google App Engine has been around since 2008 and was one of the first cloud services available from Google. It initially supported Python, but soon expanded to Java and now supports many languages like Go, .Net, Node.js, and others. The App Engine Standard Environment manages running instances for you by scaling from zero instances (in the case of no traffic) to quickly scaling up to meet any demand level. An application with low traffic can be run for free, which is great for prototyping or building proof-of-concept applications.

Recently, while reading about natively compiled Java, I came across a tidbit that said that Java compiled as a native binary can be deployed to the App Engine Standard Environment. So, I thought I’d investigate further since I was only aware of deploying a war or jar type artifact to App Engine.

Enter Micronaut

If your application deployed on App Engine is not serving any requests, it is scaled down to zero instances automatically. When a request comes in, App Engine will start up an instance for you automatically. You want your application to start quickly so that first request doesn’t have to wait too long to be served. Even a moderately sized Spring application can take many seconds to start up. Another framework that touts its ability to start up quickly is Micronaut. Micronaut’s fast startup speed is attributed to how it does all of its dependency injection and AOP type operations at compile time. Spring does all of this at runtime. Even better, Micronaut has a lot of support for building natively compiled binaries using GraalVM, which makes startup time and memory consumption even lower. Another benefit of Micronaut is that it looks a lot like Spring when developing an application, so it is a fairly easy transition for those Spring developers out there.

Please Note

Before going any further into this post, I should note that I did all development on Linux. The binaries compiled on MacOS or Windows probably will not work on Google App Engine. In a real environment, a CI/CD pipeline will exist where the binary is built using Linux in a Docker container.

Prerequisites

Several prerequisites are needed to get started, some of which may already exist for you. I will not go into detail on how they are installed, but will have links available to get you started.

- SDKMan – A great tool to have installed anyway!
- GraalVM – Install with SDKMan (version may be different)
- **sdk install java 22.1.0.r17-grl**
- The native-image tool from GraalVM
- **gu install native-image**
- Gradle – Install with SDKMan
- **sdk install gradle**
- Micronaut CLI – Install with SDKMan
- **sdk install micronaut**
- zlib and musl
- Create a GCP account and an App Engine project. If you are given a choice, choose the “standard” environment (instead of “flex”). There are some basic instructions here.
- gcloud SDK CLI

Code It Up

The full source code of my example application can be found on GitHub, but I will walk through it and point out a few gotchas.

Use Micronaut to create your application:

**mn create-app com.improving.native-on-app-engine --build=gradle --lang=java --features=graalvm**

At this point, you will have a shell of an application with most of what you will need.

The first step is to create a simple controller. In my code, I’ve injected a property to indicate which profile it is reading from. Micronaut profiles work similarly to Spring by naming the application.yml files appropriately.

`@Controller("/hello") public class HelloController { @Inject // required for private variables when natively compiled @Property(name = "app.greeting") private String greeting; private final String baseText; public HelloController(@Property(name = "app.basetext") String txt) { this.baseText = txt; } @Get @Produces(MediaType.TEXT_PLAIN) public String index() { return baseText + " " + greeting; } }`

All of this should be unremarkable except for the @Inject annotation. When injecting private variables, the @Inject annotation is required for native compiling (not needed for jar/war type artifacts). Other ways around this are to have a public setter or use constructor injection, like I have done here. Setting the variable to package-private is another option. I think in most cases, constructor injection is the best route.

The build.gradle file also needs a few amendments. It will need this plugin:

`id("com.google.cloud.tools.appengine") version '2.4.2' `

These additional libraries:

`annotationProcessor("io.micronaut:micronaut-graal") `

`nativeImageCompileOnly("com.google.cloud:native-image-support:0.14.1") `

`annotationProcessor("io.micronaut:micronaut-inject-java") `

Also this additional configuration needs to be added:

`appengine { stage.artifact = "${buildDir}/native/nativeCompile/native" deploy { projectId = "YOUR_PROJECT_ID_HERE" version = "1" } ` `} `

`graalvmNative { binaries{ main { imageName.set('native') buildArgs.addAll(["--verbose", "--static", "--libc=musl"]) } } } `

The build args in the **graalvmNative** config tell it to statically compile the binary using the musl library for libc. This ensures it will run anywhere no matter the version of libc/glibc installed on the host machine (as long as it is Linux). I ran into problems not statically compiling the code. The version of glibc on App Engine was different than the version on my Linux laptop so it wouldn’t start up on App Engine. Statically compiling the binary this way puts everything into the binary that is needed. It creates a larger binary, but also increases compatibility so it will run in more places.

See settings.gradle for some additional configuration related to plugins.

Create a `src/main/appengine/app.yml `file with the following contents:

`runtime: java11 entrypoint: ./native `

At this point check to make sure things are running without the native compile. The application should start up by running `./gradlew run`. Using curl or Postman to hit the URL http://localhost:8080/hello should return the message “**Hello World base**,” unless you have changed the profile to use one of the other property files (by setting the environment variable `MICRONAUT_ENVIRONMENTS=local`). If that all works as expected, let’s move on to the native compile.

Native Compile

Using the command `./gradlew nativeCompile` should build a binary. It is a much longer build compared to building a jar file. The new binary should be located at **/build/native/nativeCompile/native**

To test the binary, run the command` ./build/native/nativeCompile/native `

You should notice the startup times drop from 500-600ms to less than 100ms.

Deploy to the Cloud

Back when you created your GCP project, you were given a project ID. This ID needs to go in the `appengine` configuration in the` build.gradle` file. If everything is set up, you can deploy the binary using `./gradlew appengineDeploy` which will take a few minutes.

When the deployment completes, it will give you a base URL for your application in the terminal. If you take that URL and add` /hello` to the end you should see the message “Hello Cloud GCP.” It picked up the correct profile automatically based on its environment (`application-gcp.yml`)! The first time you hit your endpoint, it might take 1500ms actual time but subsequent requests should take ~50ms. I believe most of that 1500ms is overhead with App Engine doing what it needs to do to get your application up and running. If you look at the actual logs in GCP you will see that your app started up in 100-200ms.
