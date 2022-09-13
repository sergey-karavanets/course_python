# put your python code here
def fill_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = '0'
            if i + 1 == j or i - 1 == j:
                matrix[i][j] = '1'
            if i + 2 == j or i - 2 == j:
                matrix[i][j] = '2'
            if i + 3 == j or i - 3 == j:
                matrix[i][j] = '3'
            if i + 4 == j or i - 4 == j:
                matrix[i][j] = '4'
            if i + 5 == j or i - 5 == j:
                matrix[i][j] = '5'
            if i + 6 == j or i - 6 == j:
                matrix[i][j] = '6'
            if i + 7 == j or i - 7 == j:
                matrix[i][j] = '7'
            if i + 8 == j or i - 8 == j:
                matrix[i][j] = '8'
            if i + 9 == j or i - 9 == j:
                matrix[i][j] = '9'
    print_matrix(matrix, n)

def print_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


n = int(input())
matrix = [[9] * n for _ in range(n)]

fill_matrix(matrix, n)