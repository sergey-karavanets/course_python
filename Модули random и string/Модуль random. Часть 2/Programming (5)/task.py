from random import randrange as r

def fill_matrix(matrix):
    digits_used = []
    for i in range(5):
        for j in range(5):
            random_num = r(1, 76)
            if random_num not in digits_used:
                matrix[i][j] = random_num
                digits_used.append(random_num)
            else:
                while random_num in digits_used:
                    random_num = r(1, 76)
                matrix[i][j] = random_num
                digits_used.append(random_num)
    zero_in_matrix(matrix)

def zero_in_matrix(matrix):
    matrix[2][2] = 0
    print_matrix(matrix)

def print_matrix(matrix):
    for i in range(5):
        for j in range(5):
            print(str(matrix[i][j]).ljust(3), end='')
        print()

matrix = [[0] * 5 for _ in range(5)]
fill_matrix(matrix)