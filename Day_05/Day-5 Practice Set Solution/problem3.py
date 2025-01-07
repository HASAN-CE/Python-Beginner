# Creating a set with both string and integer representations of the same value
s1 = {"18", 18}  # The set contains "18" (a string) and 18 (an integer)
print(s1)  # Prints the set. Both "18" and 18 will be present as they are considered different types.

# Yes, we can have 18 as a string and as an integer in a set
# This is because sets treat elements of different types (even with the same apparent value) as unique.
