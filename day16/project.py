import requests

API_KEY = ""
city = "Delhi"

# API endpoint
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("🌤️ Weather Report:")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Condition: {data['weather'][0]['description'].title()}")
else:
    print("Failed to retrieve data:", response.status_code)
