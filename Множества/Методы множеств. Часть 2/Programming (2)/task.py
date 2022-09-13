# put your python code here
n = {int(i) for i in input().split()}
m = {int(i) for i in input().split()}
s = n.difference(m)
s = sorted(s)
print(*s)