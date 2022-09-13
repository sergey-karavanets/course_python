# put your python code here
def print_matrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()

def print_reverse_matrix(matrix, rows, cols):
    for i in range(cols):
        for j in range(rows):
            print(matrix[j][i], end=' ')
        print()


n, m = int(input()), int(input())
matrix = []
for _ in range(n):
    temp = [input() for _ in range(m)]
    matrix.append(temp)

print_matrix(matrix, n, m)
print()
print_reverse_matrix(matrix, n, m)
