from 银行账户 import Bank
import json
class SavePersonalInfo(Bank):
    def __init__(self, name, count, password, phone):
        super().__init__(name, count, password, phone)

    def save(self):
        data = {
            "name": self.name,
            "count": self.count,
            "password": self.password,
            "phone": self.phone
        }

        with open("acount_data.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self):
        try:
            with open("acount_data.json", "r", encoding="UTF-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("未找到该文件，请先创建账户。")
        else:
            print(data)

