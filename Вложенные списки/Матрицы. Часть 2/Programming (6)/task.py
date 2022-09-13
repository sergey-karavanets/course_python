# put your python code here
def rotate_matrix(matrix, n):
    for i in range(n):
        for j in range(n-1, -1, -1):
            print(matrix[j][i], end=' ')
        print()


n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

rotate_matrix(matrix, n)