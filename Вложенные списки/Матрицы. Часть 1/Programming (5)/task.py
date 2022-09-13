# put your python code here
def search_maximum(matrix, n):
    maximum = -99999
    for i in range(n):
        for j in range(n):
            if i >= j and i <= n-1-j and matrix[i][j] > maximum:
                maximum = matrix[i][j]
    for i in range(n):
        for j in range(n):
            if i <= j and i >= n-1-j and matrix[i][j] > maximum:
                maximum = matrix[i][j]
    return maximum


n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

print(search_maximum(matrix, n))