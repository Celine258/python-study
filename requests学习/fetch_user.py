import json
import requests
import logging
import argparse




logging.basicConfig(
    filename="D:/Python学习/requests学习/git_user.log",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def fetch_user(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url=url,timeout=10)
        response.raise_for_status()
        data = response.json()
        logging.info("成功拉取用户信息")
        return data
    except requests.exceptions.RequestException:
        logging.exception("请求用户信息失败")
        return None


def save_info(data):
    try:
        with open(arg.output, "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            logging.info("存入信息成功")
            print("success")
    except OSError:
        logging.exception("信息写入失败")
        print("信息写入失败，请检查日志")

if __name__ == "__main__":
    #创建解析器
    parser = argparse.ArgumentParser(description="查询github用户信息")
    #定义需要哪些参数
    parser.add_argument("username", help="查询用户的名字")
    parser.add_argument("--output", default="D:/Python学习/requests学习/git_user.json", help="文件保存的路径")
    #解析传入的参数
    arg = parser.parse_args()

    data = fetch_user(arg.username)
    if data is not None:
        save_info(data)
        with open(arg.output, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(data["login"])
        print(data["public_repos"])  # 公开仓库数量
        print(data["html_url"])      # GitHub 主页
    else:
        print("文件为空")
