# import requests

# API_KEY = "2c810631fe084d089ab73e32b04b0b19"
# url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     # print(data)
#     print("🗞️ Top Headlines:\n")
#     for i, article in enumerate(data['articles'], start=1):
#         print(f"{i}. {article['title']}")
#         print(f"   📰 Source: {article['source']['name']}")
#         print(f"   🔗 URL: {article['url']}\n")
# else:
#     print("Failed to fetch news:", response.status_code)


import requests
import openai

# ====== Step 1: API Keys ======
openai.api_key = "YOUR_OPENAI_API_KEY"        # Replace with your OpenAI API key
news_api_key = "2c810631fe084d089ab73e32b04b0b19"             # Replace with your NewsAPI key

# ====== Step 2: Set up the API endpoint, headers, and parameters ======
url = "https://newsapi.org/v2/top-headlines"

headers = {
    
    "Authorization": f"Bearer {news_api_key}"   # Token goes in headers
}

params = {
    "country": "us",         # News from the US
    "category": "technology" # Only tech news
}

# ====== Step 3: Make the API call ======
response = requests.get(url, headers=headers, params=params)

# ====== Step 4: Handle errors ======
if response.status_code != 200:
    print("❌ Failed to fetch news:", response.status_code)
    exit()

# ====== Step 5: Extract top 5 headlines from JSON ======
articles = response.json().get("articles", [])[:10]

titles = [f"{i+1}. {article['title']}" for i, article in enumerate(articles)]
news_text = "\n".join(titles)

print("📰 Top Headlines:\n", news_text)
