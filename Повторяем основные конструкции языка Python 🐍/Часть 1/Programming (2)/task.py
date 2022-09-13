# put your python code here
def cost_calculation(string):
    cost = len(string) * 60
    rub = cost // 100
    cop = cost % 100
    print(rub, 'р.', cop, 'коп.')


n = input()

cost_calculation(n)