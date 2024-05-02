import boto3
import json
import os

client = boto3.client('bedrock', region_name='us-east-1')
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

guardrail_identifier = os.environ['GUARDRAIL_IDENTIFIER']
guardrail = client.list_guardrails(guardrailIdentifier=guardrail_identifier)['guardrails'][-1]

def invoke_model(client, prompt, model,
    accept = 'application/json', content_type = 'application/json',
    max_tokens  = 512, temperature = 1.0, top_p = 1.0, top_k = 200, stop_sequences = [],
    guardrailIdentifier=guardrail['id'],
    guardrailVersion=guardrail['version'],
    trace="ENABLED"):

    input = {
        'max_tokens': max_tokens,
        'stop_sequences': stop_sequences,
        'temperature': temperature,
        'top_p': top_p,
        'top_k': top_k,
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [{"role": "user", "content": prompt}]
    }
    body=json.dumps(input)
    response = client.invoke_model(body=body, modelId=model, accept=accept, contentType=content_type,
                             guardrailIdentifier=guardrailIdentifier,guardrailVersion=guardrailVersion,trace=trace)
    response_body = json.loads(response.get('body').read())
    output = response_body.get('content')[0]['text']
    return output, response_body

def get_output(prompt, model, max_tokens, temperature, top_p):
    output, response_body = invoke_model(
        client=bedrock_runtime,
        prompt=prompt,
        model=model,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )
    print("Guardrail Trace:")
    print(json.dumps(response_body, indent=2))

    print("Response:")
    print(output)

prompt = os.environ['MSG']
model = "anthropic.claude-3-haiku-20240307-v1:0"

max_tokens = 1024
temperature = 0.1
top_p = 0.9

get_output(prompt, model, max_tokens=max_tokens, temperature=temperature, top_p=top_p)
