with open('class_scores.txt', 'r', encoding='utf-8') as old_file, open('new_scores.txt', 'w', encoding='utf-8') as new_file:
    temp = [i.strip().split() for i in old_file.readlines()]
    new_file.writelines(map(lambda x: str(x[0]) + ' ' + str(int(x[1]) + 5) + '\n' if int(x[1]) <= 95 else str(x[0]) + ' 100\n', temp))