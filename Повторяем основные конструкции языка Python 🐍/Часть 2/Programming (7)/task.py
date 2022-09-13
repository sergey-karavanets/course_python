# put your python code here
def determine_winner_3(x, y):
    if (x == 'камень' and y == 'ножницы') or (x == 'бумага' and y == 'камень') or (x == 'ножницы' and y == 'бумага'):
        return 'Тимур'
    elif (y == 'камень' and x == 'ножницы') or (y == 'бумага' and x == 'камень') or (y == 'ножницы' and x == 'бумага'):
        return 'Руслан'
    else:
        return 'ничья'

def determine_winner_5(x, y):
    if (x == 'ящерица' and y == 'Спок') or (x == 'ящерица' and y == 'бумага') or (x == 'камень' and y == 'ящерица') or (x == 'бумага' and y == 'Спок') or (x == 'Спок' and y == 'ножницы') or (x == 'Спок' and y == 'камень') or (x == 'бумага' and y == 'Спок') or (x == 'ножницы' and y == 'ящерица'):
        return 'Тимур'
    elif (y == 'ящерица' and x == 'Спок') or (y == 'ящерица' and x == 'бумага') or (y == 'камень' and x == 'ящерица') or (y == 'бумага' and x == 'Спок') or (y == 'Спок' and x == 'ножницы') or (y == 'Спок' and x == 'камень') or (y == 'бумага' and x == 'Спок') or (y == 'ножницы' and x == 'ящерица'):
        return 'Руслан'
    else:
        return 'ничья'

x = input()  # Тимур
y = input()  # Руслан

if x in ['камень', 'ножницы', 'бумага'] and y in ['камень', 'ножницы', 'бумага']:
    print(determine_winner_3(x, y))
else:
    print(determine_winner_5(x, y))