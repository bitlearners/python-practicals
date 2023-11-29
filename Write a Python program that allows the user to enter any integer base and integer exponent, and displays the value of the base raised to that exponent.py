# Write a Python program that allows the user to enter any integer base and integer exponent, and displays the value of the base raised to that exponent.
base = int(input("Enter the base (an integer): "))
exponent = int(input("Enter the exponent (an integer): "))

# Calculate the result using the power operator **
result = base ** exponent

# Display the result
print(f"{base} raised to the power of {exponent} is: {result}")
