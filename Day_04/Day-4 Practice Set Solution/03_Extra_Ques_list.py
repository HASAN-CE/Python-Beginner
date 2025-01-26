'Write a Python program to reverse a list without using the reverse() method'
# Prompt the user to enter the size of the list
n = int(input('Enter the size of the list: '))

# Initialize an empty list to store user input
user_list = []

# Ask the user to input each element to populate the list
for i in range(n):
    element = int(input(f'Enter element {i+1}: '))  # Prompting for each element with index
    user_list.append(element)

# Display the original list entered by the user
print("Original List:", user_list)

# Initialize an empty list to store the reversed list
rev_list = []

# Reverse the original list by slicing, then append each element to the new list
for i in range(len(user_list)):
    # Create a reversed copy of the list using slicing [::-1]
    reverse = user_list[::-1]  
    rev_list.append(reverse[i])

# Display the reversed list
print("Reversed List:", rev_list)

