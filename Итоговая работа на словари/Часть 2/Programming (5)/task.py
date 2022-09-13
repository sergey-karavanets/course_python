mydict = {}
for _ in range(int(input())):
    temp = input().split()
    for i in range(1, len(temp)):
        if temp[0] not in mydict:
            mydict[temp[0]] = []
        if temp[i] == 'W':
            mydict[temp[0]].append('write')
        elif temp[i] == 'R':
            mydict[temp[0]].append('read')
        elif temp[i] == 'X':
            mydict[temp[0]].append('execute')

for _ in range(int(input())):
    temp2 = input().split()
    if temp2[0] in mydict[temp2[1]]:
        print('OK')
    else:
        print('Access denied')