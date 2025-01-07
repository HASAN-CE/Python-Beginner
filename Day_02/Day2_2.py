# The input() function in Python always returns the user input as a string,
# regardless of whether the entered value appears to be numeric or otherwise.

# Typecast both input values to perform addition.
a = int(input("ENTER NUMBER 1: "))  # Prompt user to enter the first number and convert it to an integer
print(a)

b = int(input("ENTER NUMBER 2: "))  # Prompt user to enter the second number and convert it to an integer
print(b)

# Perform addition of both numbers and print the result
print(a + b)
