# put your python code here
def print_matrix(mult, n, m):
    for i in range(n):
        for j in range(m):
            print(str(mult[i][j]).ljust(3), end='')
        print()


n, m = int(input()), int(input())
mult = []
for i in range(n):
    temp = [j*i for j in range(m)]
    mult.append(temp)

print_matrix(mult, n, m)