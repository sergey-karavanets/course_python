# put your python code here
def pascal(num):
    l = [[1], [1, 1]]
    print(*l[0])
    print(*l[1])
    for i in range(2, num):
        l2 = [1]
        for j in range(2, i+1):
            l2.append(l[i-1][j-2] + l[i-1][j-1])
        l2.append(1)
        l.append(l2)
        print(*l[i])


n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(1)
    print(1, 1)
else:
    pascal(n)