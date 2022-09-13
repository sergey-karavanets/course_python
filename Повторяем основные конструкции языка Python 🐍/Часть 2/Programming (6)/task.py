# put your python code here
def determine_winner(x, y):
    if (x == 'камень' and y == 'ножницы') or (x == 'бумага' and y == 'камень') or (x == 'ножницы' and y == 'бумага'):
        return 'Тимур'
    elif (y == 'камень' and x == 'ножницы') or (y == 'бумага' and x == 'камень') or (y == 'ножницы' and x == 'бумага'):
        return 'Руслан'
    else:
        return 'ничья'


x = input()  # Тимур
y = input()  # Руслан

print(determine_winner(x, y))