'Write a program to find the frequency of each character in a string.'

# Input string
input_string = "hello world"

# Create an empty dictionary to store the frequency of each character
frequency = {}

# Iterate over each character in the input string
for char in input_string:
    # If the character is already in the dictionary, increment its count
    if char in frequency:
        frequency[char] += 1
    # Otherwise, add the character to the dictionary with a count of 1
    else:
        frequency[char] = 1

# Print the frequency of each character
for char, count in frequency.items():
    print(f"'{char}': {count}")