# put your python code here
def matrix_separation(my_list, matrix, n):
    for i in range(n):
        temp = [my_list[j] for j in range(i, len(my_list), n)]
        matrix.append(temp)
    print(matrix)


my_list = list(map(str, input().split()))
n = int(input())
matrix = []

matrix_separation(my_list, matrix, n)