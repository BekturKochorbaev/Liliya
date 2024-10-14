numbers = [4, 7, 5, 9, 3]
max_digit = numbers[0]

for number in numbers:
    if number > max_digit:
        max_digit = number

print("Самая большая цифра:", max_digit)
