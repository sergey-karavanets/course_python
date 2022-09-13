# put your python code here
def fill_matrix(matrix, my_list, n, m):
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                matrix[i][j] = my_list[(i * m) + j]
            if i % 2 != 0:
                matrix[i][j] = my_list[(int(len(my_list) / n)) * (i + 1) - 1 - j]
    print_matrix(matrix, my_list, n, m)

def print_matrix(matrix, my_list, n, m):
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


n, m = [int(i) for i in input().split()]
my_list = [i for i in range(1, (n * m) + 1)]
matrix = [[0]*m for _ in range(n)]

fill_matrix(matrix, my_list, n, m)