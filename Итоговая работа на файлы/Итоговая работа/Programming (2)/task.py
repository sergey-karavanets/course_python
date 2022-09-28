with open('grades.txt', encoding='utf-8') as grades:
    temp = [i.split() for i in grades.readlines()]
    total = 0
    for name, g1, g2, g3 in temp:
        if int(g1) >= 65 and int(g2) >= 65 and int(g3) >= 65:
            total += 1
    print(total)