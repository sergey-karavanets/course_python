# put your python code here
n = int(input())
myset = set()
for _ in range(n):
    myset.add(input())
new_sity = input()
if new_sity in myset:
    print('REPEAT')
else:
    print('OK')