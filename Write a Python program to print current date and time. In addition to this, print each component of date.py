"""
Write a Python program to print current date and time. In addition to this, print each component of date
"""

# Developer: Bitlearners


import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Extract components of date and time
current_date = current_datetime.date()
current_time = current_datetime.time()

# Display the results
print("Current Date and Time:", current_datetime)
print("\nDate Components:")
print("Year: {}".format(current_date.year))
print("Month: {}".format(current_date.month))
print("Day: {}".format(current_date.day))

print("\nTime Components:")
print("Hours: {}".format(current_time.hour))
print("Minutes: {}".format(current_time.minute))
print("Microseconds: {}".format(current_time.microsecond))


'''
Explanation:

The program uses the datetime module to get the current date and time.
It then extracts the date and time components using the date() and time() methods.
Finally, it prints the current date and time, along with each component of the date (year, month, day) and time (hours, minutes, microseconds) separately.
'''
