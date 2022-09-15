from operator import *
def arithmetic_operation(operation):

    def func(x, y):
        result = {'+': add(x, y), '-': sub(x, y), '*': mul(x, y), '/': truediv(x, y)}
        return result[operation]
    return func