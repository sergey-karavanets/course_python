from functools import reduce

def product_of_odds(data):
    result = reduce(lambda a, b: a * b, filter(lambda x: x % 2 == 1, data), 1)
    return result