# put your python code here
def add_commas(num):
    if num >= 1000:
        l = list(str(num))
        count = 0
        for i in range(1, ((len(l) - 1) // 3) + 1):
            l.insert(-3 * i - count, ',')
            count += 1
        print(*l, sep='')
    else:
        print(num)


n = int(input())

add_commas(n)

