print('Enter your Name')
name = input('=> ')
print('ok ', name, ' check your BMI but '
                   'for that you enter some value ')

print('Do you want to enter your weight in pounds or in kilograms? Please enter "pound" or "kg": ')
way = input()

if way == 'pound':
    print('Enter your weight in pounds:')
    weight_P = float(input())
    print('Enter your height in inches:')
    height_e = float(input())
    BMI = (weight_P / (height_e * height_e)) * 703
    print('Your BMI is:', BMI)
elif way == 'kg':
    print('Enter your weight in kilograms:')
    weight_kg = float(input())
    print('Enter your height in meters:')
    height_m = float(input())
    BMI = weight_kg / (height_m * height_m)
    print('Your BMI is:', BMI)
else:
    print('Invalid input. Please enter "pound" or "kg" for weight.')

if 18.5 <= BMI <= 25:
    print('Your body is in the healthy BMI range.')
else:
    print('Your BMI is outside the healthy range. Please consult with a healthcare professional.')


# print("HI vandan let's go to temple ")
# print('Vandan has a "Rolls Roys" in his garage')
# print("""I'm reading a book called "Rich dad poor Dad" which is nice book """)
# print('''I'm reading a book called "Rich dad poor Dad" which is nice book ''')
#
# weight = 100
# print(weight )
# name =  input('what is your name : -')
# print(name ,'is your name ')

# age = int(input('Enter your age = '))
#
# match age:
#
#     case x if x>18 :
#         print('your are a man')
#     case x if x<18 :
#         print(('your are a teen'))
#     case _:
#         print(age)