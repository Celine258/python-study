import argparse
import logging
import json
import re

logging.basicConfig(
    filename="D:/Python学习/re.log",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

parse = argparse.ArgumentParser(description="输入文件地址")
parse.add_argument("input_path", help="读取文件的地址")
parse.add_argument("--output_path", default="D:/Python学习/data.json", help="输出文件的地址")
arg = parse.parse_args()

r1 = r"[\w-]+(?:\.[\w-]+)*@[\w-]+(?:\.[\w-]+)+"
r2 = r"ORD-[0-9]{8}-[0-9]{3}"

try:
    with open(arg.input_path, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    logging.exception("未找到文件")
    raise SystemExit(1)
except UnicodeDecodeError:
    logging.exception("编码错误")
    raise SystemExit(1)
except PermissionError:
    logging.exception("没有对应权限")
    raise SystemExit(1)
except OSError:
    logging.exception("其他操作系统相关的读取错误")
    raise SystemExit(1)
email = re.findall(r1, text)
order = re.findall(r2, text) 
data = {
    "name": "Celine",
    "email": email,
    "order": order
}
try:
    with open(arg.output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
except OSError:
    logging.exception("数据写入失败")
    raise SystemExit(1)
else:
    logging.info("数据保存成功")