def merge(values):      # values - это список словарей
    mydict = {}
    for dct in values:
        for key, value in dct.items():
            if key not in mydict:
                mydict[key] = set()
            mydict[key].add(value)
    return mydict