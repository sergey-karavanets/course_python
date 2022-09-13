# put your python code here
mylist = [word.strip('.,!?:;-') for word in input().lower().split()]
mydict = {}
for word in mylist:
    mydict[word] = mydict.get(word, 0) + 1
all_value = [value for key, value in mydict.items()]
min_value = min(all_value)
all_min_value = [key for key, value in mydict.items() if value == min_value]
print(sorted(all_min_value)[0])