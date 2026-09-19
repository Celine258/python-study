# part6-llm 第 1 课：把地基打好（环境变量 + Pydantic + 分层）

这一课不调用任何模型。它解决的是你那条学习路线上「当前最优先完成的四件事」里的**第一步**：

> 整理现有 FastAPI 项目，分开配置、数据模型、业务逻辑与数据库访问。

顺带把两个路线图点名要求、但你还没接触过的前置知识补上：**环境变量** 和 **Pydantic**。

---

## 先看文件分工

| 文件 | 属于哪一层 | 干什么 |
|---|---|---|
| `config.py` | 配置层 | 从 `.env` 读密钥、地址、超时；对外展示时把密钥打码 |
| `schemas.py` | 模型层 | 用 Pydantic 描述请求/响应的数据结构 |
| `main.py` | 接口层 | 把 HTTP 请求接到函数上，不含任何业务细节 |
| `test_api.py` | 测试 | 用 pytest 给上面的接口上保险（接上你 part1 学的 pytest） |
| `.env` | 配置数据 | 你真正的密钥（**永远不提交**） |
| `.env.example` | 配置模板 | 可以提交，告诉别人"需要配哪些变量" |
| `.gitignore` | —— | 声明哪些文件不进版本库 |

你的 `Start.py` 没错，只是这三件事挤在一个文件里。随着接口变多，拆开才维护得动。

---

## 知识点 1：环境变量

你在 `part4-pyspark/map算子.py` 里写过：

```python
os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
```

`os.environ` 就是一个操作系统的"全局字典"。环境变量就是写进这个字典的值，
好处是**它不在代码里** —— 所以代码可以公开，密钥不用。

`python-dotenv` 做的事很简单：读 `.env` 文件，替你把每一行塞进 `os.environ`。

**两个必须记住的坑：**

1. 读出来**永远是字符串**。`os.getenv("LLM_TIMEOUT")` 拿到的是 `"30"`，不是 `30`，要自己转 `int()`。
2. 路径别写死。你现在 `part3` 里的脚本都写成 `D:/Python学习/part3/...`，
   但文件夹实际叫 `part3-mysql`，所以一跑就 FileNotFoundError。配置就是放这类值的地方。

**顺手要做的一件事**：去 `part3-mysql/mysql/mysql.py`，把那个明文密码也改成从环境变量读。

---

## 知识点 2：Pydantic

一句话：**Pydantic = 带自动校验的类。**

对照你写过的两个文件看：

```python
# part3-mysql/类型注解.py —— 注解只是"备忘"，Python 运行时根本不查
def add(x: int, y: int) -> int: ...

# part1-基础语法/类.ipynb —— 普通类也不查，你想赋什么型都行
class Student:
    name = None
```

Pydantic 把这些注解变成**真的规则**：

```python
class Student(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    age: int = Field(ge=0, le=150)
    address: str = "未知"
```

于是传 `{"name": "", "age": -5}` 会得到一份非常清楚的报错，
而不是等到程序深处才莫名其妙地崩掉。

**三个你已经在用、只是没收进 Pydantic 的东西：**

- `Field(ge=, le=, min_length=)` —— 相当于你在 `while循环.ipynb` 里手写的年龄分段判断
- `@field_validator` —— 就是你学的**装饰器**（`part5-进阶/装饰器.py`）
- `Literal["system","user","assistant"]` —— 相当于 `if role not in [...]`，但写在类型上

**另外两个常用的：**

```python
stu = Student(name="Alex", age=12)
stu.model_dump()          # 转成普通 dict（v2 里叫 model_dump，v1 叫 .dict()）
Student.model_validate_json('{"name":"Alex","age":12}')   # 从 JSON 字符串建对象
```

---

## 怎么跑起来

先激活你原来那个虚拟环境（PowerShell，在 `D:\Python学习\FastAPI` 下你应该是这么干的）：

```powershell
cd D:\Python学习\part6-llm
D:\Python学习\FastAPI\.venv\Scripts\Activate.ps1
```

装依赖（虚拟环境里已经有大部分了，跑一下保险）：

```powershell
pip install -r requirements.txt
```

启动：

```powershell
uvicorn main:app --reload
```

然后打开浏览器访问 **http://127.0.0.1:8000/docs** ——
FastAPI 会自动生成一个交互式文档页，上面 4 个接口都可以直接点「Try it out」测试。
这是 FastAPI 最好用的地方：**因为你在类型注解里把数据结构写清楚了，文档是自动生成的。**

---

## 验证清单

按顺序做一遍，亲眼看到这四件事：

**1. 配置读进来了（且密钥没泄露）**

浏览器打开 http://127.0.0.1:8000/config

`api_key_loaded` 现在是 `false`（因为 `.env` 里的 Key 还空着），等你填上自己的 Key
再回来看，它就变成 `true`，同时 `api_key_preview` 会显示成 `sk-a****...****1234` 的打码形式
——**注意它永远不会把完整密钥吐出来**，这是配置层该有的自觉。

**2. Pydantic 在拦错误数据**

在 `/docs` 里试 `POST /student`：
- `{"name": "Alex", "age": 12}` → 成功返回
- `{"name": "Alex", "age": -5}` → **422**，报错里会说 `age` 必须 ≥ 0
- `{"name": "   ", "age": 12}` → **422**，报错来自你自己写的 `name_not_blank`
- `{"age": 12}` → **422**，缺 `name`

把每次的报错内容读一遍——**Pydantic 的报错信息本身就是最好的教学材料**。

**3. 路径参数的类型转换**

- http://127.0.0.1:8000/student/1 → 返回 Alex
- http://127.0.0.1:8000/student/99 → 返回 404「学号 99 不存在」
- http://127.0.0.1:8000/student/abc → 返回 422（注意：这跟 404 是两回事，一个是"格式不对"，一个是"数据没有"）

**4. 嵌套模型**

在 `/docs` 里试 `POST /chat/preview`，传两条消息，观察返回的「消息条数」。
再故意把 `role` 写成 `"admin"`，看它怎么报错。

---

## 跑测试

上面那些手动点击很好，但**点一次不算数**——改动之后要能一键重验。这就是 `test_api.py` 的作用：

```powershell
pip install pytest
pytest test_api.py -v
```

应该看到 11 个测试全部 PASSED。这批测试覆盖的正是路线图要求的三种情况：
正常输入、错误输入（422）、不存在的数据（404）。

以后你每改一次 `schemas.py`，跑一遍就知道有没有改坏——这就是"可重复验证"。

---

## 练习题

**第 1 题（改 `schemas.py`）**
给 `Student` 加一个字段 `email: str`，要求：
- 不传的时候可以为空
- 传了的话必须是合法邮箱格式
- 提示：`email-validator` 已经装好了，直接 `from pydantic import EmailStr` 就行
- 加完记得在 `test_api.py` 里补一个"邮箱写错 → 422"的测试

**第 2 题（改 `main.py`）**
新增接口 `POST /student/batch`，一次接收**一组**学生（提示：参数类型写 `list[Student]`），
返回这批学生的总人数和平均年龄。想想平均年龄会不会出现除零错误？

**第 3 题（改 `schemas.py` + `main.py`）**
给 `/chat/preview` 加一个统计：把所有 `role == "user"` 的消息内容拼起来，
返回它的字符数（这其实就是模型计费的"输入长度"的粗略估算）。
提示：列表推导式是 `part1-基础语法/操作列表.ipynb` 里的老朋友了。

**第 4 题（改 `config.py`）**
现在 `Settings` 是在模块导入时就创建的。改成延迟创建（第一次用才创建），
想想这样有什么好处？（提示：你学过单例模式）

**第 5 题（真·动手）**
把 `.env` 里 `LLM_TIMEOUT` 改成 `abc`，重启服务，看会发生什么。
然后想一想：**这个错误应该在什么时候被抓住？** 现在是在启动时就崩，还是在请求时才崩？
哪种更好？

---

## 加餐：更进一步的做法

`config.py` 里那些 `int(os.getenv(...))` 手工转换，其实 Pydantic 也能帮你做——
`pydantic-settings` 这个包就是专门干这个的（你环境里已经装好了）：

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    llm_api_key: str = ""
    llm_base_url: str = "https://api.deepseek.com/v1"
    llm_timeout: int = 30      # 自动转成 int，写错直接在启动时报错

settings = Settings()
```

**但建议你先把现在这版手写的跑熟、做完练习，再改写成这一版**——
知道手工做有多麻烦，才能体会到框架替你省了什么。这也是学习路线里强调的：
先理解，再用工具。

---

## 下一课要做什么

`POST /chat/preview` 现在只是把请求原样回显。下一课我们会：

1. 装 `openai` 这个 SDK（国内的智谱、DeepSeek、Kimi、通义都提供 OpenAI 兼容接口，所以同一个 SDK 能通吃）
2. 新建一个 `llm_client.py`，完成一次真正的模型调用
3. 加上超时、重试、耗时记录
4. 把 `/chat/preview` 换成真的 `/chat`

**前提**：`.env` 里的三个值要填对。等你告诉我是哪家的 Key，我再帮你确认 `LLM_BASE_URL` 和 `LLM_MODEL` 该怎么写。
