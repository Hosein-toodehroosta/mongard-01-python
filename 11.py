# dunder methods
class Car:      # parent | superclass
    wheel = 4
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show(self):
        print(f"i have a {self.name}")
    def __str__(self):
        return f'my car brand is{self.name}'
    def __add__(self, other):
        return self.price + other.price
    def __len__(self):
        return len(self.name)


a = Car("Benz", 800)
b = Car("Pride", 100)

print(a)
print(a + b)
print(len(a))
