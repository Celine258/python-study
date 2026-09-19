import requests
response = requests.get(
    "https://api.github.com/users/octocat",
    timeout=10
)

response.raise_for_status()
data = response.json()
print(data)