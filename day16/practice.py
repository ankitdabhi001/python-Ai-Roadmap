
# Tranding News Summrized By GPT4ALL

import requests
from gpt4all import GPT4All

news_api_key = "2c810631fe084d089ab73e32b04b0b19"

# 1. Call News API
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
res = requests.get(url)
articles = res.json()["articles"][:5]

# 2. Extract and clean titles
titles = [f"{i+1}. {a['title']}" for i, a in enumerate(articles)]
news_text = "\n".join(titles)

# 3. Summirized Using GPT4ALL

model_path = "E:/Python Roadmap/python-Ai-Roadmap/models"  # ✅ folder containing your model

llm = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf", model_path=model_path, allow_download=False)

prompt=f"""
    You're an intelligent assistant. Here are some recent news headlines:{news_text}

    Please provide a brief summary of the overall news trends in 3-4 bullet points.
    """
answer=llm.generate(prompt)

print(answer)