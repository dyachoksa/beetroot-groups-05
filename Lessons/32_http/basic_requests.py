import requests

base_url = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{base_url}/posts")

print(f"Status code: {response.status_code}")
print(f"Content type: {response.headers['content-type']}")
print("Response content:")
print(response.json())
