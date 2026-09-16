import requests
get = requests.get(
    "http://127.0.0.1:8000/students/1",
)
print(get.status_code)
print(get.json())