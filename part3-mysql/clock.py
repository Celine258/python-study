class Clock:
    #id = None
    #price = None
    def __init__(self,id,price):
        self.id = id
        self.price = price
        
    def ring(self):
        import winsound
        winsound.Beep(2000,2000)

clock = Clock(1,"12RMB")
#clock.id = 1
#clock.price = "12RMB"
print(f"Price:{clock.price},ID:{clock.id}")
clock.ring()
#面向对象本质就是创建类，基于类去创建对象，让对象去做工作。