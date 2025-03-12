class Car:
    wheel = 4
    def __init__(self, n, p):
        self.name = n
        self.price = p
    def show_wheel(self):
        print(f"{self.name} has {self.wheel} wheels and costs is {self.price}$")

a = Car('Pride', 100)
b = Car('Benz', 800)

a.wheel = 5

a.show_wheel()
b.show_wheel()

print(a.__dict__)
print(b.__dict__)
print(Car.__dict__)
print(a.__class__.wheel)
