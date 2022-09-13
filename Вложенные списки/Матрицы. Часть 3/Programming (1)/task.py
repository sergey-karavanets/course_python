# put your python code here
def add_numbers_in_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            if i + j + 1 == n:
                matrix[i][j] = 1
            if (i <= j and i < n - 1 - j) or (i >= j and i < n - 1 - j):
                matrix[i][j] = 0
            if (i <= j and i > n - 1 - j) or (i >= j and i > n - 1 - j):
                matrix[i][j] = 2
    print_matrix(matrix, n)

def print_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


n = int(input())
matrix = []
for _ in range(n):
    temp = [9]*n
    matrix.append(temp)

add_numbers_in_matrix(matrix, n)