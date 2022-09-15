file = open('nums.txt', encoding='utf-8')
content = [i.strip() for i in list(file)]
print(sum(map(int, filter(lambda x: x != '', content))))