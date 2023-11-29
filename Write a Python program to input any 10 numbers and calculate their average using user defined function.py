# Developer: Bitlearners
# Write a Python program to input any 10 numbers and calculate their average using user defined function?
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Input from the user for 10 numbers
numbers = []
for i in range(10):
    number = float(input("Enter number {}: ".format(i + 1)))
    numbers.append(number)

# Calculate and display the average
average_result = calculate_average(numbers)

print("\nAverage of the 10 numbers: {:.2f}".format(average_result))

'''
Explanation:

The program defines a function calculate_average that takes a list of numbers as a parameter, calculates the sum and average of the numbers, and returns the average.
The program then uses a loop to get input from the user for 10 numbers, storing them in a list called numbers.
It calls the calculate_average function with the list of numbers and stores the result in the variable average_result.
Finally, the program prints the average of the 10 numbers.
'''
