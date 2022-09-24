with open('logfile.txt', encoding='utf-8') as logfile, open('output.txt', 'w', encoding='utf-8') as output:
    temp = []
    for log in logfile:
        temp.append(log.strip().split(', '))
    for name, start, stop in temp:
        if (int(stop.split(':')[0]) * 60 + int(stop.split(':')[1])) - (int(start.split(':')[0]) * 60 + int(start.split(':')[1])) >= 60:
            print(name, file=output)