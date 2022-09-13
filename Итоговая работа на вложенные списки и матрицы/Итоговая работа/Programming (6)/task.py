# put your python code here
def put_the_queen(matrix, letter, number):
    matrix[number][letter] = 'Q'
    print_matrix(matrix)

def fill_matrix(matrix, letter, number):
    for i in range(8):
        for j in range(8):
            if i+1 >= number >= i-1 and j+1 >= letter >= j-1:
                matrix[i][j] = '*'
    add_diagonals(matrix, letter, number)

def add_diagonals(matrix, letter, number):

    for i in range(8):
        for j in range(8):
            if i - j == number - letter:
                matrix[i][j] = '*'
            if i + j == number + letter:
                matrix[i][j] = '*'
    add_lines(matrix, letter, number)

def add_lines(matrix, letter, number):
    for i in range(8):
        for j in range(8):
            if i == number or j == letter:
                matrix[i][j] = '*'
    put_the_queen(matrix, letter, number)

def print_matrix(matrix):
    for i in range(8):
        for j in range(8):
            print(matrix[i][j], end=' ')
        print()


dict_for_letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
dict_for_numbers = {'8':0, '1':7, '2':6, '3':5, '4':4, '5':3, '6':2, '7':1}
place = list(input())
letter = dict_for_letters[place[0]]
number = dict_for_numbers[place[1]]
matrix = [['.'] * 8 for _ in range(8)]

fill_matrix(matrix, letter, number)
