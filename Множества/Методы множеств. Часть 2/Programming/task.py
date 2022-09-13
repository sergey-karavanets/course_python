# put your python code here
n = {int(i) for i in input().split()}
m = {int(i) for i in input().split()}
total = n & m
print(len(total))