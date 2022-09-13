from random import choice

def generate_password(length):
    chair = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    password = ''
    for i in range(length):
        password += choice(chair)
    return password

def generate_passwords(count, length):
    data_password = []
    for _ in range(count):
        data_password.append(generate_password(length))
    return data_password


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')