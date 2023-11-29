#Write a Python program to calculate the subtraction of two compatible matrices?
# Developer: Bitlearners
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Function to subtract two matrices
def subtract_matrices(matrix1, matrix2):
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result_matrix.append(row)
    return result_matrix

# Input matrices from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("\nEnter Matrix 1:")
matrix1 = [[float(input("Enter element at position ({},{}): ".format(i+1, j+1))) for j in range(cols)] for i in range(rows)]

print("\nEnter Matrix 2:")
matrix2 = [[float(input("Enter element at position ({},{}): ".format(i+1, j+1))) for j in range(cols)] for i in range(rows)]

# Check if matrices are compatible for subtraction
if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
    # Subtract matrices
    result_matrix = subtract_matrices(matrix1, matrix2)
    
    # Display the result
    print("\nResultant Matrix (Matrix1 - Matrix2):")
    for row in result_matrix:
        print(row)
else:
    print("\nMatrices are not compatible for subtraction.")


'''
Explanation:

The program defines a function subtract_matrices that takes two matrices as input and returns their subtraction.
It then takes input from the user for the dimensions of the matrices and their elements.
The program checks if the matrices are compatible for subtraction (i.e., they have the same number of rows and columns).
If the matrices are compatible, it calls the subtract_matrices function and displays the result. Otherwise, it notifies the user that the matrices are not compatible for subtraction.


'''
