# Set Methods

# Creating a set with various types of elements
s = set()  
s = {"Python", "Js", None, False, 156, 15, "html"}  # A set containing strings, None, a boolean, and integers
print(s, type(s))  # Prints the set and its type

# 1). add()
# Adds a single element to the set. If the element already exists, the set remains unchanged.
s.add(566)  # Adding the integer 566 to the set
print(s, type(s))  # Prints the updated set and its type

# 2). remove()
# Removes the specified element from the set. If the element does not exist, it raises a KeyError.
s.remove(None)  # Removes the element `None` from the set
print(s, type(s))  # Prints the updated set and its type

# Uncommenting the line below will raise an error because "Css" is not in the set
# s.remove("Css")

print(s, type(s))  # The set remains unchanged if the element to remove does not exist

# 3). copy()
# Creates a shallow copy of the set. The copied set is independent of the original set.
s.copy()  # Creates a copy of the set (the copied set is not stored here)
print(s, type(s))  # The original set remains unchanged

# 4). clear()
# Removes all elements from the set, leaving it empty.
s.clear()  # Clears the set
print(s, type(s))  # Prints the empty set and its type

# Printing the length of the set (number of elements in the set)
print(len(s))  # Since the set is now empty, it will print `0`
