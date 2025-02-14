# Prompt the user for input
number = int(input("enter a number to calculate its factorial: "))

# Initialize the factorial to 1
factorial = 1

# Check if the number is negative, zero, or positive
if number < 0:
    print("Factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else: 
    # Use a loop to calculate the factorial
    for i in range(1, number + 1):
        factorial *= i

    # Print the result
    print(f"The factorial of {number} is {factorial}")