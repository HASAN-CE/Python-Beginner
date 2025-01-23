'Sort a list of tuples by the second element of each tuple' 

# Define a list of tuples
tuples_list = [(1, 3), (4, 1), (2, 5), (7, 2)]

# Sort the list of tuples based on the second element of each tuple
# The lambda function specifies that sorting should consider x[1] (second element of the tuple)
sorted_list = sorted(tuples_list, key=lambda x: x[1])

# Print the original list (unchanged)
print("Original List:", tuples_list)

# Print the sorted list (ordered by the second element)
print("Sorted List:", sorted_list)

