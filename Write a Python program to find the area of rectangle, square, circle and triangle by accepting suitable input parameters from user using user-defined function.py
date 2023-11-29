import math

# Function to calculate area of rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate area of square
def square_area(side):
    return side * side

# Function to calculate area of circle
def circle_area(radius):
    return math.pi * (radius ** 2)

# Function to calculate area of triangle
def triangle_area(base, height):
    return 0.5 * base * height

# Input from the user
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
side = float(input("Enter side of the square: "))
radius = float(input("Enter radius of the circle: "))
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))

# Calculate and display areas
rectangle_result = rectangle_area(length, width)
square_result = square_area(side)
circle_result = circle_area(radius)
triangle_result = triangle_area(base, height)

# Displaying the results with appropriate formatting
print("\nAreas:")
print("Rectangle Area: {:.2f}".format(rectangle_result))
print("Square Area: {:.2f}".format(square_result))
print("Circle Area: {:.2f}".format(circle_result))
print("Triangle Area: {:.2f}".format(triangle_result))


"""
Explanation:

1. The program defines four functions (rectangle_area, square_area, circle_area, and triangle_area) to calculate the areas of the respective shapes.
2. The user is prompted to input the required parameters for length and width of the rectangle, side of the square, radius of the circle, base, and height of the triangle.
3. The program then calls the corresponding functions with the user-provided inputs to calculate the areas of the rectangle, square, circle, and triangle.
4. The results are displayed with appropriate formatting, showing the areas of each shape.
"""
