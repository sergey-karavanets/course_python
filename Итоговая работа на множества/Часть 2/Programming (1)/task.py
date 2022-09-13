# put your python code here
mylist = [int(i) for i in input().split()]
myset = set(mylist)
print(len(mylist) - len(myset))