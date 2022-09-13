import math

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def redical(number):
    return number ** 0.5

def module(number):
    return abs(number)

def sinus(number):
    return math.sin(number)

mydict = {'квадрат': square,
          'куб': cube,
          'корень': redical,
          'модуль': module,
          'синус': sinus}

number = int(input())
func = input()

print(mydict[func](number))