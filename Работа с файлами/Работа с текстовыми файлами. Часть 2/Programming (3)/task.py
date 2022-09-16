with open('numbers.txt', encoding='utf-8') as file:
    for line in list(file):
        print(sum(map(int, filter(lambda x: str(x.strip()) != '', line.split()))))