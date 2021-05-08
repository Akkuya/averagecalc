def averageCalc():
    def average():
        enter = input()  # Enter your numbers
        try:
            # Checks if the input can be converted into an float
            average.floatEnter = float(enter)
        except ValueError:  # If it can't be converted into an float
            print("Not a valid number, please try again")
            average()  # Call back

    numbers = input("Enter how many numbers you wish to find the average of.")

    sum1 = 0
    for i in range(int(numbers)):  # Asks for all the  numbers
        print("Please enter number " + str(i + 1))
        average()
        sum1 = sum1+average.floatEnter

    # Calculates the average.
    average = sum1/int(numbers)

    # Prints the average
    print("The average of all " + str(numbers) + " numbers is " + str(average))


while True:  # Infinite Loop
    averageCalc()
