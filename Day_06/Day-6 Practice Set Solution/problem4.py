# Prompt user for a username
user_name = input('Enter the username: ')
print(user_name)

# Check the length of the username
if (len(user_name) > 10):
    print('Valid username')  # If username length is greater than 10, it is valid
elif (len(user_name) < 10):
    print('Invalid username')  # If username length is less than 10, it is invalid
