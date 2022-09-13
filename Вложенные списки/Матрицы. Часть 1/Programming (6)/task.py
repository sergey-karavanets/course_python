# put your python code here
def upper_quarter(matrix, n):
    total = 0
    for i in range(n):
        for j in range(n):
            if i < j and i < n-1-j:
                total += matrix[i][j]
    return total

def right_quarter(matrix, n):
    total = 0
    for i in range(n):
        for j in range(n):
            if i < j and i > n-1-j:
                total += matrix[i][j]
    return total

def down_quarter(matrix, n):
    total = 0
    for i in range(n):
        for j in range(n):
            if i > j and i > n - 1 - j:
                total += matrix[i][j]
    return total

def left_quarter(matrix, n):
    total = 0
    for i in range(n):
        for j in range(n):
            if i > j and i < n - 1 - j:
                total += matrix[i][j]
    return total

n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

print('Верхняя четверть:', upper_quarter(matrix, n))
print('Правая четверть:', right_quarter(matrix, n))
print('Нижняя четверть:', down_quarter(matrix, n))
print('Левая четверть:', left_quarter(matrix, n))

