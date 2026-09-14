from 通知器 import SNSNotifier
#from 保存账户信息 import SavePersonalInfo
import json
class Bank:
    def __init__(self):
        self.loadInfo()

    def atm(self):
        a = 1
        while(True):
            pw = int(input("请输入密码:\n"))
            if pw == self.password:
                print(f"Name:{self.name}\nCount: {self.count}\nMoney:{self.money}")
                print("请选择服务\n")
                option = int(input("取钱输入0，存钱输入1:\n"))
                if option == 1:
                    self.deposit()
                    self.saveInfo()
                    break
                elif option == 0:
                    self.withdraw()
                    self.saveInfo()
                    break
            elif a == 5:
                print("密码错误次数过多，已关闭服务")
                break
            else:
                print("密码错误，请重新输入")
                a += 1

    def deposit(self):
        while(True):
            try:
                num = float(input("请输入你要存的金额:\n"))
            except ValueError:
                print("请输入数字")
                continue
            if num >= 0.00:
                self.money += num
                print(f"当前余额是{self.money}元")
                msg = f"已向所在账户充值{num}元"
                self.notifier.send(msg)
                print("服务结束")
                break
            else:
                print("请输入正确的金额")

    def withdraw(self):
            while(True):
                try:
                    num = float(input("请输入你要取的金额:\n"))
                except ValueError:
                    print("请输入数字")
                    continue
                if num < 0:
                    print("金额必须大于0")
                elif num <= self.money:
                    self.money -= num
                    print(f"当前余额是{self.money}元")
                    msg = f"已向所在账户扣款{num}元"
                    self.notifier.send(msg)
                    print("服务结束")
                    break
                elif num > self.money:
                    print("余额不足")
                    break
                else:
                    print("请输入正确的金额")

    def saveInfo(self):
            data = {
                "name": self.name,
                "count": self.count,
                "password": self.password,
                "phone": self.phone,
                "money": self.money
            }
    
            with open("D:/Python学习/练习题/acount_data.json", "w", encoding="UTF-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    def loadInfo(self):
            try:
                with open("D:/Python学习/练习题/acount_data.json", "r", encoding="UTF-8") as f:
                    data = json.load(f)
                    self.name = data['name']
                    self.count = data['count']
                    self.password = data['password']
                    self.money:float = data['money']
                    self.phone = data['phone']
                    self.notifier = SNSNotifier(data['name'], data['phone'])

            except FileNotFoundError:
                print("未找到该文件，请先创建账户。")
