# put your python code here
set1 = {name for name in input().split()}
set2 = {name for name in input().split()}
print(*sorted(set1 | set2))