from random import choice

def generate_password(length):
    uppercase = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    lowercase = 'abcdefghijkmnpqrstuvwxyz'
    digits = '23456789'
    password = ''
    for i in range(length):
        if i % 3 == 0:
            password += choice(uppercase)
        elif i % 3 == 1:
            password += choice(lowercase)
        elif i % 3 == 2:
            password += choice(digits)
    return password

def generate_passwords(count, length):
    data_password = []
    for _ in range(count):
        data_password.append(generate_password(length))
    return data_password


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')