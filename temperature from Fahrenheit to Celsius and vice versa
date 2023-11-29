#Write a Python program to convert the given temperature from Fahrenheit to Celsius and vice versa depending upon users choice.
while True:
    # Display the options for the user.
    print("Choose an option:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Quit")

    # Get the user's choice as input.
    choice = input("Enter your choice (1, 2, or 3): ")

    # Check the user's choice and perform the corresponding action.
    if choice == '1':
        # If the user chooses option 1, convert Fahrenheit to Celsius.
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        # The conversion formula: Celsius = (Fahrenheit - 32) * 5/9
        celsius = (fahrenheit - 32) * 5/9
        # Display the result.
        print(f"{fahrenheit} Fahrenheit is {celsius:.2f} Celsius\n")
    elif choice == '2':
        # If the user chooses option 2, convert Celsius to Fahrenheit.
        celsius = float(input("Enter temperature in Celsius: "))
        # The conversion formula: Fahrenheit = (Celsius * 9/5) + 32
        fahrenheit = (celsius * 9/5) + 32
        # Display the result.
        print(f"{celsius} Celsius is {fahrenheit:.2f} Fahrenheit\n")
    elif choice == '3':
        # If the user chooses option 3, exit the program.
        print("Exiting the program. Goodbye!")
        break  # Exit the loop.
    else:
        # If the user enters an invalid choice, notify and ask again.
        print("Invalid choice. Please enter 1, 2, or 3.\n")

# The program ends when the user chooses to quit.
