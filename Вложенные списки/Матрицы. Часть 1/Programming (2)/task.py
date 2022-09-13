# put your python code here
def matrix_trace(matrix, n):
    total = 0
    for i in range(n):
        total += matrix[i][i]
    return total


n = int(input())
matrix = []

for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

print(matrix_trace(matrix, n))