import requests

prompt = "Summarize this email: Dear customer, your order #1234 has been shipped and will arrive by Friday."

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "deepseek-coder",
        "prompt": prompt,
        "stream": False
    }
)

res_json = response.json()

if 'response' in res_json:
    print("🤖 DeepSeek Output:\n")
    print(res_json["response"])
else:
    print("❌ Error:\n", res_json)
