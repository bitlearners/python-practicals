# Input from the user
variable1 = input("Enter the value for variable1: ")
variable2 = input("Enter the value for variable2: ")

print("\nBefore Swapping:")
print("Variable1:", variable1)
print("Variable2:", variable2)

# Swapping the values
variable1, variable2 = variable2, variable1

print("\nAfter Swapping:")
print("Variable1:", variable1)
print("Variable2:", variable2)


'''
Explanation:

The program takes input from the user for the values of two variables (variable1 and variable2).
It then prints the values of the variables before swapping.
The values of the two variables are swapped using a tuple unpacking statement: variable1, variable2 = variable2, variable1.
Finally, the program prints the values of the variables after swapping, demonstrating that the values have been interchanged.
'''
