# List Methods

l1 = [1, 1651, 1668, 1326, 18641, 511, 316, 615, 9898]  # Example list
friends = ["Apple", "Orange", 5, 345.06, False, None, "Karan"]  # Another example list

# Accessing a slice of the list
print(friends[1:5])  # Output the slice from index 1 to 4

# 1. append
friends.append("Sharma")  # Add "Sharma" to the end of the list
print(friends)

# 2. sort
l1.sort()  # Sort the list in ascending order
print(l1)

# 3. reverse
l1.reverse()  # Reverse the order of the list
print(l1)

# 4. insert
friends.insert(5, "Arman")  # Insert "Arman" at index 5
print(friends)

# 5. pop
friends.pop(1)  # Remove the element at index 1
print(friends)

# 6. remove
l2 = [1, 2, 56, 165, 4916, 16, 98, 64, 918]  # Another example list
l2.remove(56)  # Remove the first occurrence of 56
print(l2)

# 7. index() method returns the index of the element
value = l2.index(98)  # Get the index of the element 98
print(value)
