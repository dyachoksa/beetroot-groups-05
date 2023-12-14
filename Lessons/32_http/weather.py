import requests

api_key = ""
base_url = "http://api.weatherapi.com/v1"

city = input("City: ")

res = requests.get(f"{base_url}/current.json?key={api_key}&q={city}")

data = res.json()

print(f"Location: {data['location']['name']}, {data['location']['country']}")
print("Current temp:", data['current']['temp_c'])
print("Weather conditions:", data['current']['condition']['text'])
