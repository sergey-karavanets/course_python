# put your python code here
def chunked(s, num):
    l = []
    l2 = []
    for i in range(len(s)//num + 1):
        for j in range(num):
            if s:
                l2.append(s.pop(0))
        if l2:
            l.append(l2)
            l2 = []
    return l

string = input().split()
n = int(input())

print(chunked(string, n))