# put your python code here
n = int(input())
k = int(input())

r = 0
for i in range(1, n+1):
    r = (r + k) % i

print(r + 1)