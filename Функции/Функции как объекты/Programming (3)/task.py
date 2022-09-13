def name(athlet):
    return athlet[0]

def age(athlet):
    return athlet[1]

def growth(athlet):
    return athlet[2]

def weight(athlet):
    return athlet[3]


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
commands = {1: name, 2: age, 3: growth, 4: weight}

command = int(input())

my_list = sorted(athletes, key=commands[command])
for i in my_list:
    print(*i)