import random

def generate_ip():
    ip = ''
    for i in range(4):
        ip += (str(random.randint(0, 255)))
        if i != 3:
            ip += '.'
    return ip
