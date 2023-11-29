#Write a Python Program to Convert Kilometers to Miles

# Developer: Bitlearners

# Function to convert kilometers to miles
def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# Input from the user
kilometers = float(input("Enter distance in kilometers: "))

# Check if the input is a non-negative number
if kilometers < 0:
    print("Please enter a non-negative number for distance.")
else:
    # Convert and display the result
    miles_result = kilometers_to_miles(kilometers)
    print("\n{} kilometers is equal to {:.2f} miles.".format(kilometers, miles_result))


'''

Explanation:

The program defines a function kilometers_to_miles that takes a distance in kilometers as input and converts it to miles using the conversion factor (1 kilometer = 0.621371 miles).
The user is prompted to enter a distance in kilometers.
The program checks if the input is a non-negative number. If it is, it calls the kilometers_to_miles function and prints the converted result. Otherwise, it prompts the user to enter a non-negative number.
'''
