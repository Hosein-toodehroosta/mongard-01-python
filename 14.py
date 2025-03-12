try:
    f = open('01.py')
    print(str.upper('hosein'))
except FileNotFoundError:
    print('File does not exist')
except TypeError:
    print('Your name must be string')
else:
    print('Hello hosein')
finally:
    print('Goodbye')