# put your python code here
def fill_matrix(matrix, n, m):
    count = 0
    for i in range(n):
        count += 1
        for j in range(m):
            matrix[i][j] = count
            count += n
        count = i+1
    print_matrix(matrix, n, m)

def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

fill_matrix(matrix, n, m)