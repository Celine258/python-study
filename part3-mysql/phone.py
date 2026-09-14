class Phone:
    __current_voltage = None

    name = None

    def __keep_single_core(self):
        print("让cpu以单核形式运行")

phone = Phone()
phone.__current_voltage = "100w"
#phone.__keep_single_core()
print(phone.__current_voltage)