# Tuples Methods

a = (38, "MANAV", 18, True, None, 58, 98, 56, 85, 58, 25, 35, 58, "SHAH", "BROTHER")  # Example tuple
print(a)

# count() method 
No = a.count(58)  # Count occurrences of 58 in the tuple
print(No)  # Output: Number of times 58 appears in the tuple
print(a)  # Output the original tuple

# index() method
In = a.index(58)  # Find the first index of 58 in the tuple
print(In)  # Output: Index of the first occurrence of 58

# len() method
print(len(a))  # Output the length of the tuple

# Concatenation of a list of tuples
# As tuples are immutable, it creates a whole new tuple and does not change the existing one
tup_1 = ("PYTHON", "JS", "RUBY", "SHELL", "RUST")  # First tuple
tup_2 = (1, 2, 3, 4)  # Second tuple
res = tup_1 + tup_2  # Concatenate tup_1 and tup_2
print(res)  # Output: Combined tuple

# Different Tuple Methods
# min() - Returns the smallest value in the tuple
# max() - Returns the largest value in the tuple
# sum() - Returns the sum of all the numerical values in the tuple
# any() - Returns True if any element in the tuple is true; otherwise, it returns False
