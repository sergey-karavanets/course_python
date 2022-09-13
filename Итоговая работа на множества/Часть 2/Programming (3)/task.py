# put your python code here
m = int(input())  # books in library
n = int(input())  # books in summer-list
my_library = {input() for _ in range(m)}
for _ in range(n):
    if input() in my_library:
        print('YES')
    else:
        print('NO')