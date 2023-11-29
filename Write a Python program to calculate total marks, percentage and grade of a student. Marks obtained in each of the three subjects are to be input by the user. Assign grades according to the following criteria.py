# Function to calculate total marks, percentage, and grade
def calculate_grade(js, cc, python):
    total_marks = js + cc + python
    percentage = (total_marks / 300) * 100

    # Assigning grades based on percentage
    if percentage >= 80:
        grade = 'A'
    elif 70 <= percentage < 80:
        grade = 'B'
    elif 60 <= percentage < 70:
        grade = 'C'
    elif 40 <= percentage < 60:
        grade = 'D'
    else:
        grade = 'E'

    return total_marks, percentage, grade

# Input from the user
js = float(input("Enter marks for Subject Java Script: "))
cc = float(input("Enter marks for Subject Cloud Computing: "))
python = float(input("Enter marks for Subject Python: "))

# Calculate and display results
total_marks, percentage, grade = calculate_grade(js, cc, python)

print("\nResults:")
print("Total Marks: {:.2f}".format(total_marks))
print("Percentage: {:.2f}%".format(percentage))
print("Grade: {}".format(grade))
