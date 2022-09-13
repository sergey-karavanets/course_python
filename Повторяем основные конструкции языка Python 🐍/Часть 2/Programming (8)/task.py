# put your python code here
s = input()

if 'Р' not in s:
    print(0)
else:
    count_max = 0
    count = 0
    for i in s:
        if i == 'Р':
            count += 1
            if count_max < count:
                count_max = count
        elif i != 'Р':
            count = 0
    print(count_max)