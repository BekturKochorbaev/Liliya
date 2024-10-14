fruits = ['apple', 'banana', 'cherry', 'carrot']
word = input('name:').lower()

if word in fruits:
    print(fruits.index(word))
else:
    print('No')