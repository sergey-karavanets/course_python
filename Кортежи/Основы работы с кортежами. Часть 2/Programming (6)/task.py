# put your python code here
n = int(input())
a, b, c = 1, 1, 1
for i in range(n):
    print(a, end=' ')
    a, b, c = b, c, a + b + c