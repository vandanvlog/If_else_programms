
name = input("Enter your name = ")

print("Wel come to the Dashboard",name ," Enter your Marks of 3 tests ",name)

test_1 = int(input("Enter your test 1 mark = "))
test_2 = int(input("Enter your test 2 mark = "))
test_3 = int(input("Enter your test 3 mark = "))

avg = (test_1 + test_2 + test_3)*100/300

if avg > 95 :
    print("your Result is = ",avg)
    print(" you are a brilliant student ",name,"keep it up ")
else:
    print("your Result is = ",avg)
    print("you need more hard work ", name)