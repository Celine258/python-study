class Phone:
    __is_5g_enable: bool = False

    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5G通话已开启")
        else:
            print("5G关闭，使用4G网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中...")

#phone = Phone()
#phone.call_by_5g()
#print(phone.__is_5g_enable)
