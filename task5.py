numbers_one = (1, 2, 5, 7, 9)
numbers_two = (1, 8, 2, 3, 9)
set_1 = set(numbers_one)
set_2 = set(numbers_two)

all_set = set_1.intersection(set_2)
length = len(all_set)
print(f"окшош сандар:{length}")