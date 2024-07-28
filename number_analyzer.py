number = int(input('Enter you favorite number = '))

odd_number = (number % 2) == 0


if number < 0:
    print('your number is Negative ',number)
    if odd_number:
        print(' your number is odd number ',number)
    else:
        print('your number is even ',number)
elif number > 0:
    print('you  have positive number ',number)
    if odd_number :
        print('your number is odd ',number)
    else:
        print('your number is even',number)
else:
    print('your number is ZEro')