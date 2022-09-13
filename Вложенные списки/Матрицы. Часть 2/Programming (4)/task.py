# put your python code here
def diagonal_swap(matrix, n):
    for i in range(n):
        matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
    print_matrix(matrix, n)

def print_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

diagonal_swap(matrix, n)