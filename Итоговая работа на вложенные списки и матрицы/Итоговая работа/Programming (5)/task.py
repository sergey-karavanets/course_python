# put your python code here
def matrix_check(matrix, n, summa):
    temp = 0
    for i in range(n):
        for j in range(n):
            temp += matrix[i][j]
        if temp != summa:
            return 'NO'
        temp = 0
        for k in range(n):
            temp += matrix[k][i]
        if temp != summa:
            return 'NO'
        temp = 0
    return 'YES'



n = int(input())
summa = sum([j for j in range(1, n+1)])
matrix = [[int(i) for i in input().split()] for _ in range(n)]

print(matrix_check(matrix, n, summa))