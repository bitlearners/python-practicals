# Write a Python Program to Display the multiplication Table
# Developer: Bitlearners


number = int(input("Enter the number for the multiplication table: "))

# Display the multiplication table
print("\nMultiplication Table for", number)
for i in range(1, 11):
    result = number * i
    print("{} x {} = {}".format(number, i, result))

'''

Explanation:

The program takes input from the user for a number using int(input("Enter the number for the multiplication table: ")).
It then uses a for loop to iterate from 1 to 10 (inclusive) to generate the multiplication table.
In each iteration, it calculates the result of multiplying the input number by the current iteration value and prints the result in a formatted string.
'''
