import requests
import json
import openai

def get_openai_response(prompt):
    endpoint = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.7
    }
    
    response = requests.post(endpoint, headers=headers, json=data)
    response_data = json.loads(response.text)
    print(response_data)
    completion = response_data['choices'][0]['text'].strip()
    return completion

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'

# Example usage
prompt = "Once upon a time"
response = get_openai_response(prompt)
print(response)
 
