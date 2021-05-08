
def average():
    enter = input()
    try:
        average.intEnter = int(enter)

    except ValueError:
        print("Not a valid number, please try again")
        average()


numbers = input("Enter how many numbers you wish to find the average of.")

sum1 = 0
for i in range(int(numbers)):
    print("Please enter number " + str(i + 1))
    average()
    sum1 = sum1+average.intEnter

average = sum1/int(numbers)

print("The average of all " + str(numbers) + " numbers is " + str(average))
