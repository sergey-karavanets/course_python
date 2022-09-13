# put your python code here
def multiply_matrices(matrix_1, matrix_2, matrix_3, n, m, k):
    for i in range(n):
        for j in range(k):
            for x in range(m):
                matrix_3[i][j] += matrix_1[i][x] * matrix_2[x][j]
    print_matrix(matrix_1, matrix_2, matrix_3, n, m, k)

def print_matrix(matrix_1, matrix_2, matrix_3, n, m, k):
    for i in range(n):
        for j in range(k):
            print(matrix_3[i][j], end=' ')
        print()


n, m = [int(i) for i in input().split()]
matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
input()
m2, k = [int(i) for i in input().split()]
matrix_2 = [[int(i) for i in input().split()] for _ in range(m2)]
matrix_3 = [[0] * k for _ in range(n)]

multiply_matrices(matrix_1, matrix_2, matrix_3, n, m, k)