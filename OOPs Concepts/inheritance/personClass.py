class Person():

    def __init__(self, msg, name, age):
        self.msg = msg
        self.name = name
        self.age = age

    def printMsg(self):
        print("welcome {}".format(self.name))

class Student(Person):
    pass

s1 = Student("dummy","Stuent",25)
s1.printMsg()