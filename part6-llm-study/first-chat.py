import requests
import os
api_key = os.environ["ds_api_key"]
messages = []
while(True):
    question:str = input("You Say:\n")
    if question == "exit":
        print("退出成功")
        break
    elif question == "clear":
        messages.clear()
        print("聊天记录已清空")
        continue
    messages.append({
        "role":"user",
        "content": question,
    })
    print(f"You say : {question}")
    try:
        response = requests.post(
            url="https://api.deepseek.com/chat/completions",
            headers={
                "Authorization":f"Bearer {api_key}",
                "Content-type": "application/json",
            },
            json={
                "model":"deepseek-flash",
                "messages": messages,
            # [
            #     {
            #         "role":"user",
            #         "content": question,
            #     }
            # ],
                "stream":False,#等待完整回复，再一次性返回
            },
            timeout=120,

        )
        response.raise_for_status()#它只检查 HTTP 错误状态，抛出HTTP错误。
        
    except requests.exceptions.Timeout:
        print("Timeout")
        messages.pop()
        continue
    except requests.exceptions.ConnectionError:
        messages.pop()
        print("check wifi")
        continue
    except requests.exceptions.HTTPError:
        print("错误码：", response.status_code)
        print("错误信息：", response.text)
        messages.pop()
        continue
    data = response.json()
    messages.append({
        "role":"assistant",
        "content": data["choices"][0]["message"]["content"],
    })
    print(f"DeepSeek say: {data['choices'][0]['message']['content']}")



# ds返回的数据的格式决定了
# data = {
#     "id": "某次请求的编号",
#     "choices": [
#         {
#             "message": {
#                 "role": "assistant",
#                 "content": "列表是 Python 中用于存储多个元素的容器。"
#             },
#             "finish_reason": "stop"
#         }
#     ]
# }