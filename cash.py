count = 0

quarters = 25
dimes = 10
nickels = 5
pennies = 1

while True:
    try:
        dollars = float(input("Change Owed: "))
        if dollars >= 0:
            cents = round(dollars * 100)
            break
        else:
            print("Should be positive")
    except ValueError:
        print("Enter a number")

while cents > 0:
    if cents >= quarters:
        cents = cents - quarters

    elif cents >= dimes:
        cents = cents - dimes

    elif cents >= nickels:
        cents = cents - nickels

    elif cents >= pennies:
        cents = cents - pennies

    count += 1

print(count)
