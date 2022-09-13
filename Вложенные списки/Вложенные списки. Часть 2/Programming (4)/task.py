# put your python code here
def duplicates(string):
    l = []
    l2 = []
    for i in range(len(string)):
        if not l2:
            l2.append(string[i])
            if i+1 == len(string):
                l.append(l2)
        else:
            if l2[0] == string[i]:
                l2.append(string[i])
                if i + 1 == len(string):
                    l.append(l2)
            elif l2[0] != string[i]:
                l.append(l2)
                l2 = []
                l2.append(string[i])
                if i + 1 == len(string):
                    l.append(l2)
    return l


n = input().split()

print(duplicates(n))