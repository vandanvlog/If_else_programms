# this program shows nasted if statements
# in this program if users salary is >= 30,000$ or expirenace is > 2 years then he will get the loan other wise
# he will not get any loan

min_salary = 30000
years_of_expi = 2

name = input("Enter your name = ")
salary = int(input(f" {name} What is your anual salary = "))
years_of_work = int(input(" how many years of experience do you have = "))

if salary >= min_salary :
    if years_of_work > years_of_expi :
        print(" you will have the loan soon")
    else:
        print(' you are not eligible for the loan')

else:
    print(" you are not eligible for the loan so you need to work hard for that you anual salary must bne "
      "more then ", min_salary," and you should have hands on ",years_of_expi,"then you will get the loan ")


print('; this is the same program using and operator')

your_name = input("Enter your Name ")
your_salary = int(input("Enter your salary  = "))
your_expi = int(input("how many years have you been working "))

if your_salary <= min_salary or your_expi <= years_of_expi :
    print("your are eligible fo the loan")
else:
    print('you are npt eligible for this loan ')