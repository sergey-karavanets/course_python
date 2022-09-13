# put your python code here
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}
set3 = {int(i) for i in input().split()}

set1.intersection_update(set2)
set1.difference_update(set3)
print(*sorted(set1, reverse=True))