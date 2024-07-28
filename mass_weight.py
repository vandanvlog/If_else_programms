name = input(' Enter your Name =  ')

object_mass = float(input(f'{name},Enter your Objective Mass = '))

weight = object_mass * 9.8

if weight <= 100:
    print(f'{name}, your weight is too light, and that is {weight:.2f} N')
elif weight >= 500:
    print(f'{name}, your weight is too heavy, and that is {weight:.2f} N')
else:
    print(f'{name}, your weight is balanced, and that is {weight:.2f} N')

