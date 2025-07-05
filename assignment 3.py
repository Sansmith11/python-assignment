# Task 1: Calculate Factorial Using a Function

# Define a function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    print(f"The factorial of {num} is: {fact}")


# Task 2: Using the Math Module for Calculations

import math

# Ask the user for a number
num = float(input("Enter a positive number: "))

if num <= 0:
    print("Please enter a positive number for valid calculations.")
else:
    # Calculate using math module
    square_root = math.sqrt(num)
    natural_log = math.log(num)        # log base e
    sine_value = math.sin(num)         # input is in radians

    # Display the results
    print("\nResults:")
    print(f"Square root of {num}: {square_root}")
    print(f"Natural logarithm of {num}: {natural_log}")
    print(f"Sine of {num} radians: {sine_value}")
