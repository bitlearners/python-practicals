#Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal

# Developer: Bitlearners


#----------------------------------------------------------------------------------------------------------------------------

# Function to check if a string is palindrome
def is_palindrome(string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(string.split()).lower()
    reversed_string = cleaned_string[::-1]
    return cleaned_string == reversed_string

# Input from the user
user_input = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(user_input):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")


'''
Explanation:

The program defines a function is_palindrome that takes a string as input, removes spaces, and converts it to lowercase for case-insensitive comparison. It then checks if the cleaned string is equal to its reverse.
The user is prompted to input a string.
The program calls the is_palindrome function and prints whether the entered string is a palindrome or not based on the function's result.

'''
