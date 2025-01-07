# Sets
# A set is a collection of unique elements. It is unordered, meaning the elements have no specific order.
# For creating an empty set, do not use e = {} as it will create an empty dictionary instead.

# Correct way to create an empty set
s = set()  # Creates an empty set
print(type(s))  # Prints the type to confirm it's a set

# Set Example
# In a set, if an element is repeated, it will only be stored once (duplicates are not allowed).

s1 = set()  # Creates an empty set
s1 = {1, 2, 4, 8, 10, 12, 14, 16, 18, 20}  # Assigning a set with unique integer elements
print(s1)  # Prints the set
print(type(s1))  # Prints the type to confirm it's a set

# Another example of a set
s2 = set()  # Creates an empty set
s2 = {1, 2, 4, 8, 10, 12, 14, 16, 18, 20, 161, 11, 165, 252, 252, 1, 2, 4, 8, 10, 12, 14, 16}
# Note: Duplicate elements like 1, 2, 4, etc., will be ignored, and they will only appear once in the set.
print(s2)  # Prints the set, which will only include unique elements
print(type(s2))  # Prints the type to confirm it's a set
