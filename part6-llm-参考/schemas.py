"""
数据模型层 schemas.py —— 用 Pydantic 描述"一份数据长什么样"。

【先回忆两件你学过的事】

1) part3-mysql/类型注解.py 里你写过：

       def add(x: int, y: int) -> int:
           return x + y

   注意：这些注解 Python **运行时根本不检查**。你写 add("a", "b") 它也照样跑，
   只是 IDE 会给你划黄波浪线。注解对 Python 来说只是"备忘"。

2) part1-基础语法/类.ipynb 里你写过 Student 类：

       class Student:
           name = None
           ...
           stu1.name = "Alex"
           stu1.age = 12

   这个类也完全不检查：你写 stu1.age = "十二岁" 它也不会拦你。

【Pydantic 干的事】
把那些"备忘"变成"规则"，并且真的在执行。你声明 age: int，
那么传进来 "abc" 就会当场报错，还会告诉你错在哪、为什么错。

一句话：**Pydantic = 带自动校验的类。**
"""

from typing import Literal

from pydantic import BaseModel, Field, field_validator


class Student(BaseModel):
    """用 Pydantic 重写你在 part1 写过的 Student 类，对比一下多了什么。"""

    # 格式：字段名: 类型 [= 默认值 / Field(...)]
    name: str = Field(min_length=1, max_length=20, description="姓名")
    age: int = Field(ge=0, le=150, description="年龄")   # ge=大于等于, le=小于等于
    address: str = "未知"                                # 有默认值 → 请求里可以不传

    @field_validator("name")
    @classmethod
    def name_not_blank(cls, value: str) -> str:
        """自定义校验规则。

        注意这一行同时用到了你学过的两样东西：
          - @field_validator(...) 是**装饰器**（part5-进阶/装饰器.py）
          - cls 是**类方法**的第一个参数（part3-mysql/class.ipynb）
        Pydantic 就是靠装饰器把校验函数"挂"到字段上的。

        校验通过就 return 处理后的值；发现问题就 raise ValueError，Pydantic 会把它
        变成一条清晰的报错信息。
        """
        if not value.strip():
            raise ValueError("姓名不能全是空格")
        return value.strip()   # 顺手去掉首尾空格


class ChatMessage(BaseModel):
    """一条对话消息：role 只能取固定的几个值。"""

    # Literal["system","user","assistant"] 意思是"只能是这三个字符串之一"，
    # 传 "admin" 会被直接拒绝。这比写 if role not in ... 干净得多。
    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1, description="消息内容，不能是空字符串")


class ChatRequest(BaseModel):
    """一次对话请求。注意里面嵌套了上面的 ChatMessage —— 模型是可以套娃的。"""

    messages: list[ChatMessage] = Field(min_length=1, description="至少一条消息")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0, description="随机性")

    model_config = {
        "json_schema_extra": {          # 只是给 /docs 文档页加个示例，不影响校验
            "examples": [
                {
                    "messages": [
                        {"role": "system", "content": "你是一个学习助手"},
                        {"role": "user", "content": "帮我解释一下 Pydantic"},
                    ],
                    "temperature": 0.7,
                }
            ]
        }
    }
