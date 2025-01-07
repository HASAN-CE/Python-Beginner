# String Functions

a = '''pYTHON PROGRAM'''
words = ["PYTHON", "PROGRAMMING"]
b = "I AM GOOD AT PROGRAMMING AND MATHS"

# Get the length of the string 'a'
print(len(a))

# Check if 'a' ends with "MING"
print(a.endswith("MING"))

# Check if 'a' starts with "PYTHO"
print(a.startswith("PYTHO"))

# Count occurrences of "A" in 'a'
print(a.count("A"))

# Convert 'a' to title case
print(a.title())

# Capitalize the first character of 'a'
print(a.capitalize())

# Check if all characters in 'a' are alphabetic
print(a.isalpha())

# Check if all characters in 'a' are digits
print(a.isdigit())

# Find the index of the first occurrence of "H" in 'a'
print(a.find("H"))

# Join the list of words with a space
print(" ".join(words))

# Split 'a' at each period
print(a.split("."))

# Remove leading and trailing whitespace from 'a'
print(a.strip())

# Convert 'a' to lowercase
print(a.lower())

# Convert 'a' to uppercase
print(a.upper())

# Replace "GOOD" with "EXCELLENT" in 'b'
print(b.replace("GOOD", "EXCELLENT"))  # It takes all occurrences in the string
