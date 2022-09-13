# put your python code here
def fill_matrix(matrix, n, m):
    count = 1
    for i in range(n):
        for j in range(m):
            matrix[i][j] = count
            count += 1
    print_matrix(matrix, n, m)

def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


my_list = list(map(int, input().split()))
n = my_list[0]
m = my_list[1]
matrix = []
for _ in range(n):
    temp = [0]*m
    matrix.append(temp)

fill_matrix(matrix, n, m)