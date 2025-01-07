# Elif Example

# Input: A number
a = int(input('Enter the Number: '))

# If-elif-else ladder to determine the type of number
if (a == 0):  # Check if the number is zero
    print('Enter number is Zero')  # Print if the number is zero
elif (a < 0):  # Check if the number is negative
    print('Enter number is Negative')  # Print if the number is negative
elif (a % 2 == 0):  # Check if the number is even
    print('Enter number is Even')  # Print if the number is even
else:  # If none of the above, the number must be odd
    print('Enter number is Odd')  # Print if the number is odd

print('End of Elif Example')  # Indicate the end of the elif example
