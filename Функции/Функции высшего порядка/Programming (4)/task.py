def func_apply(func, items):
    result = []
    for item in items:
        temp = func(item)
        result.append(temp)
    return result