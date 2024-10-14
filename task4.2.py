fruits = ['apple', 'banana', 'cherry', 'carrot', 'cherry', 'apple']
name = input('write name of fruit:')

if name in fruits:
    print(fruits.count(name))
else:
    print('0')