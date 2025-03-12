class Car:
    wheel = 4
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"i have a {self.name}")


class Motor(Car):
    wheel = 2


m = Motor('honda')
m.show()
print(m.wheel)

# MRO = Method resolution order
help(m)
print(m.__class__.mro())