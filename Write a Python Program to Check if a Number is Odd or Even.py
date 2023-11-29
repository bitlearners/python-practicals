# Developer: Bitlearners

# Write a Python Program to Check if a Number is Odd or Even
number = int(input("Enter a number: "))

# Check if the number is odd or even
if number % 2 == 0:
    print("The entered number is even.")
else:
    print("The entered number is odd.")


'''

Explanation:
# Developer: Bitlearners
The program takes input from the user for a number using int(input("Enter a number: ")).
It uses the modulo operator % to check if the number is divisible by 2.
If the remainder is 0, it means the number is even, and the program prints "The entered number is even."
If the remainder is not 0, it means the number is odd, and the program prints "The entered number is odd."
'''
