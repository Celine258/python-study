import requests
import os
api_key = os.environ['ds_api_key']
def deepseek_api(message: list):
    try:
        response = requests.post(
            url="https://api.deepseek.com/chat/completions",
            headers= {
                "Authorization":f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek-flash",
                "messages": message,
                "stream": False,
            },
            timeout=120,
        )
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Timeout")
        raise
    except requests.exceptions.ConnectionError:
        print("check WIFI")
        raise
    except requests.exceptions.HTTPError:
        print("错误码：", response.status_code)
        print("错误信息：", response.text)
        raise
    data = response.json()
    print("DeepSeek say:", data["choices"][0]["message"]["content"])
    return data["choices"][0]["message"]["content"]
    