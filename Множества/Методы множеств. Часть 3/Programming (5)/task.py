# put your python code here
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}
set3 = {int(i) for i in input().split()}
myset = {i for i in range(11)}
set4 = myset - (set1 | set2 | set3)
mylist = sorted(set4)
print(*mylist)