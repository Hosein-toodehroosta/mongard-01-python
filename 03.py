class Car:
    def __init__(self, n, p):
        self.name = n
        self.price = p
    def show(self):
        print(f"{self.name} costs {self.price}")


a = Car('Pride', 100)
b = Car('Benz', 800)

a.show()
b.show()
