# put your python code here
n = int(input())
students = [[i for i in input().split()] for _ in range(n)]
for student in students:
    print(*student)
print()
for i in range(len(students)):
    if students[i][1] == '4' or students[i][1] == '5':
        print(*students[i])