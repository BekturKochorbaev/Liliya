
def change_numbers(a):
    new_list = []
    for i in a:
        new_list.append(i * a.index(i))
    return new_list

print(change_numbers([4, 5, 7]))
