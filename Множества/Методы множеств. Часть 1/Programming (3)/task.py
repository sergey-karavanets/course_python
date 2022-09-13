# put your python code here
def check_list(n):
    myset = set()
    for i in range(len(n)):
        if n[i] in myset:
            print('YES')
        else:
            print('NO')
            myset.add(n[i])


n = [int(i) for i in input().split()]
check_list(n)