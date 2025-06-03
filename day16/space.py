import requests

# Fetch all launches
url="https://api.spacexdata.com/v5/launches"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if isinstance(data, list):
        print("🚀  5 SpaceX Missions:\n")
        for a in data[2:7]:
            mission = a.get('name')
            print(f"🔹 {mission}")
    else:
        print("Unexpected data format.")
else:
    print("Error:", response.status_code)
