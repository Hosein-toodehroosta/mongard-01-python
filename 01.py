class Car:  # blueprint
    def show(self):
        print('This is Method...')
        print(self)

a = Car()   # object | instance
b = Car()

a.name = 'Pride'
b.name = 'Benz' # attribute | property

a.show()    # dot notation
print(a)
b.show()
