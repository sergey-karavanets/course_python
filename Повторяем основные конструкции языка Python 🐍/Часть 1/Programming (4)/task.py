# put your python code here
def zodiac_sign(year):
    y = year % 12
    if y == 1:
        print('Петух')
    elif y == 2:
        print('Собака')
    elif y == 3:
        print('Свинья')
    elif y == 4:
        print('Крыса')
    elif y == 5:
        print('Бык')
    elif y == 6:
        print('Тигр')
    elif y == 7:
        print('Заяц')
    elif y == 8:
        print('Дракон')
    elif y == 9:
        print('Змея')
    elif y == 10:
        print('Лошадь')
    elif y == 11:
        print('Овца')
    elif y == 0:
        print('Обезьяна')


n = int(input())

zodiac_sign(n)