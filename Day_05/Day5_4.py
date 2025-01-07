# Union and Intersection in Sets

# Defining two sets with some overlapping and unique elements
s1 = {1, 46, 89, 100, 120}  # Set `s1` with integer elements
s2 = {46, 99, 1, 778}       # Set `s2` with integer elements

# Union of the sets
# The union operation combines all unique elements from both sets.
print("Union of the Sets: ", s1.union(s2))  # Prints the union of `s1` and `s2`

# Intersection of the sets
# The intersection operation finds elements that are common in both sets.
print("Intersection of the Sets: ", s1.intersection(s2))  # Prints the intersection of `s1` and `s2`
