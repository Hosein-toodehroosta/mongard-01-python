class Car:
    wheel = 4  # class variable
    def __init__(self, n, p):
        self.name = n   # instance variable
        self.price = p
        print(f"{self.name} has {Car.wheel} wheels and costs is {self.price}$")


a = Car('Pride', 100)
b = Car('Benz', 800)

a.wheel = 5

print(Car.__dict__) # shows class attributes
print(a.__dict__)   # shows instance attributes
print(b.__dict__)   # shows instance attributes
