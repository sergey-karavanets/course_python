# put your python code here
n = int(input())
mydict = {}
for _ in range(n):
    temp = input().split(maxsplit=1)
    mydict[temp[0].strip(':').lower()] = temp[1]
m = int(input())
for i in range(m):
    print(mydict.get(input().lower(), 'Не найдено'))