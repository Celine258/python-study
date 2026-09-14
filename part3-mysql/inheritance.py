from work2 import Phone
class Phone2(Phone):#单继承
    IMEI = None
    producer = "MI"

phone = Phone2()
phone.call_by_5g()

class NFCRender:
    nfc_type = "五代"
    producer = "me"

    def read_card(self):
        print("读卡")

    def write_card(self):
        print("写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控已开启")

class Phone_new(Phone2,RemoteControl,NFCRender):#多继承
    pass

phone_new = Phone_new()
phone_new.control()
phone_new.read_card()


#复写，重新定义继承后的成员属性和成员方法
class MyPhone(Phone2):
    producer = "mhy"

    def call_by_5g(self):
        print("无法使用5g")
        #Phone2.call_by_5g(self)
        super().call_by_5g()


phone3 = MyPhone()
phone3.call_by_5g()
