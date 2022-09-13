# put your python code here
def print_matrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()


n = int(input())  # number of rows
m = int(input())  # number of cols
matrix = []
for i in range(n):
    temp = [input() for _ in range(m)]
    matrix.append(temp)

print_matrix(matrix, n, m)