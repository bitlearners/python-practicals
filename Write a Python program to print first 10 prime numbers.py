#Write a Python program to print first 10 prime numbers.

# Developer: Bitlearners


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find and print the first 10 prime numbers
count = 0
number = 2

print("First 10 Prime Numbers:")
while count < 10:
    if is_prime(number):
        print(number, end=" ")
        count += 1
    number += 1


'''
Explanation:

The program defines a function is_prime to check if a given number is prime or not.
It uses a while loop to find and print the first 10 prime numbers.
The loop iterates through numbers starting from 2, and for each number, it checks if it is prime using the is_prime function.
If a prime number is found, it is printed, and the count is incremented until 10 prime numbers are printed.


'''
