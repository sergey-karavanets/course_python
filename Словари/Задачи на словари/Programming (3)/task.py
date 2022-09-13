# put your python code here
def search_synonym(mydict, word):
    for key, value in mydict.items():
        if key == word:
            return value
        elif value == word:
            return key


mydict = {}
for _ in range(int(input())):
    temp = input().split()
    mydict[temp[0]] = temp[1]

print(search_synonym(mydict, input()))