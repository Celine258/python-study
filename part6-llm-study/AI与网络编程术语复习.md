# AI 调用与网络编程术语复习

整理日期：2026-09-18  
对应练习：[first-chat.py](./first-chat.py)  
当前范围：使用 Python requests 调用 DeepSeek，实现非流式、多轮对话，以及 exit、clear 指令。

## 1 先看完整的数据流

```text
input() 读取问题
    ↓
处理 exit 或 clear 等本地指令
    ↓
把用户消息追加到 messages
    ↓
requests.post() 发送 HTTP 请求
    ↓
服务器验证身份和参数，调用模型生成回复
    ↓
收到 response 响应对象
    ↓
raise_for_status() 检查 HTTP 错误状态
    ↓
response.json() 解析响应体
    ↓
取出回复文本，保存 assistant 消息并打印
    ↓
下一轮发送包含历史的 messages
```

**注意：`messages.append()` 只修改本地列表，`requests.post()` 才会发出网络请求。**

## 2 AI 与对话术语

| 术语 | 含义 | 在当前代码中的作用 |
|---|---|---|
| AI 人工智能 | 一个广泛的技术领域，大语言模型是其中一类技术 | 当前程序使用大语言模型提供问答能力 |
| LLM 大语言模型 | 能处理和生成自然语言的模型 | DeepSeek 服务根据传入的消息生成回答 |
| 推理 Inference | 使用已经训练好的模型计算输出 | 每次调用模型生成回答，都在进行模型推理；这里不表示每次都训练模型 |
| model 模型名称 | 指定请求使用哪个模型的字段 | 当前填写 `"deepseek-flash"`；模型名属于服务接口配置，后续以官方文档为准 |
| Prompt 提示词 | 提供给模型的问题、指令或相关材料 | 例如“用两句话解释 Python 的列表” |
| Message 消息 | 一条带角色、内容等字段的信息 | 普通文本消息形如 `{"role": "user", "content": question}` |
| messages 消息列表 | 按顺序组织的消息集合 | 你维护的 Python 列表，也是请求体中必须正确拼写的字段名 |
| role 角色 | 标记消息属于哪个角色 | 用来区分用户提问和模型回答 |
| user 用户角色 | 用户提供的消息 | `"role": "user"` |
| assistant 助手角色 | 模型提供的回复 | `"role": "assistant"`；它描述谁说的，不是说消息发给谁 |
| system 系统角色 | 用于给模型提供整体行为要求的消息角色 | 当前代码没有使用，后续可以用于说明助手的任务和回答要求 |
| content 消息内容 | 普通文本消息中的具体文本 | 用户问题或模型回复 |
| 对话历史 | 按顺序保存的过去消息 | `messages` 中已有的用户消息和助手回复 |
| Context 上下文 | 模型本次生成时能够利用的信息 | 当前请求携带的聊天历史和新问题；以后也可以加入指令、检索资料等 |
| 多轮对话 | 连续交流，后续回答利用之前的信息 | 每轮都追加消息，并把需要的历史一起发送 |
| 无状态接口 Stateless API | 不自动延续上一次调用的对话上下文 | DeepSeek 的这个聊天接口需要客户端重新发送历史；这不等于对服务方日志保存政策的说明 |
| Token | 模型处理文本的基本单位 | 消息会被转换成 token；一个 token 不一定对应一个汉字、单词或字符 |
| 上下文窗口 | 模型一次处理的上下文长度限制，通常用 token 衡量 | 聊天历史不能无限增加；当前练习先理解概念，之后再学习裁剪和摘要 |
| 非流式输出 | 等待完整结果后返回 | 请求体中的 `"stream": False` |
| 流式输出 | 生成过程中陆续返回数据 | 请求体中设置 `"stream": True` 后还要改接收逻辑；每批不一定只有一个字 |

DeepSeek 的多轮消息组织方式参见：[官方多轮对话说明](https://api-docs.deepseek.com/zh-cn/guides/multi_round_chat/)。

### 2.1 多轮对话为什么要发送历史

假设第一轮你说“我正在学习 Python”，第二轮问“我刚才说在学什么？”，第二轮需要发送类似下面的消息：

```python
messages = [
    {"role": "user", "content": "我正在学习 Python。"},
    {"role": "assistant", "content": "好的，我们可以一起学习 Python。"},
    {"role": "user", "content": "我刚才说在学什么？"},
]
```

上面的助手回复是结构示例。实际程序中应保存模型真正返回的回复。

模型能利用前文，是因为程序再次发送了它，不是因为 API Key 自动关联了一份聊天记录。当前程序也没有把聊天记录保存到磁盘，重启程序会重新创建空列表。

### 2.2 choices 与回复取值

下面是为了理解结构而简化的响应，并非完整响应：

```python
data = {
    "id": "本次响应的编号",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "列表可以保存多个元素。",
            },
            "finish_reason": "stop",
        }
    ],
}
```

| 表达式或字段 | 含义 |
|---|---|
| `data` | 响应 JSON 解析后的 Python 字典；变量名由自己起 |
| `data["choices"]` | 本次响应中的生成结果列表；字段名由接口规定 |
| `data["choices"][0]` | 第一个结果；Python 列表索引从 0 开始 |
| `data["choices"][0]["message"]` | 这个结果的助手消息 |
| `data["choices"][0]["message"]["content"]` | 助手回复的正文文本 |
| `finish_reason` | 生成结束的原因；示例中的 `stop` 表示正常结束或遇到停止条件 |

**`choices[0]` 不是第一轮聊天的意思。第二轮、第三轮也读取本次响应的第一个结果。**

```python
reply = data["choices"][0]["message"]["content"]

messages.append({
    "role": "assistant",
    "content": reply,
})
```

左边的 `"content"` 是你构造的历史消息字段；右边的表达式是从服务器响应中读取回复。

接口格式参见：[DeepSeek 首次调用说明](https://api-docs.deepseek.com/zh-cn/)。

## 3 网络编程术语

这些概念也适用于普通网站和后端接口，并非 AI 专属。

| 术语 | 含义 | 当前代码中的对应内容 |
|---|---|---|
| 客户端 Client | 发起请求的一方 | 你的 Python 程序 |
| 服务端 Server | 接收请求并返回结果的一方 | DeepSeek API 服务 |
| API 接口 | 程序与服务交互的约定和入口 | 约定请求路径、参数和返回结构 |
| URL | 资源或接口的地址 | `https://api.deepseek.com/chat/completions` |
| 域名 Host | 定位服务使用的名称 | `api.deepseek.com` |
| 路径 Path | 标识服务中的具体入口 | `/chat/completions` |
| Endpoint 接口端点 | 一个具体的接口入口，通常结合方法和路径描述 | `POST /chat/completions` |
| HTTP | 客户端与服务器交换请求、响应的协议 | 请求有方法、头部和可选的正文；响应有状态码、头部和正文 |
| HTTPS | 使用 TLS 保护传输的 HTTP | URL 以 `https://` 开头 |
| Request 请求 | 客户端提交给服务器的信息 | 由 `requests.post()` 发出 |
| Response 响应 | 服务器返回的状态、头部、正文等信息 | 保存在 `response` 对象中 |
| GET | HTTP 方法，通常用于获取资源 | 之前查询 GitHub 用户时使用；本次生成回复用 POST |
| POST | HTTP 方法，用于提交数据给服务处理 | 本次将模型名称和消息列表提交给 DeepSeek |
| Headers 请求头 | 请求携带的身份、格式等元信息 | `headers={...}`；参数名是复数 `headers` |
| Body 请求体 | 请求中实际提交的数据 | 当前通过 `json={...}` 发送 |
| Authorization | 携带认证信息的请求头 | `"Authorization": f"Bearer {api_key}"` |
| Bearer | 一种携带访问凭据的认证方案 | `Bearer` 后面通过一个空格连接密钥 |
| API Key | 调用服务使用的身份凭据 | 由本机环境变量读取，不应写入笔记或提交到仓库 |
| Content-Type | 声明正文的数据类型 | `application/json` 表示正文为 JSON |
| JSON | 跨语言传递结构化数据的文本格式 | 包含对象、数组、字符串、数值、布尔值和 null 等 |
| 序列化 | 把程序里的数据转换成可传输的表示 | `json=payload` 会让 Requests 将 Python 数据编码为 JSON |
| 反序列化 | 把传输的数据解析成程序对象 | `response.json()` 把 JSON 解析成 Python 对象 |
| 状态码 Status Code | 服务端用数字表示请求的处理情况 | `response.status_code` |
| 超时 Timeout | 对连接、等待响应数据等过程设置等待限制 | `timeout=120`；不等于整个请求严格最多运行 120 秒 |
| HTTPError | Requests 对 HTTP 错误状态抛出的异常 | `raise_for_status()` 遇到 4xx 或 5xx 时会抛出 |

请求头名称不区分大小写，所以 `Content-type` 与 `Content-Type` 都可以；JSON 字段名则要严格遵守接口约定。

请求头、JSON 编码及异常行为参见：[Requests 官方快速入门](https://requests.readthedocs.io/en/latest/user/quickstart/)。

### 3.1 headers 与 json 分别放什么

```python
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

payload = {
    "model": "deepseek-flash",
    "messages": messages,
    "stream": False,
}
```

- `headers`：身份和请求正文格式等元信息。
- `payload`：要交给模型服务处理的数据；这是自定义变量名。
- `requests.post(..., json=payload)`：把 `payload` 编码为 JSON 请求体。
- 只使用 `json=...` 发送数据时，Requests 会自动设置 JSON 的 Content-Type；此时可以不手写该请求头。

Python 字典与 JSON 文本不是同一种对象。例如 Python 写 `False`、`None`，JSON 写 `false`、`null`，转换工作由库完成。

### 3.2 response 与 data 的区别

```python
response = requests.post(...)  # 这里只展示结构，省略号不是完整请求代码
response.raise_for_status()
data = response.json()
```

| 对象或方法 | 作用 |
|---|---|
| `response` | Requests 的 Response 对象，包含 HTTP 响应信息 |
| `response.status_code` | 获取数字状态码 |
| `response.text` | 获取文本形式的响应体，排查错误时很有用 |
| `response.content` | 获取字节形式的响应体；不是模型消息里的 content 字段 |
| `response.json()` | 尝试把响应体解析为 Python 对象；响应不是合法 JSON 时会报解析错误 |
| `response.raise_for_status()` | 遇到 HTTP 4xx/5xx 抛出异常；不会自动修复或重试请求 |
| `data` | 当前接口的 JSON 解析结果，通常是字典，不再是 Response 对象 |

**能调用 `.json()` 成功，不代表业务请求成功。错误响应也可能是合法 JSON。**

### 3.3 目前需要认识的状态码

| 状态码 | 在当前 DeepSeek 调用中的含义 | 优先检查 |
|---|---|---|
| 200 | 正常成功响应 | 再读取正文并检查结果 |
| 400 | 请求体格式错误 | `messages`、`role`、`content` 等字段及结构 |
| 401 | 身份认证失败 | API Key 和 Authorization |
| 402 | 余额不足 | 对应 API 账户余额 |
| 422 | 请求参数错误 | 参数内容、类型或组合 |
| 429 | 请求速率达到上限 | 请求频率、token 用量，按服务规则退避重试 |
| 500 | 服务器内部故障 | 记录响应信息，稍后重试 |
| 503 | 服务繁忙 | 稍后重试 |

上表中具体错误含义按 DeepSeek 服务说明理解，不能把所有服务的业务约定都视为相同。来源：[DeepSeek 错误码](https://api-docs.deepseek.com/zh-cn/quick_start/error_codes/)。

排错时先查看服务端的错误正文：

```python
if not response.ok:
    print(response.status_code)
    print(response.text)

response.raise_for_status()
```

`response.ok` 为真并不只代表 200：它通常表示状态码小于 400。若业务要求特定状态，应直接检查状态码。

### 3.4 两处 stream 不要混淆

```python
requests.post(
    url,
    json={"model": "deepseek-flash", "messages": messages, "stream": True},
    stream=True,               # Requests 自身的参数
)
```

上面只展示参数所在位置，省略了认证和接收处理，不是完整的流式调用代码。

- 请求体里的 `stream`：要求模型服务按流式格式返回。
- Requests 的 `stream`：控制客户端是否延迟读取响应体，便于逐步消费数据。
- 真正显示流式回复还需要读取和解析响应中的事件或数据片段，不能只把 False 改成 True 后继续使用一次 `response.json()`。

## 4 对话管理涉及的 Python 术语

| 写法 | 含义 | 在练习中的作用 |
|---|---|---|
| `os.environ["ds_api_key"]` | 从进程环境变量中读取值 | 获取密钥；变量不存在时会抛出 KeyError |
| `messages = []` | 创建空列表并赋给变量 | 初始化聊天历史，放在循环外 |
| `messages.append({...})` | 在列表末尾追加元素 | 保存一条用户或助手消息 |
| `messages.clear()` | 清空当前列表 | 移除当前程序维护的历史消息 |
| `input()` | 读取终端输入，结果是字符串 | 获取用户本轮问题 |
| `while True` | 持续循环 | 支持多轮聊天 |
| `break` | 结束当前循环 | 输入 exit 后退出聊天循环 |
| `continue` | 跳过本轮剩余代码 | clear 后直接等待下一次输入 |

`messages = []` 是重新绑定一个新列表；`messages.clear()` 是清空原列表。当前程序只通过 messages 使用这个列表时，都可以达到清空历史的目的，但都不会自动跳过后续发送代码。

## 5 本次练习的易错点

### 错误一 请求里的 messages 少写了 s

```python
# 错误："message": messages
# 正确：
"messages": messages
```

请求中的消息集合叫 `messages`；响应中某个结果的消息叫 `message`。它们位于不同结构中。

### 错误二 保存助手回复时把 content 写成 message

```python
# 正确结构
messages.append({
    "role": "assistant",
    "content": data["choices"][0]["message"]["content"],
})
```

第一轮可能成功，第二轮才失败：第一轮发送时只有正确的用户消息；收到回复后追加了错误的助手消息；第二轮再发送历史时，错误结构才被提交。

### 错误三 把 choices 的索引当成聊天轮数

`[0]` 是本次结果列表的第一项。聊天轮数增加，增长的是本地 `messages`，不是 `choices` 的索引。

### 错误四 在循环内无条件重新创建 messages

如果每轮开头都执行 `messages = []`，上一轮的聊天记录就用不上了。初始化放在循环外，循环内追加。

### 错误五 clear 后缺少 continue

2026-09-18 核对代码时，当前 clear 分支执行了清空和打印，但缺少 `continue`。后面的代码仍会追加并发送字符串 `"clear"`。可以按下面的局部结构自行修改：

```python
question = input("You Say:\n")

if question == "exit":
    print("退出成功")
    break
elif question == "clear":
    messages.clear()
    print("聊天记录已清空")
    continue

# 只有普通问题才走到这里
messages.append({"role": "user", "content": question})
```

这里的 clear 和 exit 是自己定义的本地指令，不是 DeepSeek 接口提供的参数。清空本地历史不修改模型参数，也不代表删除服务端可能保留的记录。

## 6 复习自测

先不看上文，尝试回答：

1. API Key 应该放在请求头还是 messages 中？
2. `role` 表示谁说的，还是消息发给谁？
3. `messages.append()` 会不会立即向模型发送请求？
4. 为什么模型能回答“我刚才说了什么”？
5. 第二轮为什么仍然取 `choices[0]`？
6. 请求中的 `messages`、响应中的 `message`、消息里的 `content` 有什么区别？
7. `response.json()` 与 `response.raise_for_status()` 各检查什么？
8. 400 出现时，应该增加哪两项输出帮助排错？
9. clear 后为什么要写 continue？break 又有什么不同？
10. 请求体里的 stream 与 Requests 的 stream 有什么不同？

练习验收：告诉模型一个信息，下一轮检查它能否利用历史；执行 clear 后再问旧信息；最后输入 exit，确认退出。调试时可打印 messages 核对实际发送结构，分享输出前注意移除隐私内容和密钥。
