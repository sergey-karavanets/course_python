from fractions import Fraction as F
import math

n = int(input())
if n % 2 == 0:
    numerator = n // 2 - 1
    denominator = n - numerator
else:
    numerator = n // 2
    denominator = n - numerator

for i in range(n):
    numerator -= i
    denominator += i
    if numerator == F((str(F(numerator) / F(denominator)).split('/'))[0]):
        print(F(numerator) / F(denominator))
        break