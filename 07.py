# Methods => 1.instance method, 2.class method, 3.static method

import datetime
class Person():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self): # instance method
        print(f"{self.name} is {self.height} height and is {self.age} age")  # instance method
    @classmethod        # class method
    def from_birth(cls, name, height, age):     # class method
        return cls(name, height, datetime.datetime.now().year - age)

    @staticmethod       # static method
    def is_adult(age):
        if age > 18:
            print('Yes')
        else:
            print('No')


p1 = Person('hosein', 173, 1985)
p1.show()

p2 = Person.from_birth('ali', 180, 1985)
p2.show()

Person.is_adult(23)