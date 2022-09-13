def build_query_string(params):
    temp = sorted(params.keys())
    mylist = [key + '=' + str(params[key]) for key in temp]
    return '&'.join(mylist)
