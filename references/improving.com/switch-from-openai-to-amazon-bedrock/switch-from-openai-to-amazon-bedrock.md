---
type: Reference
title: "Switch from OpenAI to Amazon Bedrock"
resource: "https://www.improving.com/thoughts/switch-from-openai-to-amazon-bedrock/"
author: "Ravjot Brar"
published: '2025-04-04'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

## What is Amazon Bedrock?

Amazon Bedrock is a service provided by AWS that gives users access to a variety of different foundation models using a single API. Using Bedrock, developers can build and deploy generative AI applications without managing their own infrastructure. The current AI providers available on Bedrock are the following:

- AI21 Labs
- Amazon
- Anthropic
- Cohere
- Luma AI
- Meta Llama
- Mistral AI
- Stability AI
- Custom Model Import

## Why make the switch?

### Integration with AWS Ecosystem

One reason you should make the switch to Bedrock from OpenAI is if you are already using the AWS ecosystem to store the input and output pertaining to your current model. This offers a performance boost by minimizing latency, as the services will operate on the same network infrastructure.

Furthermore, integration within a single ecosystem allows you to centralize multiple aspects of an otherwise disparate cloud environment. For instance, moving everything to AWS gives you unified access control using AWS’ Identity and Access Management (IAM). In addition, the ecosystem provides automatic scaling for all compute and storage resources, as well as a single source of truth for metrics about these resources. Finally, AWS contains various other services, such as SageMaker, that can integrate seamlessly with your current system.

### Variety of Models

Another reason to make the switch is because Bedrock supports multiple models, giving users the ability to choose whichever one fits their needs the best. If you’re not sure which model works best for your use-case, you can easily experiment with different models using Amazon Bedrock’s playgrounds functionality. Bedrock’s Playgrounds is a user-friendly interface to test various inference parameters, prompts, and system prompts to see the output the model spits back. With the diverse selection of models, Bedrock reduces the risk of vendor lock-in when choosing an AI provider.

### Reduced Costs

The table below depicts the pricing of OpenAI models based on the cost per million tokens. Each token is approximately 0.75 words in the English language or about 4 characters.

The pricing of Bedrock depends on the model that you choose. As there are numerous models, the costs vary depending on the capabilities of the model. To illustrate, I’ve listed the costs of Amazon’s Nova models below:

Comparing the Amazon Nova Pro to OpenAI’s gpt-4o model (an apples-to-apples comparison), the Nova Pro is 68% cheaper than gpt-4o. This is a significant cost reduction, making the Nova Pro an attractive option for users looking to prioritize cost savings without compromising on performance. Here is an article for a more in-depth analysis of Amazon’s Nova Pro vs. OpenAI’s gpt-4o models: [https://dev.to/makawtharani/amazon-nova-pro-v10-vs-openai-gpt-4o-a-cost-comparison-through-an-example-1hbo. ](https://dev.to/makawtharani/amazon-nova-pro-v10-vs-openai-gpt-4o-a-cost-comparison-through-an-example-1hbo. )

## How to switch from OpenAI to Bedrock

To keep this guide concise, I will skip steps, such as creating an AWS account and granting permissions.

### Request access to an Amazon Bedrock foundation model

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/).
2. Select Model access at the bottom of the left navigation pane.
3. To request access to all models, choose **Enable all models**. To request access to specific models, choose **Enable specific models**.
4. Access may take several minutes to complete. When access is granted to a model, the Access status for that model will become Access granted

### Migrate from OpenAI ChatCompletion to Boto3 Bedrock Runtime

This is arguably the most complex portion of the migration, as it requires one-to-one mapping of the Bedrock and OpenAI interfaces, as well as the JSON responses returned by the APIs.

An example request to create a new chat completion in OpenAI is shown below:

```java
 response = await openai.ChatCompletion.acreate( 
                model=MODEL, 
                messages=   messages = [ 
       		 {"role": "system", "content": system_instruction}, 
        		 {"role": "user", "content": user_prompt}  ] 
                temperature=TEMPERATURE, 
                functions=functions, 
                function_call={"name": functions[0]["name"]}, 
            ) 
```

Similarly, an example request using the Bedrock Converse API is shown below:

```markup
 response = bedrockClient.converse( 
                modelId= “us.anthropic.claude-3-5-sonnet-20241022-v2:0", 
                inferenceConfig={ 
                    "maxTokens": BEDROCK_MAXTOKENS, 
                    "temperature": BEDROCK_TEMPERATURE, 
                }, 
                system=[{"text": system_instruction}], 
                messages=[ 
                    { 
                        "role": "user", 
                        "content": [{"text": user_prompt}], 
                    } 
                ], 
                toolConfig={ 
                    "tools": [ 
                        {"toolSpec": tools}, 
                    ], 
                    "toolChoice": {"tool": {"name": tools["name"]}}, 
                }, 
            ) 
```

It’s apparent that both Bedrock and OpenAI offer similar parameters but make them available in different ways. Let’s list the main differences:

- Model configuration params, such as temperature, are within an inferenceConfig object in Bedrock, whereas they are configured separately in OpenAI
- The system prompt is its own parameter, as opposed to OpenAI keeping it within the messages object
- Functions in OpenAI are called tools in Bedrock and are configured similarly

Another important difference between the two APIs is how to access your structured response.

Bedrock: response["output"]["message"]["content"][0]["toolUse"]["input"] OpenAI: json.loads(response["choices"][0]["message"]["function_call"]["arguments"])

Finally, the schema that we pass along with the tool in our request must be wrapped with a {"json": { ... }} block.

Bedrock Example:

```java
{ 

  "json": { 

    "type": "object", 

    "properties": { 

      "location": { 

        "type": "string", 

        "description": "The city and state or country (e.g., 'New York, NY')." 

      } 

    }, 

    "required": ["location"] 

  } 

} 
```

OpenAI Example:

```markup
{ 

  "type": "object", 

  "properties": { 

    "location": { 

      "type": "string", 

      "description": "The city and state or country (e.g., 'New York, NY')." 

    } 

  }, 

  "required": ["location"] 

} 
```

## Conclusion

Switching from OpenAI to Amazon Bedrock is especially convenient when you already use AWS, as it reduces latency and simplifies infrastructure management. Bedrock also supports multiple foundation models, giving users flexibility and helping avoid vendor lock-in. In addition, the Playgrounds feature allows easy experimentation to find the best model for your needs. Cost-wise, Bedrock can be significantly cheaper—Amazon’s Nova Pro costs 68% less than OpenAI’s GPT-4o. Even though migration does involve some API differences, the overall structure is similar, making the transition manageable. As a result, if you're already using AWS or looking for cost-effective AI models, Bedrock is a strong alternative.

[Reach out to us!](https://www.improving.com/contact)
