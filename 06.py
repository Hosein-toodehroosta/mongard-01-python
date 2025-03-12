class Car:
    obj_nums = 0
    def __init__(self, n, p):
        self.name = n
        self.price = p

        Car.obj_nums += 1
    def show_wheel(self):
        print(f"{self.name} has {self.wheel} wheels and costs is {self.price}$")

a = Car('Pride', 100)
b = Car('Benz', 800)

print(Car.obj_nums)
