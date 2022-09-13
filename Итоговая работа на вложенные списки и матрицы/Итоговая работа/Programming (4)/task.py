# put your python code here
def symmetry_check(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n-1-j][n-1-i] and i != n - j:
                return 'NO'
    return 'YES'


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

print(symmetry_check(matrix, n))