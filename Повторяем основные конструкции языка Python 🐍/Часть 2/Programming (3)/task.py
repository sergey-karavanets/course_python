# put your python code here
def swap_numbers(num):
    l2 = []
    l2.append(num[-1])
    l2 += num[:-1]
    return l2


l = list(map(int, input().split()))
print(*swap_numbers(l))