import random
mylist = []
for i in range(7):
    mylist.append(random.randint(1, 49))
print(*sorted(mylist))