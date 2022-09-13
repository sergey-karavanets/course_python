# put your python code here
def swap_numbers(list):
    l2 = []
    for i in range(1, (len(list) // 2) + 1):
        l2.append(list[i*2-1])
        l2.append(list[(i*2)-2])
    if len(list) % 2 == 1:
        l2.append(list[-1])
    return l2

def check_num(num):
    if len(num) == 1:
        return num
    else:
        return swap_numbers(num)


l = list(map(int, input().split()))
print(*check_num(l))