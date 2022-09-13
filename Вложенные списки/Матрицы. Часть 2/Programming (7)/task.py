# put your python code here
def print_matrix(matrix, letter, number, n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

def add_horse(matrix, letter, number, n):
    matrix[number][letter] = 'N'
    add_possible_moves(matrix, letter, number, n)

def add_possible_moves(matrix, letter, number, n):
    for i in range(n):
        for j in range(n):
            if i != number and j != letter and number-2 <= i <= number+2 and letter-2 <= j <= letter+2 and (number + letter)-3 <= i + j <= (number + letter)+3 and (number + letter) % 2 != (i + j) % 2:
                matrix[i][j] = '*'
    print_matrix(matrix, letter, number, n)


dict_for_letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
dict_for_numbers = {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}
coordinates = list(input())
letter = dict_for_letters[coordinates[0]]
number = dict_for_numbers[int(coordinates[1])]
n = 8
matrix = []
for _ in range(n):
    temp = ['.']*8
    matrix.append(temp)

add_horse(matrix, letter, number, n)