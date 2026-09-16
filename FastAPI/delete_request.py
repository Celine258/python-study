import requests
delete = requests.delete(
    "http://127.0.0.1:8000/students/1",
)
print(delete.status_code)
print(delete.json())