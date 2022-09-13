# put your python code here
mydict = {}
for _ in range(int(input())):
    temp = input().split()
    for i in range(len(temp)-1):
        mydict[temp[1+i]] = temp[0]
for _ in range(int(input())):
    print(mydict[input()])