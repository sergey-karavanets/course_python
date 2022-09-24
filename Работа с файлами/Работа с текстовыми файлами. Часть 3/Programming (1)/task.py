from random import randint

rand_num = [str(randint(111,777)) for _ in range(25)]

with open('random.txt', 'w', encoding='utf-8') as file:
    file.writelines(map(lambda x: x + '\n', rand_num))