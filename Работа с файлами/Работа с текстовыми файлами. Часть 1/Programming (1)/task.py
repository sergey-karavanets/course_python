temp_file = open(input(), encoding='utf-8')
content = temp_file.readlines()
temp_file.close()
print(content[-2])