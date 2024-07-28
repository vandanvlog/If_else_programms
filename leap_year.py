print('Enter your Name')
name = input('=> ')
print('ok ',name,' check leap year ')
year = float(input('Enter your Year = '))

leap_year = year%4

if leap_year == 0:
    print(year," This year is Leap Year")
else:
    print(year,"This year is not Leap Year")
