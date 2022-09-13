# put your python code here
math = int(input())
info = int(input())
set_math = {input() for _ in range(math)}
set_info = {input() for _ in range(info)}
print(len(set_math - set_info))