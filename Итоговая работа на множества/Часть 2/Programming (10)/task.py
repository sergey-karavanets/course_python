# put your python code here
all_lessons = int(input())
all_names = set()
all_names_lesson = set()
for i in range(all_lessons):
    num = int(input())
    for j in range(num):
        temp = input()
        if i == 0:
            all_names.add(temp)
            all_names_lesson.add(temp)
        else:
            all_names_lesson.add(temp)
    all_names.intersection_update(all_names_lesson)
    all_names_lesson = set()
print(*sorted(all_names), sep='\n')