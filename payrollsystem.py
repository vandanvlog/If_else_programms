# if the employee works more then 40 hours then pay them 1.5 times more hourly

name = input("Enter your Name = ")

hours = int(input(f"{name}, how many hours did you work this week? "))
print(f"You worked {hours} hours this week .")



if hours <= 40 :
    regular_pay = hours * 11.44
    print(f"so {name}, your pay for this week is ",regular_pay,"you will get by bank transfer")
else:
    extra_pay = hours * 1.5 * 11.44
    print(f"so {name}, your pay  with extra hours is ",extra_pay,"you will get by bank transfer ")