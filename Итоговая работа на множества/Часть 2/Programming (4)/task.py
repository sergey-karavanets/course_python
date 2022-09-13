# put your python code here
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}
set3 = set1 & set2
if set3:
    print(*sorted(set3, reverse=True))
else:
    print('BAD DAY')