# put your python code here
mydict = {}
n = input().lower()
for i in n:
    if i not in '.,!?:;-' and i.isalpha():
        mydict[i] = mydict.get(i, 0) + 1
n2 = input().lower()
for j in n2:
    if j not in '.,!?:;-' and j.isalpha():
        mydict[j] = mydict.get(j, 0) - 1
#print(mydict.items())
if -1 in mydict.values():
    print('NO')
else:
    print('YES')