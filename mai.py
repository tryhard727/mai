import argparse
import requests
import json


API_KEYS = {
    "openai": "openai_api_key",
    "claude": "claude_api_key",
    "perplexity": "perplexity_api_key",
    "deepseek": "deepseek_api_key",
    "nemotron": "nemotron_api_key"
}

API_ENDPOINTS = {
    "openai": "https://api.openai.com/v1/chat/completions",
    "claude": "https://api.anthropic.com/v1/messages",
    "perplexity": "https://api.perplexity.ai/chat/completions",
    "deepseek": "https://api.deepseek.com/v1/chat/completions",
    "nemotron": "https://api.nvidia.com/v1/nemotron/chat"
}

def query_api(model, prompt):
    if model not in API_KEYS or model not in API_ENDPOINTS:
        print(f"Error: {model} API is not supported or key is missing.")
        return
    
    headers = {"Authorization": f"Bearer {API_KEYS[model]}", "Content-Type": "application/json"}
    payload = {}
    
    if model == "openai":
        payload = {"model": "gpt-4", "messages": [{"role": "user", "content": prompt}]}
    elif model == "claude":
        payload = {"model": "claude-3", "messages": [{"role": "user", "content": prompt}]}
    elif model == "perplexity":
        payload = {"model": "pplx-7b-chat", "messages": [{"role": "user", "content": prompt}]}
    elif model == "deepseek":
        payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
    elif model == "nemotron":
        payload = {"model": "nemotron-3b", "messages": [{"role": "user", "content": prompt}]}
    
    response = requests.post(API_ENDPOINTS[model], headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("\nResponse:")
        print(json.dumps(data, indent=2))
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI for querying multiple LLM APIs.")
    parser.add_argument("model", choices=API_KEYS.keys(), help="Choose the LLM model")
    parser.add_argument("prompt", help="Enter the query prompt")
    args = parser.parse_args()
    query_api(args.model, args.prompt)
