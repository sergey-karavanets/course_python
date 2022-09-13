# put your python code here
def print_matrix(matrix, n):
    for i in range(n-1, -1, -1):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

print_matrix(matrix, n)