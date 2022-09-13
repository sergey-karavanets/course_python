# put your python code here
mydict = {}
for _ in range(int(input())):
    number, name = input().lower().split()
    if name not in mydict:
        mydict[name] = list()
    mydict[name].append(number)
for _ in range(int(input())):
    print(*mydict.get(input().lower(), ['абонент не найден']))