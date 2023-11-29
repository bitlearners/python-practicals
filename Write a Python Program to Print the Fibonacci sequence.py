#Write a Python Program to Print the Fibonacci sequence

# Developer: Bitlearners


# Function to generate the Fibonacci sequence up to n terms
def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

# Input from the user
terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Check if the input is a positive integer
if terms <= 0:
    print("Please enter a positive integer.")
else:
    # Generate and display the Fibonacci sequence
    result_sequence = fibonacci_sequence(terms)
    print("\nFibonacci Sequence:")
    print(result_sequence)



'''

Explanation:

The program defines a function fibonacci_sequence that generates the Fibonacci sequence up to n terms using a while loop.
The user is prompted to enter the number of terms in the Fibonacci sequence.
The program checks if the input is a positive integer. If it is, it calls the fibonacci_sequence function and prints the resulting sequence. Otherwise, it prompts the user to enter a positive integer.
'''
