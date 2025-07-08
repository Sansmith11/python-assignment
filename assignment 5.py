# Task 1: Create a Dictionary of Student Marks

# Step 1: Create a dictionary with student names and their marks
student_marks = {
    "Sandeep": 85,
    "Ankit": 78,
    "Himanshu": 92,
    "Annu": 88,
    "karan": 76
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display the marks, or show an error if not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")


# Task 2: Demonstrate List Slicing

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements using slicing
first_five = numbers[:5]

# Step 3: Reverse the extracted list
reversed_five = first_five[::-1]

# Step 4: Print both the extracted list and the reversed list
print("Original list:", numbers)
print("First five elements:", first_five)
print("Reversed first five elements:", reversed_five)
