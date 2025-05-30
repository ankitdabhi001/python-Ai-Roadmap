import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello! Can you respond?"}
    ]
)

print(response.choices[0].message["content"])
