print('Enter your Name')
name = input('=> ')
print('ok ', name, ' check your BMI but '
                   'for that you enter some value ')

print('you want to enter your wait in pound or in kg, so give answer in only in pound or kg ')
way = str(input())

if way == 'pound':
    print('enter your waite in pound')
    weight_P = float(input())
    print('enter your height in inches')
    height_e = float(input())
    BMI = 705 * (weight_P) / height_e * height_e
    print('your bmi is BMI is == ', BMI)
elif way == 'kg':
    print('enter your weight in KG')
    weight_kg = float(input())
    print('enter your height in meter ')
    height_m = float(input())
    BMI = weight_kg / height_m * height_m
    print('your BMI is == ', BMI)
