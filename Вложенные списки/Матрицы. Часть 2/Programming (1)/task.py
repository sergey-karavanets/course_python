# put your python code here
def search_index_maximum(matrix, n, m):
    maximum = -99999
    for i in range(n):
        if max(matrix[i]) > maximum:
            maximum = max(matrix[i])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == maximum:
                return i, j


n, m = int(input()), int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

print(*search_index_maximum(matrix, n, m))