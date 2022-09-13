from fractions import Fraction as F

n = int(input())
myset = set()
for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j:
            myset.add(F(i) / F(j))
mylist = list(myset)
print(*sorted(mylist), sep='\n')