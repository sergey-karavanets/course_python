# put your python code here
def reverse_num_5(num):
    l = num[:-6:-1]
    remove_zeros(l)

def reverse_num_6(num):
    l = num[:-6:-1]
    l1 = n[0]+l
    remove_zeros(l1)

def remove_zeros(num):
    if num[0] == '0':
        num2 = num[1:]
        remove_zeros(num2)
    else:
        print(num)


n = input()

if len(n) == 5:
    reverse_num_5(n)
elif len(n) == 6:
    reverse_num_6(n)