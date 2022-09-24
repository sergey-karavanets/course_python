with open('goats.txt', encoding='utf-8') as goats, open('answer.txt', 'w', encoding='utf-8') as answer:
    temp = goats.read().split('GOATS')
    temp2 = filter(lambda x: x if x != '' else None, temp[1].split('\n'))
    result = {}
    for goat in temp2:
        result[goat] = result.get(goat, 0) + 1
    summa = sum(result.values())
    for key, value in result.items():
        if value / summa > 0.070001:
            print(key, file=answer)