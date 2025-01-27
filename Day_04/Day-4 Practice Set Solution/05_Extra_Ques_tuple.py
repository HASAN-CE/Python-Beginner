'Convert a tuple to a list and vice versa.'
#tuple to list:

# Define a tuple
t1 = (1, 23, 45, 78)

# Convert the tuple to a list using the list() function
l1 = list(t1)

# Print the type of l1 to confirm it is now a list
print("Type of l1:", type(l1))  # Output: <class 'list'>
# Print the actual value of l1
print("Value of l1 (List):", l1)  # Output: [1, 23, 45, 78]

# Print the type of t1 to confirm it is still a tuple
print("Type of t1:", type(t1))  # Output: <class 'tuple'>
# Print the actual value of t1
print("Value of t1 (Tuple):", t1)  # Output: (1, 23, 45, 78)

# Define a list
l2 = [235, 8, 498, 1]

# Convert the list to a tuple using the tuple() function
t2 = tuple(l2)

# Print the type of t2 to confirm it is now a tuple
print("Type of t2:", type(t2))  # Output: <class 'tuple'>
# Print the actual value of t2
print("Value of t2 (Tuple):", t2)  # Output: (235, 8, 498, 1)

# Print the type of l2 to confirm it is still a list
print("Type of l2:", type(l2))  # Output: <class 'list'>
# Print the actual value of l2
print("Value of l2 (List):", l2)  # Output: [235, 8, 498, 1]
