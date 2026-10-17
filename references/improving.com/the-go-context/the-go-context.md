---
type: Reference
title: "The Go Context"
resource: "https://www.improving.com/thoughts/the-go-context/"
author: "Paul Ferguson"
published: '2023-04-11'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

I am a long-time Java developer that had the opportunity to learn Go while developing an application for my client. There are many similarities that made the experience fairly easy, but there were a few gotchas that I discovered along the way. The one I want to talk about now is the Go context.

In a Java application when a request comes in it is completely processed and a response is returned.

In a Go application, there is a context that makes things more interesting. A context carries deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes. When working with a request it can be used to cancel or timeout the request. A cancel can happen for many different reasons. The user could close their browser or click cancel as the request is being processed. There could be a bad internet connection or some other network issue. A client could timeout deciding the request is taking too long and close it. Regardless of the reason the context will signal it is done. This means work that has not yet been completed can be skipped.

Some packages for databases, http clients and others will require a context to be passed into them. The others will likely have a way to set it. I didn’t understand why initially. There was a context already set on the request so I just passed it along. When a context would get canceled we started seeing context-canceled errors. This is because these packages would act on that done context signal by stopping all their processing and returning an error.

`ctx := request.Context() `

`*// lookup a person from the database*`` person, err := databaseCall(ctx) `

`… `

`*// databaseCall Looks up a person from the database.*`` `

`funcdatabaseCall(ctxcontext.Context) (Person, error) { `

` logInfo(ctx, "Making the database call") `

` var person Person `

` ``*// pause for a bit to allow the context to be cancelled*`` `

`* *``err := pause(ctx) `

` if err != nil { `

` return person, err `

` } `

` ``*// the popular pgxpostgres database package requires a context to be set in most operations*`

`* *``connection, err := pgx.Connect(ctx,`

`"postgres://postgres:postgres@localhost:5432/postgres")`

` if err != nil { `

` ``*// in addition to the usual errors if the pgx package notices the context is done it will return an error*`` `

`* *``return person, err `

` }`

` defer connection.Close(ctx) `

` ``*// query the database for a person and populate their struct values*`` `

`* *``err = connection.QueryRow(ctx, "select name from`

`people").Scan(&person.Name) `

` return person, err `

`} `

*To view the complete code check out my example application on GitHub at *[*https://github.com/paul-ferguson/the-go-context*](https://github.com/paul-ferguson/the-go-context)

Notice how this application checks to see if the database call returns an error. If there is an error we check to see if the context is done. If it is done the application does no further processing and then just returns. It doesn’t even need to return a http error code nor any JSON response.

If you want a Go application to function like a Java application you need to use the appropriate context. Let’s say we have a REST endpoint that is processing a post-call to save some data. We will want that to get completely processed and persisted to the database regardless if the request context is cancelled. In this case, we can use *context.Background()* to create a new context that can never be canceled. I have shown an example of this below. I also included in the code comments the `*context.WithCancel()*``, ``*context.WithDeadline()*` or `*context.WithTimeout()*`. They respectively define a cancel method and a deadline or timeout/duration that will trigger the context done signal. A `context.Background()` should only be used in certain scenarios: main functions, initialization, and tests, and as the top-level Context for incoming requests. Our use case is the latter. In most situations, it is best practice to use one of the other options.

*ctx:= context.Background() *

*/* thy this: Try these other options instead: *

*// this returns a context and a function we called cancel *

*ctx, cancel := context.WithCancel(request.Context()) *

*// calling cancel will trigger the done signal *

*cancel() *

*// this will trigger a timeout after 2 seconds *

*ctx, cancel := context.WithTimeout(request.Context(), time.Second * 2) *

*// from the Go doc: Even though ctx will be expired, it is good practice to call its cancellation function in any case. Failure to do so may keep the context and its parent alive longer than necessary. defer cancel() // this will trigger a timeout after a time that is 2 seconds in the future ctx, cancel := context.WithDeadline(request.Context(), time.Now().Add(time.Second * 2)) defer cancel() *

**/ *

*… *

`*// restCall Looks up a person by making a rest call.*`` `

`funcrestCall(ctxcontext.Context) (Person, error) { `

` logInfo(ctx, "Making the rest call")`

` var person Person ``*// create the get request to the server side endpoint*`` `

`* *``request, err := http.NewRequestWithContext(ctx, "GET",`

`"http://localhost:8080/server-side-get", nil) `

` ``*/**`` `

`* try this: If we don't pass the context along the request will not be cancelled when a done signal occurs. The*`` `

`* request will be fully processed wasting resources.*`` `

`* request, err := http.NewRequest("GET", "http://localhost:8080/server-side-get", nil)*`` `

`* */*`` `

`* // pass along the request id in the header allowing us to trace this request*`` `

`* *``request.Header.Add(requestIDHeaderKey, ctx.Value(requestIDContextKey).(string)) `

` ``*// make the request*`` `

`* *``response, err := http.DefaultClient.Do(request) `

` if err != nil { `

` ``*//todo*`` `

`* *``return person, err `

` } `

`*// read the full response body*`` `

`* *``body, err := io.ReadAll(response.Body) `

` if err != nil { `

` return person, err `

` } `

`*// close the response body*`` `

`* *``err = response.Body.Close() `

` if err != nil { `

` return person, err `

` } `

` ``*// unmarshal the response body contents to a person struct*`` `

`* *``err = json.Unmarshal(body, &person) return person, err `

`} `

*To view the complete code check out my example application on GitHub at *[*https://github.com/paul-ferguson/the-go-context*](https://github.com/paul-ferguson/the-go-context)

Finally, to be complete I should show how the context can be used to pass request-scoped values across API boundaries and between processes. I have previously used this for logging common values, like a request id. Here is an example.

`const requestIDHeaderKey= "request-id" `

`const requestIDContextKey= contextKey(requestIDHeaderKey) `

`… `

`*// set the request id as a value in the context*`` `

`requestId:= request.Header.Get("request-id") `

`if requestId== "" { `

` ``*// no request id set so create a unique one*`` `

`* *``requestId= uuid.New().String() `

`} `

`ctx= context.WithValue(ctx, requestIDContextKey, requestId) `

`logInfo(ctx, "Get was called") `

`… `

`*// here are many logging packages we could have used, but rolling our own for more clarity in this example*`

`funclogInfo(ctxcontext.Context, message string) { `

` fmt.Println("info", message, ctx.Value(requestIDContextKey)) `

`} `

*To view the complete code check out my example application on GitHub at *[*https://github.com/paul-ferguson/the-go-context*](https://github.com/paul-ferguson/the-go-context)
