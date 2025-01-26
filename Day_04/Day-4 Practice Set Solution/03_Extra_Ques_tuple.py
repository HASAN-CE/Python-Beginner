'Write a Python program to find the index of an item in a tuple.'
# Define a tuple with multiple integer values
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# Prompt the user to input the item they want to find the index of
# Convert the input to an integer since the tuple contains integers
item = int(input("Enter the item to find the index of: "))

# Check if the item exists in the tuple
if item in my_tuple:
    # If the item is found, get its index using the index() method
    index = my_tuple.index(item)
    # Display the index to the user
    print(f"The index of {item} is: {index}")
else:
    # If the item is not found in the tuple, inform the user
    print(f"{item} not found in the tuple.")

    