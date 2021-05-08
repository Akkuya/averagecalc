def averageCalc():
    def average():
        enter = input()  # Enter your numbers
        try:
            # Checks if the input can be converted into a float
            average.floatEnter = float(enter)
        except ValueError:  # If it can't be converted into an float
            print("Not a valid number, please try again.")
            average()  # Call back

    def numbers1():
        numbers = input(
            "Enter how many numbers you wish to find the average of. ")
        try:
            # Checks if the unput can be converted into an integer
            numbers1.intNumbers = int(numbers)
        except ValueError:
            print("Not a valid number, please try again.")
            numbers1()  # Call back

    numbers1()
    sum1 = 0
    for i in range(numbers1.intNumbers):  # Asks for all the  numbers
        print("Please enter number " + str(i + 1))
        average()
        sum1 = sum1+average.floatEnter

    # Calculates the average.
    average = sum1/numbers1.intNumbers

    # Prints the average
    print("The average of all " + str(numbers1.intNumbers) +
          " numbers is " + str(average))


while True:  # Infinite Loop
    averageCalc()
