numbers_one = [3, 5, 8]
numbers_two = [0, 2, 1, 7]
numbers_one.extend(numbers_two)

print(sorted(numbers_one, reverse=True))

''' # 2-Варивнт
numbers_one = [3, 5, 8]
numbers_two = [0, 2, 1, 7]

numbers_one.extend(numbers_two)
numbers_one.sort(reverse=True)
print(numbers_one)
3-вариант
numbers_one = [3, 5, 8]
numbers_two = [0, 2, 1, 7]

numbers = numbers_one + numbers_two
numbers.sort(reverse=True)
print(numbers)
'''