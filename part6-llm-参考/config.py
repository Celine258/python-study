"""
配置层 config.py —— 所有"会变的东西"集中放这里。

【为什么要这一层？】
回忆你写的 part3-mysql/mysql/mysql.py：

    conn = Connection(host="localhost", port=3306, user="root", password="240567")

密码直接写死在代码里，会有三个问题：
  1. 这份代码一旦发给别人 / 传到网上，密码就泄露了
  2. 换一台电脑、换一个数据库，必须改代码（而不是改配置）
  3. 同一个项目在不同环境（自己电脑 / 服务器）要用不同的值，没法共用一份代码

解决办法：把"会变的值"从代码里搬出去，放进**环境变量**。

【什么是环境变量？】
其实你已经用过它了。在 part4-pyspark/map算子.py 里你写过：

    os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"

os.environ 就是一个"全局字典"，操作系统把它借给所有程序用。
.env 文件只是把这个字典的内容先写在一个文本文件里，再由 python-dotenv 读进去，
这样我们就不用每次手工去设置系统环境变量了。
"""

import os

from dotenv import load_dotenv

# load_dotenv() 会找到当前项目下的 .env 文件，
# 把里面的每一行 "KEY=VALUE" 塞进 os.environ，相当于替你执行了 os.environ["KEY"] = "VALUE"
load_dotenv()


class Settings:
    """把配置收进一个类里 —— 和你 alien_invasion/settings.py 里的 Settings 是同一个思路。"""

    def __init__(self) -> None:
        # os.getenv("名字", "默认值")：从环境变量取值；没取到就用默认值
        self.api_key: str = os.getenv("LLM_API_KEY", "")
        self.base_url: str = os.getenv("LLM_BASE_URL", "https://api.deepseek.com/v1")
        self.model: str = os.getenv("LLM_MODEL", "deepseek-chat")
        self.timeout: int = int(os.getenv("LLM_TIMEOUT", "30"))

        # 配置里写了 int 就要转成 int —— 因为环境变量读出来永远是字符串！
        # 这一点很容易踩坑：os.getenv("LLM_TIMEOUT") 拿到的是 "30" 而不是 30。
        # （想省掉这些转换，可以进阶去用 pydantic-settings，见 README 的"加餐"）

    def describe(self) -> dict:
        """对外展示配置时，密钥必须打码 —— 这是最基本的职业习惯。"""
        return {
            "base_url": self.base_url,
            "model": self.model,
            "timeout": self.timeout,
            "api_key_loaded": bool(self.api_key),
            "api_key_preview": self.mask(self.api_key),
        }

    @staticmethod
    def mask(key: str) -> str:
        """把密钥打码，只留下头尾各 4 位，中间用 * 占位。"""
        if not key:
            return "(未配置)"
        if len(key) <= 8:
            return "*" * len(key)
        return key[:4] + "*" * (len(key) - 8) + key[-4:]


# 模块级只建一个实例，别的地方 from config import settings 直接用。
# （这其实就是你在 part5-进阶/单例模式.py 里学的"单例"思想）
settings = Settings()
