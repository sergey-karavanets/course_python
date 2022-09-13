# put your python code here
l = list(map(int, input().split()))
count = 0
for i in range(len(l)-1):
    if l[i+1] > l[i]:
        count += 1
print(count)