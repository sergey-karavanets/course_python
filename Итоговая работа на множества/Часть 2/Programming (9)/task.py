# put your python code here
math = int(input())
info = int(input())
all_students = set()
for _ in range(math + info):
    temp = input()
    if temp not in all_students:
        all_students.add(temp)
    else:
        all_students.discard(temp)
if all_students:
    print(len(all_students))
else:
    print('NO')
