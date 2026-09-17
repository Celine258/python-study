import requests
post = requests.post(
    url="http://127.0.0.1:8000/students",
    json= {
        "name": "小琳",
        "age": 19,
        "major": "数学"
    }
)
print(post.json())
print(post.status_code)