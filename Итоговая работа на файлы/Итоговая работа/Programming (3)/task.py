with open('words.txt', encoding='utf-8') as words:
    temp = words.read().split()
    length = 0
    for word in temp:
        if length < len(word):
            length = len(word)
    for word in temp:
        if length == len(word):
            print(word)