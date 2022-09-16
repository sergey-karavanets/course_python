import random

with open('first_names.txt', encoding='utf-8') as names, open('last_names.txt', encoding='utf-8') as surnames:
    list_with_names = list(names)
    list_with_surname = list(surnames)
    for _ in range(3):
        print(random.choice(list_with_names).strip(), random.choice(list_with_surname).strip())