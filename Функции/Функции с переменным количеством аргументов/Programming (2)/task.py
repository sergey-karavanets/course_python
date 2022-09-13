def mean(*args):
    summa = 0
    count = 0
    for arg in args:
        if type(arg) in (int, float):
            summa += arg
            count += 1
    if count == 0:
        return 0
    else:
        return (summa / count)