# put your python code here
def print_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print()


n = int(input())
matrix = [[int(i) for i in input().split()] for i in range(n)]

print_matrix(matrix, n)