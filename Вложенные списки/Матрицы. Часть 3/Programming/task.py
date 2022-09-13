# put your python code here
def add_stars(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if i % 2 == 0 and j % 2 == 1:
                matrix[i][j] = '*'
            if i % 2 == 1 and j % 2 == 0 and i != 0:
                matrix[i][j] = '*'
    print_matrix(matrix, n, m)

def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()


d = list(map(int, input().split()))
n = d[0]
m = d[1]
matrix = []
for _ in range(n):
    temp = ['.']*m
    matrix.append(temp)

add_stars(matrix, n, m)