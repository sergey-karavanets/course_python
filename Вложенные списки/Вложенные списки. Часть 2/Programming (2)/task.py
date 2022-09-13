# put your python code here
def pascal(num):
    l = [[1], [1, 1]]
    for i in range(2, num+1):
        l2 = [1]
        for j in range(2, i+1):
            l2.append(l[i-1][j-2] + l[i-1][j-1])
        l2.append(1)
        l.append(l2)
    return l[n]


n = int(input())

print(pascal(n))