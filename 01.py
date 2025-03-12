class Car:  # blueprint
    pass

a = Car()   # object | instance
b = Car()


a.name = 'Pride'    # attribute | property
b.name = 'Benz'

a.price = 100   # dot notation
b.price = 900

print(f"{a.name} costs {a.price} $")
print(f"{b.name} costs {b.price} $")