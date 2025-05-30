from transformers import pipeline

# Load a text-generation pipeline with a local model
generator = pipeline("text-generation", model="gpt2")  # or 'tiiuae/falcon-7b-instruct' if you want something stronger

# Prompt for blog
prompt = "Write a blog post about the wedding in india."

# Generate content
result = generator(prompt, max_length=300, num_return_sequences=1)

# Show result
print("\n📝 Generated Blog:\n")
print(result[0]['generated_text'])

with open("marrige.txt","a") as file:
    file.write(result[0]['generated_text'])
