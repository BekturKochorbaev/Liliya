import random
b = int(input('Жогорку санды жазыныз:'))
a = int(input('Томонку санды жазыныз:'))
n = random.randint(a, b)
sum = 0
while True:
    c = int(input(f"{a} жана {b} ортосундагы санды табыныз"))
    sum += 1
    if c < n:
        print('Табышмактуу сан чон')
    elif c > n:
        print('Табышмактуу сан кичине')
    elif c == n:
        print(f'Сиз табышмактуу санды {sum} аракетте таптыныз')
        break







