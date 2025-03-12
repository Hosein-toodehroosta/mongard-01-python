"""
        Access point ==> public, protected, private
"""

class Person:
    name = 'hosein'     # public
    _age = 40       # protected
    __height = 173      # private

    def __private_show(self):       # private method
        print('This method is private')

class Male(Person):
    def show(self):
        print(self._age)
    def show_height(self):
        print(self.__height)


m = Male()
m.show()
p = Person()
print(Person._age)
print(Person._Person__height)       # name mangling
print(p._Person__height)
p._Person__private_show()     # name mangling
m.show_height()
print(Person._height)