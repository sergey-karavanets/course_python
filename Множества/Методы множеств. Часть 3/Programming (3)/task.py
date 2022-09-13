# put your python code here
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}
set3 = {int(i) for i in input().split()}

set4 = set1 & set2
set5 = set2 & set3
set6 = set1 & set3
set7 = set4 & set5 & set6
set8 = (set1 | set2 | set3) - set7
mylist = sorted(set8)
print(*mylist)