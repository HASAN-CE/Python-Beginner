'Write a program to extract and print only the digits from a string.'

# Prompt the user to enter a string containing both letters and digits
sample = input("Enter a string with a mixture of both digits and letters: ")

# Display the user-inputted string
print("You entered: ", sample)

# Iterate through each character in the input string
for char in sample:
    # Check if the current character is a digit
    if char.isdigit():
        # Print the digit if found
        print("Digit found:", char)

