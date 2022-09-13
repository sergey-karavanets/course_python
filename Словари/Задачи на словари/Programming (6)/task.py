encrypted_word = list(input())
encrypted_dict = {}
for letter in encrypted_word:
    encrypted_dict[letter] = encrypted_dict.get(letter, 0) + 1
mydict = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    mydict[int(value)] = key
for i in range(len(encrypted_word)):
    encrypted_word[i] = encrypted_dict[encrypted_word[i]]
for letter in encrypted_word:
    print(mydict[letter], end='')