with open(input(), encoding='utf-8') as file:
    if len(file.readlines()) > 10:
        file.seek(0)
        temp = file.readlines()
        for i in range(-10, 0):
            print(temp[i].strip())
    else:
        file.seek(0)
        for line in file.readlines():
            print(line.strip())