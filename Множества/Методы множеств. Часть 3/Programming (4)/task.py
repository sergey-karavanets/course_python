# put your python code here
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}
set3 = {int(i) for i in input().split()}

set4 = set1 | set2
set5 = set3 - set4
mylist = sorted(set5, reverse=True)
print(*mylist)