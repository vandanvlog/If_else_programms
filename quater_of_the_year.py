month = int(input('enter your birth month = '))

if month >= 1 and month <= 3 :
    print('you are in the first quarter')
elif month >= 4 and month <= 6 :
    print('you are in the second quarter')
elif month >= 7 and month <9 :
    print(' your are in the third quarter ')
elif month >= 10 and month <= 12 :
    print(' your in the four quarter ')
else:
    print('enter correct month ')
