# put your python code here
n = int(input())
mylist = ''
for _ in range(n):
    temp = input().lower()
    mylist += temp
myset = set(mylist)
print(len(myset))