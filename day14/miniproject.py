from gpt4all import GPT4All

model_path = "E:/Python Roadmap/python-Ai-Roadmap/models"
model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf", model_path=model_path, allow_download=False)

with model.chat_session():
    user_topic=input("enter your topic : ")
    prompt=f"create a blog in 100 word about{user_topic}"

    answer=model.generate(prompt)

    # print(answer)

with open("miniproject.txt","w") as f:
    f.write(answer)