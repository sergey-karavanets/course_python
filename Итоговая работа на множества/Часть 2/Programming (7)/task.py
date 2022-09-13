# put your python code here
math = int(input())
info = int(input())
set_math = {input() for _ in range(math)}
set_info = {input() for _ in range(info)}
set_total = set_math | set_info
set_only_one = set_math ^ set_info
if set_only_one:
    print(len(set_only_one))
else:
    print('NO')

