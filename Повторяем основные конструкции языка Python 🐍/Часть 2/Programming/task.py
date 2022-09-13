# put your python code here
def define_quarter(x, y):
    global count_1
    global count_2
    global count_3
    global count_4
    if x > 0 and y > 0:
        count_1 += 1
    elif x < 0 and y > 0:
        count_2 += 1
    elif x < 0 and y < 0:
        count_3 += 1
    elif x > 0 and y < 0:
        count_4 += 1

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    define_quarter(x, y)

print('Первая четверть:', count_1)
print('Вторая четверть:', count_2)
print('Третья четверть:', count_3)
print('Четвертая четверть:', count_4)