# FastAPI 学习笔记

学习者：海南大学 2025 级软件工程 NIIT 专业本科生  
学习时间：2026 年 9 月 15 日起  
最后整理：2026 年 9 月 17 日

## 1. 学习目标与当前进度

目标：能独立编写简单的 REST API，并为后续 AI 服务部署打基础。

当前项目是一个学生信息管理 API，使用 **FastAPI + Pydantic + PyMySQL + MySQL**，使用 `requests` 和 `/docs` 测试接口，使用 DBeaver 查看数据库。

已学习：

- [x] 创建、启动 FastAPI 应用。
- [x] 定义路由，理解客户端与服务端。
- [x] 使用路径参数、查询参数和默认值。
- [x] 使用 JSON 请求体和 Pydantic 模型。
- [x] 使用 GET、POST、PUT、DELETE 实现增删改查。
- [x] 理解状态码、HTTPException 与异常处理。
- [x] 用 requests 调用接口。
- [x] 创建 MySQL 数据库和学生表。
- [x] 使用 PyMySQL 查询、新增、修改、删除数据。
- [x] 理解事务提交、回滚和连接关闭。
- [x] 用 Field 限制字符串长度和年龄范围。

学习进度不等于全部代码都已无误；当前待核对项见文末。

## 2. 学习历程

| 阶段 | 学习内容 | 实践与收获 |
|---|---|---|
| 认识 FastAPI | API、HTTP、客户端与服务端 | requests 发请求，FastAPI 接收并处理请求 |
| 第一个接口 | FastAPI 实例、路由、启动服务 | 编写 `/hello`、`/me` |
| 路径参数 | URL 中的动态值、类型注解 | 编写 `/square/{number}` 和学生查询 |
| 查询参数 | `?`、`&`、必填参数和默认值 | 编写 `/greet`、`/add`、`/rectangle` |
| POST 与请求体 | BaseModel、JSON、默认专业 | 新增学生，观察 201 和 422 |
| 客户端调用 | requests 的四种请求方法 | 在独立 Python 文件里调用接口 |
| 修改与删除 | PUT、DELETE、HTTPException | 修改学生；不存在时返回 404 |
| 数据持久化 | 内存与数据库的区别 | 理解重启后字典数据丢失的原因 |
| MySQL 准备 | Windows 服务、DBeaver、建库建表 | 创建 students 表，插入并查询数据 |
| 数据库查询 | connect、游标、参数化 SQL | GET 从 MySQL 读取学生信息 |
| 数据库写入 | INSERT、lastrowid、commit、rollback | POST 新增的数据在重启后仍保留 |
| 数据库修改与删除 | UPDATE、FOR UPDATE、rowcount | 将 PUT、DELETE 迁移到 MySQL |
| 输入验证 | Field 的长度与数值约束 | 拒绝空字符串、过长字段和越界年龄 |

## 3. 项目文件

```text
FastAPI/
├── main.py             # 应用、路由、数据模型与学生增删改查
├── data_base.py        # MySQL 连接函数 get_connection()
├── Start.py            # 最初的 hello 示例，独立应用
├── get_request.py      # 查询接口的客户端示例
├── post_request.py     # 新增接口的客户端示例
├── put_request.py      # 修改接口的客户端示例
├── delete_request.py   # 删除接口的客户端示例
├── README.md           # 学习记录
└── .venv/              # 本项目的 Python 虚拟环境
```

本项目启动入口是 `main.py`，不要与早期示例 `Start.py` 混淆。

## 4. 启动与测试

### 4.1 Python 环境

在 PowerShell 中进入项目目录：

```powershell
cd D:\Python学习\FastAPI
```

首次搭建环境时执行（已有 `.venv` 时不必重新创建）：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install "fastapi[standard]" PyMySQL requests
```

直接使用虚拟环境里的可执行文件，不需要先激活环境。

### 4.2 MySQL 服务与登录

```powershell
# 查看实际服务名称及状态
Get-Service *mysql*

# 示例：在管理员 PowerShell 中启动服务，名称以实际结果为准
Start-Service -Name MySQL80

# 使用命令行客户端登录；使用 DBeaver 时可省略此步
mysql -u root -p
```

启动服务与登录数据库是两件事。退出客户端不会停止 MySQL 服务。

DBeaver 是数据库管理客户端，MySQL 才是存储数据的服务。FastAPI 不需要通过 DBeaver 访问 MySQL。

### 4.3 配置与启动应用

此前 `data_base.py` 使用的环境变量名为 `User` 和 `passwd`。在启动服务的同一个 PowerShell 终端设置与代码一致的变量名：

```powershell
$env:User = "你的数据库用户名"
$env:passwd = "你的数据库密码"
.\.venv\Scripts\fastapi.exe dev main.py
```

这些环境变量只对当前终端及其子进程生效。不要把真实密码写进 README 或提交到代码仓库。

连接配置需要核对：主机、端口、用户名、密码、实际数据库名称，以及 `charset="utf8mb4"`。课程示例库名为 `fastapi_learning`，此前本地代码使用 `fastapilearning`，应以实际创建的数据库为准。

常用地址：

- 服务地址：<http://127.0.0.1:8000>
- 交互式文档：<http://127.0.0.1:8000/docs>
- 查询学生示例：<http://127.0.0.1:8000/students/1>

保持终端运行，按 `Ctrl+C` 停止服务。`fastapi dev` 用于开发，修改代码时会自动重载。

## 5. 核心知识点

### 5.1 FastAPI、API 与 REST

- API 是程序之间交互的入口；本项目通过 HTTP 请求调用接口。
- FastAPI 是编写接口的 Python 框架。
- REST 是接口设计风格，常用路径表示资源、HTTP 方法表示操作。

```text
requests / 浏览器 / 其他客户端
              ↓ HTTP 请求
          FastAPI 路由
              ↓ Python 代码与参数化 SQL
             MySQL
              ↓ 查询或处理结果
          HTTP 响应与 JSON
```

```python
app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello"}
```

装饰器把请求方法、路径和函数关联起来。返回字典时，FastAPI 将其转换为 JSON 响应；Python 字典与 JSON 文本不是同一种数据。

### 5.2 三种常用参数来源

| 来源 | 例子 | 适用场景 |
|---|---|---|
| 路径参数 | `/students/1` | 指定哪个资源 |
| 查询参数 | `/rectangle?width=3&height=4` | 筛选条件或计算参数 |
| JSON 请求体 | `{"name": "小林", "age": 19}` | 提交结构化数据 |

路径参数和查询参数的核心区别是 **URL 中的位置**，不是参数数量或是否存在默认值。

- 路径参数可以有多个，但必须出现在对应路径中。
- 查询参数没有默认值时也可以是必填项。
- 路径参数与查询参数可以一起使用。
- `?` 开始查询参数，`&` 分隔多个参数。

```python
@app.get("/rectangle")
def rectangle(width: float, height: float = 1):
    return {"area": width * height}
```

这里 `width` 必填，`height` 可省略。

### 5.3 请求方法与当前接口

| 方法 | 路径 | 功能 |
|---|---|---|
| GET | `/hello`、`/me` | 基础返回数据练习 |
| GET | `/square/{number}` | 路径参数与平方计算 |
| GET | `/greet`、`/add`、`/rectangle` | 查询参数练习 |
| GET | `/students/{student_id}` | 查询一个学生 |
| POST | `/students` | 新增学生 |
| PUT | `/students/{student_id}` | 替换指定学生的信息 |
| DELETE | `/students/{id}` | 删除指定学生 |

本项目的 PUT 要求提交姓名和年龄。省略专业会使用模型默认值，不会保留原专业。只修改部分字段的 PATCH 尚未学习。

浏览器地址栏直接访问通常发送 GET；POST、PUT、DELETE 可以通过 `/docs`、requests 或其他客户端发送。

```python
response = requests.put(
    "http://127.0.0.1:8000/students/1",
    json={"name": "小林", "age": 19, "major": "软件工程"}
)
print(response.status_code)
print(response.text)
```

`json=` 发送 JSON 请求体；`response.json()` 解析 JSON，`response.text` 读取响应文本。

### 5.4 HTTP 状态码

| 状态码 | 含义 |
|---|---|
| 200 | 请求成功；当前直接返回字典的接口默认使用此状态码 |
| 201 | 创建成功，当前用于 POST |
| 404 | 指定资源不存在 |
| 422 | 请求参数或请求体验证失败 |
| 500 | 服务端未处理的异常 |

状态码与响应体是分开的。写 `{"message": "没有找到"}` 不会自动变成 404。

```python
raise HTTPException(status_code=404, detail="没有找到该学生")
```

`status_code=201` 指定正常响应的状态，不会自动创建数据，也不会覆盖验证错误的 422。

### 5.5 Pydantic 与输入验证

当前学习模型：

```python
class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    age: int = Field(ge=1, le=150)
    major: str = Field(
        default="软件工程",
        min_length=1,
        max_length=100
    )
```

- `min_length`、`max_length`：字符串长度范围。
- `ge`、`le`：大于等于、小于等于。
- 本地选择允许 1～150 岁；课程最初的 0～150 岁示例只是另一种业务规则。
- POST 与 PUT 都使用 StudentCreate，因此共享验证规则。
- 验证失败返回 422，不进入接口函数，不执行数据库操作。
- `"   "` 是非空字符串，当前规则仍允许它；空白清理是下一步内容。
- `"None"` 是字符串；Python 的 `None`、JSON 的 `null` 才表示空值。当前 `major: str` 不接受 `null`。

## 6. MySQL 与 PyMySQL

### 6.1 数据持久化

原来的 `students = {...}` 只保存在进程内存中，重启或自动重载后重新初始化。数据写入 MySQL 并成功提交后，不依赖 FastAPI 进程继续存在。

学生表结构：

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    major VARCHAR(100) NOT NULL DEFAULT '软件工程'
);
```

- `PRIMARY KEY`：唯一标识一行记录。
- `AUTO_INCREMENT`：数据库生成递增编号，不保证连续无缺口。
- `NOT NULL`：禁止 NULL，不等于禁止空字符串。
- `DEFAULT`：插入时省略该列，使用默认值。

### 6.2 连接、游标和读取结果

- `pymysql.connect(...)`：创建连接。
- `DictCursor`：把查询结果中的每行表示成字典。
- `with conn.cursor() as cursor`：创建游标，结束时关闭游标。
- `cursor.execute(sql, params)`：执行参数化 SQL。
- `fetchone()`：读取一行；没有结果时返回 None。
- `fetchall()`：读取剩余所有行，供后续列表接口使用。
- `conn.close()`：关闭连接，与关闭游标不是同一件事。

```python
cursor.execute(
    "SELECT id, name, age, major FROM students WHERE id = %s",
    (student_id,)
)
student = cursor.fetchone()
```

`%s` 是值的占位符。参数交给驱动处理，不要把用户输入用 f-string 拼进 SQL。单元素元组必须保留逗号：`(student_id,)`。

### 6.3 增删改 SQL

```sql
INSERT INTO students (name, age, major) VALUES (%s, %s, %s);

UPDATE students SET name = %s, age = %s, major = %s WHERE id = %s;

DELETE FROM students WHERE id = %s;
```

以上 `%s` 用于 PyMySQL 参数绑定，直接在 DBeaver 中执行时需要填写具体测试值。

- `cursor.lastrowid`：获取刚插入记录的自增编号。
- DELETE 后的 `cursor.rowcount`：删除的行数；按主键删除时，0 表示没有该学生。
- UPDATE 的实际修改行数可能为 0，即使记录存在（新旧值相同），因此不能简单据此判断 404。
- UPDATE、DELETE 不要遗漏 WHERE 条件，否则会影响整张表。

当前 PUT 先执行 `SELECT ... FOR UPDATE` 检查并锁定记录，再更新；在 InnoDB 同一事务中，锁通常在提交或回滚时释放。

删除也可以先查询再删除；若无需读取或检查学生的其他信息，直接删除并判断 rowcount 即可。

### 6.4 事务与异常处理

当前连接使用默认的非自动提交方式，写入操作需要 commit：

```python
conn = get_connection()
try:
    with conn.cursor() as cursor:
        # 执行 SQL
        ...
    conn.commit()
except Exception:
    conn.rollback()
    raise
finally:
    conn.close()
```

- `commit()`：提交事务。
- `rollback()`：撤销尚未提交的修改。
- `raise`：继续抛出当前异常，避免失败后仍执行成功响应。
- `finally`：成功或异常时都执行清理。

HTTPException 也会被 `except Exception` 捕获，所以回滚后需要重新抛出它，才能正确返回 404。

## 7. 学习中遇到的错误

| 问题 | 原因 | 解决或检查方式 |
|---|---|---|
| 建表语句报错 | 把 AUTO_INCREMENT 写成 anto_increment | 修正拼写 |
| 数据库连接调用报错 | 把 pymysql.connect 写成 pymysql.connections | 使用 connect 函数，模块不能这样调用 |
| 字符集初始化报错 | 连接配置用了 `utf-8` | MySQL 字符集改为 `utf8mb4` |
| 环境变量 KeyError | 名称不一致或启动终端中没有设置 | 代码与当前终端中的变量名保持一致 |
| 找不到数据库 | 代码中的库名与实际库名不同 | 用 SHOW DATABASES 核对 |
| PUT 返回 500 | UPDATE 语句遗漏表名和 SET | 使用完整的 UPDATE students SET ... WHERE ... |
| 客户端 JSONDecodeError | 服务端错误响应不是合法 JSON，仍调用了 .json() | 先看状态码和 .text，再看服务端异常堆栈 |
| 删除失败却显示成功 | except 回滚后没有 raise | 回滚后重新抛出异常 |
| 删除不存在的记录返回 500 | 把 raise 写成了 ra | 补全 raise，避免 NameError 掩盖原始 404 |
| 删除成功返回 201 | 把创建成功的状态码用于删除 | 当前返回响应体的删除接口使用 200 |
| 重启后数据消失 | 数据仅存在 Python 字典中 | 改用 MySQL，并正确提交事务 |

排错顺序：先看状态码，再看响应文本，最后看运行 FastAPI 的终端中异常堆栈末尾的信息及对应代码行。

## 8. 验收记录与待办

2026-09-17 已用本地测试客户端验证：POST、PUT 对空姓名、过长姓名、负数年龄、年龄 0/151、空专业和过长专业均返回 422，且不调用数据库连接。模型验证接受年龄 1、19、150，默认专业正常。测试未写入真实数据库。

### 当前代码待核对

- [ ] 本次整理时，磁盘上的 DELETE 异常分支仍为 `ra`，需要保存为 `raise`；此前模拟删除不存在记录得到 500，应修正后确认返回 404。
- [ ] GET 学生接口目前只查询 `id, name, major`，可以加入 `age`，让查询结果包含完整信息。
- [ ] 原来的 students 内存字典已不参与数据库接口，可清理；旧注释代码可按复习需要保留或整理。

### 完整流程验收

使用专门新增的测试学生，记录接口返回的实际编号，不要假定一定是 1：

1. POST 新增学生，预期 201。
2. GET 查询该编号，确认数据一致。
3. PUT 修改，预期 200；再次 GET 确认修改结果。
4. PUT 提交相同数据，仍应成功。
5. 重启 FastAPI，再次 GET，确认已提交数据仍存在。
6. DELETE 删除，预期 200。
7. 再次 DELETE 或 GET 同一编号，预期 404。

### 后续学习方向

- [ ] 清理首尾空白，拒绝纯空格姓名和专业。
- [ ] 增加 GET /students 列表查询，再学习筛选和分页。
- [ ] 定义响应模型，统一返回字段。
- [ ] 学习 PATCH，区分部分更新与完整替换。
- [ ] 拆分路由、模型和数据库代码。
- [ ] 为关键行为添加可重复的接口测试。

## 9. 官方资料

- [FastAPI 入门](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI 请求体](https://fastapi.tiangolo.com/tutorial/body/)
- [Pydantic 文档](https://docs.pydantic.dev/latest/)
- [PyMySQL 文档](https://pymysql.readthedocs.io/en/latest/)
- [MySQL 文档](https://dev.mysql.com/doc/)

这些链接用于后续查阅；本文主要记录本项目的实际学习过程与代码检查结果。
