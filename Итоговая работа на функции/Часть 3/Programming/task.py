def concat(*args, sep=' '):
    result = sep.join(map(str, args))
    return result