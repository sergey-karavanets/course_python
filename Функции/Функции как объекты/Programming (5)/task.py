def add_numbers(num):
    return sum(map(int, str(num)))

numbers = [int(i) for i in input().split()]
numbers.sort(key=add_numbers)
print(*numbers)