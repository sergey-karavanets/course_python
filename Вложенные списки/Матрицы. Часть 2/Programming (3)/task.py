# put your python code here
def symmetry_check(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[j][i] != matrix[i][j] and i != j:
                return 'NO'
    return 'YES'


n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

print(symmetry_check(matrix, n))