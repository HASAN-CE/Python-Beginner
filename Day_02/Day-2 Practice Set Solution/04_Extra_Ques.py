'Write a Python program to check the type of a variable using the `type()` function.'

# Prompt the user to input a number and convert it to an integer
# Note: This will raise a ValueError if the input is not a valid integer
a = int(input('Enter a number to determine its type: '))

# Display the type of the variable 'a' using the built-in `type()` function
print(f"The type of the variable is: {type(a)}")