# Добавление элемент в список
#person = []
#name = input('first name: ')
#age = int(input('your age: '))
#print(person)
'''
first name: Marlen
your age: 11
['Marlen', 11]
'''

person = []
name = str(input('name:'))
age = int(input('age:'))
person.append(name)
person.append(age)
print(person)