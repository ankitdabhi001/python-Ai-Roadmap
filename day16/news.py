import requests

API_KEY = "2c810631fe084d089ab73e32b04b0b19"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    print("🗞️ Top Headlines:\n")
    for i, article in enumerate(data['articles'], start=1):
        print(f"{i}. {article['title']}")
        print(f"   📰 Source: {article['source']['name']}")
        print(f"   🔗 URL: {article['url']}\n")
else:
    print("Failed to fetch news:", response.status_code)
