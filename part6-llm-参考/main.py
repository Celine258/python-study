"""
接口层 main.py —— FastAPI 应用。

【对比你原来的 Start.py】
你原来写的是：

    from fastapi import FastAPI
    app = FastAPI()

    @app.get("/hello")
    def say_hello():
        return {"message": "你好，FastAPI！"}

那个文件没错，但它把"接口"和"配置"混在了一起，也没告诉 FastAPI
"进来的数据应该长什么样"。随着接口变多，一个文件会越来越乱。
所以现在把它拆成三层：

    config.py   —— 配置层：密钥、地址、超时这些"会变的值"
    schemas.py  —— 模型层：请求和响应的数据结构
    main.py     —— 接口层：只负责把 HTTP 请求接到函数上（你现在看的就是）

这也是你那条学习路线里"第一步：分开配置、数据模型、业务逻辑"的具体做法。
"""

from fastapi import FastAPI, HTTPException

from config import settings
from schemas import ChatRequest, Student

app = FastAPI(
    title="学习记录助手",
    description="大模型与 Agent 开发路线的练兵场：对话接口 → 工具调用 → RAG → 微调 → 部署",
    version="0.1.0",
)


# ---------------------------------------------------------------- 基础接口
@app.get("/hello", summary="最小接口")
def say_hello():
    """保留你原来那个接口，方便对照。"""
    return {"message": "你好，FastAPI！"}


@app.get("/config", summary="查看当前配置（密钥已打码）")
def read_config():
    """演示配置层。注意返回值里 api_key 是打过码的，不会把真密钥吐出去。"""
    return settings.describe()


# ------------------------------------------------- Pydantic 自动校验的演示
@app.post("/student", summary="创建学生（体验自动校验）")
def create_student(student: Student):
    """
    注意函数签名：`student: Student`。

    有了这个类型注解，FastAPI 会替你做一整套事情：
      1. 把请求体里的 JSON 解析成字典
      2. 交给 Pydantic 按 Student 的规则校验
      3. 校验通过 → 把 Student 对象直接传给你的函数
         校验失败 → 自动返回 422 错误，并把"哪个字段、错在哪"写清楚

    所以函数体里一句 if 都不用写 —— 能进到这里，数据一定是干净的。
    """
    # model_dump() 是 Pydantic v2 把模型转成普通 dict 的方法（v1 里叫 .dict()）
    return {
        "收到": student.model_dump(),
        "明年年龄": student.age + 1,
        "姓名长度": len(student.name),
    }


# ----------------------------------------------- 对接模型前的占位接口
@app.post("/chat/preview", summary="对话请求预演（暂不调用模型）")
def chat_preview(request: ChatRequest):
    """
    本阶段先把模型请求"接住"并回显，验证数据结构对不对。
    下一课再把真正的模型调用填进来 —— 到那时这个函数的骨架基本不用改，
    这就是"先把接口定好、再实现内部逻辑"的好处。
    """
    return {
        "消息条数": len(request.messages),
        "temperature": request.temperature,
        "最后一条消息": request.messages[-1].model_dump(),
    }


# ----------------------------------------------- 顺手演示一下异常处理
@app.get("/student/{student_id}", summary="按学号查学生（演示 404）")
def get_student(student_id: int):
    """
    路径参数写 `student_id: int` 时，FastAPI 会自动把它转成整数。
    传 /student/abc 会直接得到 422，根本不会进到函数里。

    下面演示"数据（按理说）不存在"时该怎么办 —— 这正是你那条学习路线
    「验收标准」里要求的"不存在的数据要能被处理"。
    """
    fake_db = {1: {"name": "Alex", "age": 12}, 2: {"name": "Steve", "age": 13}}
    if student_id not in fake_db:
        # raise HTTPException 是 FastAPI 里报错的"标准姿势"：
        # 它会中断函数，直接返回你指定的状态码和错误信息。
        raise HTTPException(status_code=404, detail=f"学号 {student_id} 不存在")
    return fake_db[student_id]


# 想直接跑这个文件也可以：python main.py
# （不过更推荐用命令行 uvicorn 启动，见 README）
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
