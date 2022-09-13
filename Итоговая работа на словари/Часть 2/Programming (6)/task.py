mydict = {}
for _ in range(int(input())):
    name, product, amount = input().split()
    if name not in mydict:
        mydict[name] = dict()
    if product not in mydict[name]:
        mydict[name][product] = 0
    mydict[name][product] += int(amount)
for names in sorted(mydict):
    print(names + ':')
    for key, value in sorted(mydict[names].items()):
        print(key + ' ' + str(value))