# super method
class Car:      # parent | superclass
    wheel = 4
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"i have a {self.name}")


class Motor(Car):       # child | subclass
    wheel = 2

    def __init__(self, name, helmet):
        super().__init__(name)
        self.helmet = helmet


m = Motor('Honda', 'Yes')
m.show()