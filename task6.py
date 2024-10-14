car = {'name': 'tesla', 'model': 'X', 'price': 54000}
name = input('write a key: ')
if name in car:
    print(car[name])
else:
    print('No')

