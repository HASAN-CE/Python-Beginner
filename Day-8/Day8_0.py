# This code snippet demonstrates the use of functions to avoid code repetition.

# Directly taking inputs and performing an addition
n1 = int(input('Enter First Number: '))  # Input for the first number
n2 = int(input('Enter Second Number: ')) # Input for the second number
n3 = int(input('Enter Third Number: '))  # Input for the third number

total = n1 + n2 + n3  # Sum of the three numbers
print(total)  # Displaying the total

# To declare a function, use the 'def' keyword.
# Function definition
def add_number():
    # Inside the function, taking inputs and performing an addition
    n1 = int(input('Enter First Number: '))  # Input for the first number
    n2 = int(input('Enter Second Number: ')) # Input for the second number
    n3 = int(input('Enter Third Number: '))  # Input for the third number

    total = n1 + n2 + n3  # Sum of the three numbers
    print("Total of the above numbers: ", total)  # Displaying the total

# Function call
add_number()  # Calling the function to execute the code inside
