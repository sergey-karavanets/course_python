# put your python code here
def print_snowflake(matrix, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = '*'
            if i == n - 1 - j:
                matrix[i][j] = '*'
            if (n // 2) == i:
                matrix[i][j] = '*'
            if (n // 2) == j:
                matrix[i][j] = '*'
    print_matrix(matrix, n)

def print_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


n = int(input())
matrix = [['.'] * n for _ in range(n)]

print_snowflake(matrix, n)