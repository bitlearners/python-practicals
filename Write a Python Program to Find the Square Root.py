#Write a Python Program to Find the Square Root

# Developer: Bitlearners



import math

# Input from the user
number = float(input("Enter a number: "))

# Check if the input is a non-negative number
if number < 0:
    print("Please enter a non-negative number.")
else:
    # Calculate and display the square root
    square_root_result = math.sqrt(number)
    print("\nThe square root of {} is: {:.2f}".format(number, square_root_result))




'''

Explanation:

The program uses the math module, which provides mathematical functions, including the sqrt() function for calculating the square root.
The user is prompted to enter a number.
The program checks if the input is a non-negative number. If it is, it calls the sqrt() function from the math module and prints the calculated square root. Otherwise, it prompts the user to enter a non-negative number.




'''
