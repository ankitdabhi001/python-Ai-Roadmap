from gpt4all import GPT4All

model_path = "./models/Llama-3.2-3B-Instruct-Q4_0.gguf"
model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf", model_path="./models", allow_download=False)

with model.chat_session():
    topic = input("📝 Enter a blog topic: ")
    prompt = f"Write a 500-word blog post about {topic}."
    print("⏳ Generating blog post...\n")
    blog = model.generate(prompt)
    print("✅ Blog Generated:\n")
    print(blog)

with open(f"{topic}.txt","w") as file:
    file.write(blog)