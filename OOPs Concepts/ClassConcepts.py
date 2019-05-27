import os, sys
class Student():
    """ A Sample Student class """
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

        print("student created:" + self.fullName,self.email)

    @property
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @property
    def email(self):
        return f'{self.firstName}.{self.lastName}@gmail.com'

st1 = Student('Krishna', 'Kummari')
st2 = Student('watsan', 'kory')
