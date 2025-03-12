class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.email = f'{self.first_name}_{self.last_name}@gmail.com'

    @property
    def full_name(self):        # property method
        return f'{self.first_name} {self.last_name}'
    @property
    def email(self):        # property method
        return f'{self.first_name}_{self.last_name}@gmail.com'


a = Person('John', 'Doe')
a.first_name = 'hosein'
print(a.first_name)
print(a.last_name)
print(a.email)
print(a.full_name)