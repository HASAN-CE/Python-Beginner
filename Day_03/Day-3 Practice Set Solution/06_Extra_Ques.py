'Convert a string to uppercase and count the number of uppercase letters.'

# Prompt the user to enter a string
example = input("Enter a string: ")

# Initialize a counter to track the number of uppercase letters
count = 0

# Iterate through each character in the string using its index
for i in range(len(example)):
    # Check if the current character is an uppercase letter
    if example[i].isupper():
        count += 1  # Increment the counter if the character is uppercase

# Display the total count of uppercase letters in the string
print("Number of uppercase letters in the string:", count)