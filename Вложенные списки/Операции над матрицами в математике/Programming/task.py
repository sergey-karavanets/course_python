# put your python code here
def sum_matrix(matrix_one, matrix_two, matrix_three, n, m):
    for i in range(n):
        for j in range(m):
            matrix_three[i][j] = matrix_one[i][j] + matrix_two[i][j]
    print_matrix(matrix_three, n, m)

def print_matrix(matrix_three, n, m):
    for i in range(n):
        for j in range(m):
            print(matrix_three[i][j], end=' ')
        print()


n, m = [int(i) for i in input().split()]
matrix_one = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix_one.append(temp)

input()

matrix_two = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix_two.append(temp)

matrix_three = [[0] * m for _ in range(n)]

sum_matrix(matrix_one, matrix_two, matrix_three, n, m)