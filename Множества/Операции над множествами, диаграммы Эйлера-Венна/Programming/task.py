# put your python code here
n, m , k, x, y, z = (int(input()) for i in range(6))
total = (n-x) + x + (m-x-y) + y + (k-y) + z
print(total)