"""
接口测试 test_api.py —— 把你学过的 pytest，用到 FastAPI 上。

回忆 part1-基础语法 里你写的 survey.py + test_survey.py：

    from survey import AnonymousSurvey
    def test_fruit_survey():
        ...
        assert i in fruit_survey.reponses

测试的思路完全一样：**给一段输入，断言输出符合预期**。
只是这次"输入"变成了 HTTP 请求。

新东西只有 TestClient 这一个：它是个假的浏览器，能不启动服务器就把请求
直接递给 app，所以测试跑得飞快。

跑法（在 part6-llm 目录下）：
    pytest test_api.py -v

【为什么要有这个文件？】
你那条学习路线的"第一步"验收标准原文是：
    「为正常输入、错误输入和不存在的数据增加可重复验证」

这个文件就是那句话的落地。以后每次改 schemas.py，跑一遍就知道有没有改坏。
"""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# ---------------------------------------------------- 正常输入
def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json()["message"] == "你好，FastAPI！"


def test_create_student_ok():
    response = client.post("/student", json={"name": "Alex", "age": 12})
    assert response.status_code == 200
    body = response.json()
    assert body["收到"]["name"] == "Alex"
    assert body["明年年龄"] == 13


def test_address_has_default():
    """没传 address 时，Pydantic 会填上默认值 "未知"。"""
    response = client.post("/student", json={"name": "Steve", "age": 13})
    assert response.json()["收到"]["address"] == "未知"


# ------------------------------------------------ 错误输入（Pydantic 拦截）
def test_age_negative_rejected():
    response = client.post("/student", json={"name": "Alex", "age": -5})
    assert response.status_code == 422   # 422 = 数据格式不对


def test_name_blank_rejected():
    """这条走的是你自己写的 name_not_blank。"""
    response = client.post("/student", json={"name": "   ", "age": 12})
    assert response.status_code == 422


def test_name_missing_rejected():
    response = client.post("/student", json={"age": 12})
    assert response.status_code == 422


# ------------------------------------------------ 不存在的数据（404）
def test_student_found():
    response = client.get("/student/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alex"


def test_student_not_found():
    """注意 404 和 422 的区别：
       404 = 请求没错，但东西不存在
       422 = 请求本身就写错了（连查都不用查）
    """
    response = client.get("/student/99")
    assert response.status_code == 404


def test_student_id_not_a_number():
    response = client.get("/student/abc")
    assert response.status_code == 422


# ------------------------------------------------ 嵌套模型
def test_chat_preview():
    payload = {
        "messages": [
            {"role": "system", "content": "你是一个学习助手"},
            {"role": "user", "content": "解释一下 Pydantic"},
        ],
        "temperature": 0.5,
    }
    response = client.post("/chat/preview", json=payload)
    assert response.status_code == 200
    assert response.json()["消息条数"] == 2


def test_bad_role_rejected():
    """role 只能是 system / user / assistant。"""
    payload = {"messages": [{"role": "admin", "content": "你好"}]}
    response = client.post("/chat/preview", json=payload)
    assert response.status_code == 422
