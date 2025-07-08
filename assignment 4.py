# Task 1: Read a File and Handle Errors

try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        print("File content:\n")
        # Read and print each line
        for line in file:
            print(line.strip())
except FileNotFoundError:
    # Handle the case when the file does not exist
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")


# Task 2: Write and Append Data to a File

# Step 1: Take user input and write it to output.txt
user_input = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data written to output.txt.")

# Step 2: Append additional data
append_input = input("Enter additional text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(append_input + "\n")

print("Additional data appended to output.txt.")

# Step 3: Read and display the final content
print("\nFinal content of output.txt:\n")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
