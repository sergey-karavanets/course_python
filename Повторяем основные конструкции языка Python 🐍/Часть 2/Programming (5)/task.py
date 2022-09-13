# put your python code here
def search_number(num):
    if len(num) == 1:
        return 'НЕТ'
    c = num[0]
    for i in range(1, len(num)):
        if c * num[i] == p:
            return 'ДА'
    num2 = num[1:]
    return search_number(num2)


n = int(input())
l = [int(input()) for _ in range(n)]
p = int(input())

print(search_number(l))