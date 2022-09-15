from random import choice

file = open('lines.txt', encoding='utf-8')
random_line = choice(file.readlines())
file.close()
print(random_line)