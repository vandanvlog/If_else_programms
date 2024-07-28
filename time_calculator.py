def convert_seconds():
    # Prompt user to enter the number of seconds
    seconds = int(input("Enter the number of seconds: "))

    # Calculate the time in different units
    minutes = seconds / 60
    hours = seconds / 3600
    days = seconds / 86400

    # Determine the appropriate time unit to display using nested if statements
    if seconds < 60:
        print(f'You got {seconds} seconds')
    else:
        if seconds < 3600:
            if seconds == 60:
                print('You got 1 minute')
            else:
                print(f'You got {minutes:.0f} minutes')
        else:
            if seconds < 86400:
                if seconds == 3600:
                    print('You got 1 hour')
                else:
                    print(f'You got {hours:.2f} hours')
            else:
                if seconds == 86400:
                    print('You got 1 day')
                else:
                    print(f'You got {days:.2f} days')

# Run the function
def convert_seconds():
    # Prompt user to enter the number of seconds
    seconds = int(input("Enter the number of seconds: "))

    # Calculate the time in different units
    minutes = seconds / 60
    hours = seconds / 3600
    days = seconds / 86400

    # Determine the appropriate time unit to display using nested if statements
    if seconds < 60:
        print(f'You got {seconds} seconds')
    else:
        if seconds < 3600:
            if seconds == 60:
                print('You got 1 minute')
            else:
                print(f'You got {minutes:.0f} minutes')
        else:
            if seconds < 86400:
                if seconds == 3600:
                    print('You got 1 hour')
                else:
                    print(f'You got {hours:.2f} hours')
            else:
                if seconds == 86400:
                    print('You got 1 day')
                else:
                    print(f'You got {days:.2f} days')

# Run the function
convert_seconds()
