with open('population.txt', encoding='utf-8') as file:
    for line in file.readlines():
        temp = line.split()
        if temp[0][0].strip() == 'G' and int(temp[-1].strip()) > 500000:
            print(temp[0])