# Task 1: Perform Basic Mathematical Operations

# Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Print the results
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")


# Task 2: Create a Personalized Greeting

# Step 1: Take first and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Step 2: Concatenate into full name
full_name = first_name + " " + last_name

# Step 3: Print personalized greeting
print(f"\nHello, {full_name}! Welcome to the Python programming world.")
