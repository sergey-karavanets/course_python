# put your python code here
mydict = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}
DNK = input()
for letter in DNK:
    print(mydict[letter], end='')