import re


def extract_emails(text):
    # 返回邮箱列表
    r1 = r"[\w-]+(?:\.[\w-]+)*@[\w-]+(?:\.[\w-]+)+"
    print(re.findall(r1, text))

def extract_orders(text):
    # 返回订单号列表
    r2 = r"[a-zA-z]{3}-[0-9]{8}-[0-9]{3}"
    return re.findall(r2, text)
    


def clean_text(text):
    # 返回清理空白后的字符串
    return re.sub(r"\s+", "", text)

if __name__ == "__main__":
    text = """
    联系人：Celine，邮箱：celine@example.com,
    备用邮箱：support@test.org,
    订单号：ORD-20260915-001,
    订单号：ORD-20260915-002,
    备注：请   尽快处理，    谢谢！
    """
    # text = "celine@example.com"
    print(extract_emails(text))
    print(extract_orders(text))
    print(clean_text(text))
