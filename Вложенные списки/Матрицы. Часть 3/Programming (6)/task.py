# put your python code here
def fill_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            matrix[i][j] = my_list[i+j]
    print_matrix(matrix, n, m)

def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
my_list = []
for _ in range(n):
    for j in range(1, m+1):
        my_list.append(j)

fill_matrix(matrix, n, m)