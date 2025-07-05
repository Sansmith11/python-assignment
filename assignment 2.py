# Task 1: Check if a Number is Even or Odd

# Take integer input from the user
num = int(input("Enter an integer: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

 
 # Task 2: Sum of Integers from 1 to 50 Using a Loop

# Initialize the sum variable
total_sum = 0

# Use a for loop to iterate from 1 to 50
for num in range(1, 51):
    total_sum += num

# Display the final sum
print("The sum of integers from 1 to 50 is:", total_sum)
