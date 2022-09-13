# put your python code here
n = int(input())
myset = set(input())
for _ in range(n-1):
    temp = set(input())
    myset &= temp
mylist = sorted(myset)
print(*mylist)