# override the methods
class Car:
    wheel = 4
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"i have a {self.name}")


class Motor(Car):
    wheel = 2

    def show(self):
        super().show()
        print(f'i ride a {self.name}')


m = Motor('Honda')
m.show()