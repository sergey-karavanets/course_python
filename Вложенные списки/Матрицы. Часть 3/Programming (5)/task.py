# put your python code here
def fill_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            if i <= j and i <= n - 1 - j:
                matrix[i][j] = 1
            if i >= j and i >= n - 1 - j:
                matrix[i][j] = 1
    print_matrix(matrix, n)

def print_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


n = int(input())
matrix = [[0] * n for _ in range(n)]

fill_matrix(matrix, n)