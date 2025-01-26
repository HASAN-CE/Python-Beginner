'Access the 3rd element of a tuple and slice the tuple from index 2 to 5.'

# Input the number of elements the user wants to add to the tuple
n = int(input("Enter the number of elements in the tuple: "))

# Initialize an empty tuple
sample = ()

# Loop to input elements and add them to the tuple
for i in range(n):
    # Take an input from the user, convert it to an integer, and add it to the tuple
    sample += (int(input("Enter the element: ")),)

# Print the 3rd element of the tuple (index 2)
# Tuples are zero-indexed, so sample[2] refers to the 3rd element
print("The 3rd element of the tuple is: ", sample[2])

# Print a slice of the tuple from the 3rd element (index 2) to the 6th element (index 5)
# The slice operation sample[2:6] returns a new tuple containing elements from index 2 to 5
print('The sliced tuple is: ', sample[2:6])
