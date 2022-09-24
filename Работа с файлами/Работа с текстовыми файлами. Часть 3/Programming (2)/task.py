with open('input.txt', 'r', encoding='utf-8') as file_input, open('output.txt', 'w', encoding='utf-8') as file_output:
    temp = [list(i) for i in enumerate(file_input, 1)]
    file_output.writelines(map(lambda x: str(x[0]) + ') ' + str(x[1]), temp))