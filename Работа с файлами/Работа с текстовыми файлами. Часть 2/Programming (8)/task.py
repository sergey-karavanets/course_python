def read_csv():
    mylist = []
    with open('data.csv', encoding='utf-8') as file:
        content = list(file)
        keys = content.pop(0).strip().split(',')
        for line in content:
            temp_dict = dict(zip(keys, line.strip().split(',')))
            mylist.append(temp_dict)
    return mylist