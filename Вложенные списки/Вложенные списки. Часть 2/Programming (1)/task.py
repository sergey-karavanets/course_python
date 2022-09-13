# put your python code here
def print_lists(num):
    l = []
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            l.append(j)
        print(l)
        l = []


n = int(input())

print_lists(n)