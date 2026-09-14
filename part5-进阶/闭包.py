def create_acount(sum):
    def atm(num , deposit = True):
        nonlocal sum
        if deposit :
            sum += num
            print(f"存款：+{num},余额：{sum}")
        else:
            sum -= num
            print(f"存款：+{num},余额：{sum}")
    return atm
fun1 = create_acount(100)
fun1(50,True)
fun1(100,False)