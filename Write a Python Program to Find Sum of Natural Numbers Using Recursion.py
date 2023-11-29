#Write a Python Program to Find Sum of Natural Numbers Using Recursion

# Developer: Bitlearners

# Function to find the sum of natural numbers using recursion
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)

# Input from the user
number = int(input("Enter a positive integer: "))

# Check if the input is a positive integer
if number < 0:
    print("Please enter a positive integer.")
else:
    # Calculate and display the sum
    result = sum_of_natural_numbers(number)
    print("Sum of the first {} natural numbers is: {}".format(number, result))


'''
Explanation:

The program defines a function sum_of_natural_numbers that takes an integer n as input and calculates the sum of the first n natural numbers using recursion.
The user is prompted to enter a positive integer.
The program checks if the input is a positive integer. If it is, it calls the sum_of_natural_numbers function and prints the result. Otherwise, it prompts the user to enter a positive integer.

'''
