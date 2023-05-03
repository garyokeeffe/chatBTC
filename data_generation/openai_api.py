import requests
import json

url = "https://api.openai.com/v1/chat/completions"

def create_payload(model, messages, temperature=1, top_p=1, n=1, stop=None, max_tokens=100, presence_penalty=0, frequency_penalty=0, user=None, logit_bias=None):
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "top_p": top_p,
        "n": n,
        "stop": stop,
        "max_tokens": max_tokens,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,

    }
    if user is not None:
        payload["user"] = user
    if logit_bias is not None:
        payload["logit_bias"] = logit_bias

    return payload

def make_request_and_process_response(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        choices = json.loads(response.text)["choices"]
        return [choice["message"]["content"].strip() for choice in choices]
    else:
        print(f"Error: {response.text}")
        return []

