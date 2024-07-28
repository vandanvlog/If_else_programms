age = int(input('Enter your age = '))

match age:

    case x if x>18 :
        print('your are a man')
    case x if x<18 :
        print(('your are a teen'))
    case _:
        print(age)