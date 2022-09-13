# put your python code here
mylist = input().split()
mydict = {}
for word in mylist:
    mydict[word] = mydict.get(word, 0) + 1
    print(mydict[word], end=' ')