with open('ledger.txt', encoding='utf-8') as ledger:
    temp = sum(map(lambda x: int(x[1:]), ledger.readlines()))
    print(f'${temp}')