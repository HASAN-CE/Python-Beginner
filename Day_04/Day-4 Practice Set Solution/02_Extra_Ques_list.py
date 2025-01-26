'Remove all occurrences of a specific element from a list.'

# Original list containing repeated elements
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ask the user for the element they want to remove from the list
number = int(input('Enter the element you want to remove from the list: '))

# Method 1: Remove all occurrences using a for loop (This method has an issue when modifying the list during iteration)
print("Using for loop to remove elements:")
for i in list[:]:  # Using a copy of the list to avoid skipping elements during iteration
    if i == number:
        list.remove(i)

# Print the list after removal using the for loop method
print("List after removal (for loop method):", list)

# Reset the list to its original state for the next method
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Method 2: Remove all occurrences using a while loop
print("Using while loop to remove elements:")
while number in list:  # Continue removing as long as the number exists in the list
    list.remove(number)

# Print the list after removal using the while loop method
print("List after removal (while loop method):", list)
