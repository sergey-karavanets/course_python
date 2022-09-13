# put your python code here
def search_maximum(matrix, maximum, n):
    for i in range(n):
        for j in range(n):
            if (i >= j and i >= n - 1 - j) or (i <= j and i >= n - 1 - j):
                if maximum < matrix[i][j]:
                    maximum = matrix[i][j]
    print(maximum)


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
maximum = -9999

search_maximum(matrix, maximum, n)