class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class Factory:
    def get_person(self,p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()

factory = Factory()
person1 = factory.get_person('w')
person2 = factory.get_person('s')
person3 = factory.get_person('t')

print(person1)
print(person2)
print(person3)