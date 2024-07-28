name = input(' Entre your name = ')

print(f'{name}, here we are going to calculate magical date so pls enter any date. ')
print(' and the formate should be inn the manner mm/dd/yy')

month = int(input('Enter the month = '))
day = int(input('Enter the day = '))
year = int(input('Enter the year but last two digit = '))

magic_date =  month * day

if  magic_date == year :
    print(f'this is the magic date {month}/{day}/{year}')
else:
    print('this is not the magic date, give me anther date ')