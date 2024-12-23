import json
import boto3

## First, load up the aggregate system prompt ##

# Open and read the JSON file
with open('prompt-config.json', 'r') as file:
    prompt_config = json.load(file)

# Iterate through each config
aggregate_prompt = ""
for filename in prompt_config:
    # Open the file in read mode
    with open('prompt-engineering-data/' + filename, 'r') as file:
       file_contents = file.read()

    # file_contents now contains the entire content of the file as a string
    aggregate_prompt += file_contents + "\n"

print(aggregate_prompt)

## Next, load up the domain knowledge ##

# Open the file in read mode
domain_prompt = ""
with open('domain-data/twenty-something-engineer.md', 'r') as file:
    domain_prompt = file.read()

print(domain_prompt)

## Now, generate a synthetic system prompt ##

# Set up the client
llm_client=boto3.client(service_name="bedrock-runtime",region_name="us-east-1")
   
prompt_config = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1024,
            "system": aggregate_prompt,
            "messages": [
                 {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": domain_prompt
                        }
                    ]
                }
            ],
        }
prompt_str = json.dumps(prompt_config, indent=4)

# Make the call to the model
model_id="anthropic.claude-3-5-sonnet-20240620-v1:0"

response = llm_client.invoke_model(
    body=json.dumps(prompt_config),
        modelId=model_id
    )

# Process the response
response_body=json.loads(response.get("body").read())
json_str = json.dumps(response_body, indent=4)
print(json_str)
print(response_body['content'][0]['text'])