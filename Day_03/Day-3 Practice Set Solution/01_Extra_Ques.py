'Write a program to check if a given string is a palindrome.'

# Prompt the user to input a string
sample_s = input('Enter a string: ')

# Convert the string to lowercase to make the palindrome check case-insensitive
sample = sample_s.lower()

# Reverse the string using slicing
r_str = sample[::-1]  # [start:end:step] with step=-1 reverses the string

# Print the reversed string (for reference)
print(f"Reversed string: {r_str}")

# Check if the original (lowercased) string matches the reversed string
if sample == r_str:
    print(f"'{sample_s}' is a palindrome string")  # Use original string for better user feedback
else:
    print(f"'{sample_s}' is not a palindrome string")
