file = open('prices.txt', encoding='utf-8')
total_list = [x for x in file.readlines()]
total = 0
for i in total_list:
    temp = i.split('\t')
    total += int(temp[1]) * int(temp[2])
print(total)