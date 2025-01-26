'Flatten a nested list in Python.'

# Define a nested list
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11, 12]]

# Initialize an empty list to store the flattened elements
new_list = []

# Outer loop to iterate over each sub-list in the nested list
for i in list:
    # Inner loop to iterate over each element in the current sub-list
    for j in i:
        # Append each element to the new_list
        new_list.append(j)

# Print the flattened list
print(new_list)
