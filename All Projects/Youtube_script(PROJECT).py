
# YouTube Script Writer PROJECT :

def build_prompt(topic,tone):
    return f""" 
    you are the professional youtube script writer.
    
    topic:{topic}
    tone:{tone}
     Write a 1 minute video script for a YouTube video. Include:
    - A hook (engaging intro)
    - Key talking points with a natural flow
    - A short call-to-action
    - A catchy title
    - Thumbnail idea

    Format:
    Title: ...
    Thumbnail Idea: ...
    Script:
    ... """

from gpt4all import GPT4All

model_path = "E:/Python Roadmap/python-Ai-Roadmap/models"
llm = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf", model_path=model_path, allow_download=False)

def generate_video_script(topic, tone):
    prompt = build_prompt(topic, tone)
    with llm.chat_session():
        response = llm.generate(prompt, max_tokens=1000)
    return response

topic = input("🎬 Enter your YouTube video topic: ")
tone = input("🎭 Enter the tone (funny, serious, educational): ")

print("⏳ Generating script...")
script = generate_video_script(topic, tone)
print("\n✅ Script generated:\n")
print(script)


with open(f"{topic}.txt","w") as file:
    file.write(script)