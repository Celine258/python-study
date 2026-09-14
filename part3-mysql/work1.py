class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def introduce(self):
        print(f"学生姓名：{self.name}，年龄：{self.age}，地址：{self.address}")
name1, age1, address1 = input("依次输入姓名，年龄，地址").split()
student1 = Student(name1,age1,address1)
student1.introduce()