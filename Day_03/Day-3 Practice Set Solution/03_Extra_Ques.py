'Write a Python function to reverse a given string.'

# Prompt the user to enter a string
s = input('Enter a string to reverse: ')

# Function to reverse the input string
def reverse_string(s):
    # Return the reversed string using slicing
    return s[::-1]

# Call the function and store the result in 'answer'
answer = reverse_string(s)

# Print the reversed string with a descriptive message
print(f"The reversed string is: {answer}")
