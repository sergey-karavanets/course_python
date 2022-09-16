with open('file.txt', encoding='utf-8') as file:
    content = list(file)
    total_letters = 0
    total_words = 0
    total_lines = len(content)
    for line in content:
        total_words += len(line.split())
        for letter in line:
            if letter.isalpha():
                total_letters += 1
print('Input file contains:')
print(total_letters, 'letters')
print(total_words, 'words')
print(total_lines, 'lines')