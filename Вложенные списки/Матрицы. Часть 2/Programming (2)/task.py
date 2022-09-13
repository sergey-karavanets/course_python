# put your python code here
def swap_cols(matrix, n, m, i, j):
    for k in range(n):
        matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
    print_matrix(matrix, n, m)

def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()


n, m = int(input()), int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)
rows = list(map(int, input().split()))
i = rows[0]
j = rows[1]

swap_cols(matrix, n, m, i, j)