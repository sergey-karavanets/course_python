from fractions import Fraction as F

n = int(input())
result = 0
for i in range(1, n+1):
    result += F(1) / F(i**2)
print(result)