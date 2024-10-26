# Define a function calculator that takes three parameters: two numbers (a and b) and a choice of operation
def calculator(a, b, choice):
    # If the user chooses to add the numbers
    if choice == 1:
        # Return the sum of a and b
        return a + b
    # If the user chooses to subtract the numbers
    elif choice == 2:
        # Return the difference of a and b
        return a - b
    # If the user chooses to divide the numbers
    elif choice == 3:
        # Return the quotient of a and b
        return a / b
    # If the user chooses to multiply the numbers
    elif choice == 4:
        # Return the product of a and b
        return a * b
    # If the user chooses to exit the calculator
    elif choice == 5:
        # Return a message indicating that the calculator is exiting
        return
    # If the user enters an invalid choice
    else:
        # Return an error message
        return "Invalid choice"

# Print the available operations to the user
print("Choose the operation:")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")
print("5. Exit")

# Create an infinite loop to keep the calculator running until the user chooses to exit
while True:
    # Ask the user to enter their choice of operation
    choice = int(input("Enter your choice: "))
    
    # If the user chooses to exit the calculator
    if choice == 5:
        # Print a message indicating that the calculator is exiting
        print("Exiting the calculator...")
        # Break out of the loop to end the program
        break
    # If the user chooses a valid operation (1-4)
    elif choice in range(1, 5):
        # Ask the user to enter the first number
        a = int(input("Enter the first number: "))
        # Ask the user to enter the second number
        b = int(input("Enter the second number: "))
        # Call the calculator function
        result = calculator(a, b, choice)
        # Print the result of the operation
        print("Result:", result)
    # If the user enters an invalid choice
    else:
        # Print an error message
        print("Invalid choice! Please enter a number between 1 and 5.")


# Input: a number from the user
number = float(input("Enter a number: "))

# Conditional statements 
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# Input a string from the user
user_input = input("Enter a string: ")

# Reversing the string 
reversed_input = ''.join(reversed(user_input))

# Display the reversed string
print("Reversed string:", reversed_input)
