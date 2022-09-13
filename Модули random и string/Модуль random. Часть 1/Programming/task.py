import random

n = int(input())    # количество попыток
for _ in range(n):
    num = random.randint(0, 1)
    if num == 0:
        print('Орел')
    else:
        print('Решка')