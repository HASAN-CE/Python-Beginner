'Check if a specific element exists in a tuple.'

# Define the tuple with elements
t = (1, 2, 3, 4, 5, 6, 8, 6, 3, 151, 161, 65, 1, 32, 2, 16, 15, 1)

# Prompt the user to input the element to check
user = input('Enter an element to check if it exists in the tuple: ')

# Validate the input to ensure it is a number
if user.isdigit():
    user = int(user)  # Convert the input to an integer
    # Check if the element exists in the tuple
    if user in t:
        print(f'The element {user} exists in the tuple.')
    else:
        print(f'The element {user} does not exist in the tuple.')
else:
    print("Invalid input. Please enter a valid integer.")
