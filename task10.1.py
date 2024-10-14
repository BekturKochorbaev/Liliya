def two_nums(a, b):
    с = a + b
    t = sorted(с, reverse=True)
    return list(t)
print(two_nums((3, 6 , 8), (8, 6, 2)))
