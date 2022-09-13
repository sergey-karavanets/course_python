# put your python code here
def search_maximum(matrix, n):
    maximum = -99999
    for i in range(n):
        for j in range(i+1):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
    return maximum


n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

print(search_maximum(matrix, n))