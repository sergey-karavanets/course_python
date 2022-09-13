from fractions import Fraction as F
import math

n = int(input())
result = 0
for i in range(1, n+1):
    result += F(1) / F(math.factorial(i))
print(result)