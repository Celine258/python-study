class Notifier:
    def __init__(self, name):
        self.name = name
    def send(self,msg):
        raise NotImplementedError("还未设置这个方法")

class SNSNotifier(Notifier):
    def __init__(self, name, phone):
        super().__init__(name)
        self.phone = phone
    def send(self, msg:str):
        print(f"已向{self.phone}的{self.name} 先生/女士 发送消息：{msg}")

class MailNotifier(Notifier):
    def __init__(self, name, mail):
        super().__init__(name)
        self.mail = mail

    def send(self, msg:str):
        print(f"已向{self.mail}的{self.name} 先生/女士 发送消息：{msg}")