# put your python code here
mylist = [i for i in input().split()]
mydict = {}
for word in mylist:
    if word not in mydict:
        mydict[word] = mydict.get(word, -1) + 1
        print(word, end=' ')
    else:
        mydict[word] = mydict.get(word, 0) + 1
        print(word + '_' + str(mydict[word]), end=' ')