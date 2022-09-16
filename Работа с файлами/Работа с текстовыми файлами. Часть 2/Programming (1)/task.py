with open('data.txt', encoding='utf-8') as file:
    temp = file.readlines()
    for i in range(len(temp)):
        print(temp[len(temp)-i-1].strip())