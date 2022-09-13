# put your python code here
my_list = input().split()
set1 = set(my_list[0])
set2 = set(my_list[1])
set3 = set(my_list[2])
if set1 == set2 == set3:
    print('YES')
else:
    print('NO')
