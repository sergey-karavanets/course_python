import random

length = int(input())    # длина пароля
password = []
for i in range(length):
    if i % 2 == 0:
        password.append(chr(random.randint(65, 89)))
    else:
        password.append(chr(random.randint(97, 121)))
print(*password, sep='')