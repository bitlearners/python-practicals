# Write a Python program to find the largest number among the three input numbers

# Developer: Bitlearners
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Find the largest number
largest_number = max(number1, number2, number3)

# Display the result
print("The largest number among {}, {}, and {} is: {}".format(number1, number2, number3, largest_number))
