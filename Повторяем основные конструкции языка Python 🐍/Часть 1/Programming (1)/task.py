# put your python code here
def body_mass_index(weight, growth):
    bmi = weight / (growth * growth)
    if bmi < 18.5:
        return print('Недостаточная масса')
    elif 18.5 <= bmi <= 25:
        return print('Оптимальная масса')
    elif bmi > 25:
        return print('Избыточная масса')


weight = float(input())
growth = float(input())

body_mass_index(weight, growth)