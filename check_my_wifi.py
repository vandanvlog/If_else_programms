print("Wel-Come let's fix your wifi\n")
print("Reboot the Computer and try to connect to the wifi again")


def question_1():
    return input("Did that fix your problem? Yes or no: ").strip().lower()


def suggestion_2():
    print("Make sure the cable between the router & modem is plugged in firmly")


def suggestion_3():
    print("Move your router to a new location and try to connect")


def suggestion_4():
    print("Get a new router")


def main():
    response = question_1()

    if response == "yes":
        print("Enjoy your Internet")
    elif response == "no":
        suggestion_2()
        response = question_1()

        if response == "yes":
            print("Enjoy your Internet")
        elif response == "no":
            suggestion_3()
            response = question_1()

            if response == "yes":
                print("Enjoy your Internet")
            elif response == "no":
                suggestion_4()
                response = question_1()

                if response == "yes":
                    print("Enjoy your Internet")
                else:
                    print("Get a new router")
    else:
        print("Please enter 'yes' or 'no'.")


main()
