
''' Удаления элемента из списка
cars = ['tesla', 'audi', 'bmw', 'mers']

name = input('name: ')

name: tesla
['audi', 'bmw', 'mers']

name: mers
['tesla', 'audi', 'bmw']
'''

cars = ['tesla', 'audi', 'bmv', 'mers']
name = input('name: ')
cars.remove(name)
print(cars)