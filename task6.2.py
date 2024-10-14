fruits1 = ('apple', 'cherry', 'banana',)
fruits2 = ['apple', 'cherry', 'blueberry', 'orange', 'melon']
fruits1_new = set(fruits1)
fruits2_new = set(fruits2)

difference_set = fruits2_new.difference(fruits1_new)

print(len(difference_set))