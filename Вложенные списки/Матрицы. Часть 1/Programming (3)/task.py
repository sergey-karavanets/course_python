# put your python code here
def display_numbers(matrix, n):
    average = 0
    total = 0
    for i in range(n):
        average = sum(matrix[i]) / len(matrix[i])
        for j in range(n):
            if matrix[i][j] > average:
                total += 1
        print(total)
        total = 0


n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

display_numbers(matrix, n)