from random import choice

names = [input() for _ in range(int(input()))]
friends = names.copy()
mydict = {}
for i in range(len(names)):
    mydict[names[i]] = ''
    random_friend = choice(friends)
    if random_friend != names[i]:
        mydict[names[i]] += (random_friend)
        friends.remove(random_friend)
    else:
        while random_friend == names[i]:
            random_friend = choice(friends)
        mydict[names[i]] += (random_friend)
        friends.remove(random_friend)

for key, value in mydict.items():
    print(key, '-', value)