# put your python code here
n = {int(i) for i in input().split()}
m = {int(i) for i in input().split()}
s = n.intersection(m)
s = sorted(s)
print(*s)