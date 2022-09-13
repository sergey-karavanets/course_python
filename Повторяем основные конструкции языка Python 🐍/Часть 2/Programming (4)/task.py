# put your python code here
def counting_digits(num):
    global count
    for i in range(len(num)-1):
        c = num[i]
        if c < num[i+1]:
            count += 1
            c = num[i]
    return count


l = list(map(int, input().split()))
count = 1

print(counting_digits(l))