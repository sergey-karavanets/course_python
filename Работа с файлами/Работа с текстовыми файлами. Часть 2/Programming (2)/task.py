with open('lines.txt', encoding='utf-8') as file:
    content = file.readlines()
    max_len = 0
    for line in content:
        if len(line) > max_len:
            max_len = len(line)
    for line in content:
        if len(line) == max_len:
            print(line.strip())