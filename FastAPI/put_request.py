import requests
put = requests.put(
    "http://127.0.0.1:8000/students/1",
    json={
        "name": "CelineDa",
        "age":19
    }
)

print(put.status_code)
print(put.json())