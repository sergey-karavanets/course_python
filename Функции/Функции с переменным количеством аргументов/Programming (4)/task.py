def print_products(*args):
    count = 0
    for arg in args:
        if type(arg) == str and arg != '':
            count += 1
            print(f'{count}) {arg}')
    if count == 0:
        print('Нет продуктов')
