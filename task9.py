numbers = [4, 2, 6, 0, 2, 7, 8]
if numbers[0] == 0:
    print(0)
else:
    total = 1
    for i in numbers:

        if i == 0:
            break
        total *= i
    print(total)
