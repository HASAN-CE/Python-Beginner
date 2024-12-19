# Dictionary
# Dictionaries are collections of key-value pairs, where each key is unique, and it maps to a specific value.

# Creating a dictionary with key-value pairs
marks = {
    "Rohan": 56,               # Key "Rohan" maps to the value 56
    "Harish": 98,              # Key "Harish" maps to the value 98
    "Lists": [1, 2, 3, 45]     # Key "Lists" maps to a list [1, 2, 3, 45] as its value
}

# Printing the entire dictionary
print(marks)

# Printing the type of the variable 'marks' to confirm it's a dictionary
print(type(marks))

# To create an empty dictionary
e = {}  # Using curly braces to define an empty dictionary
print(type(e))  # Printing the type to confirm it's a dictionary

# Accessing the value associated with a specific key in the dictionary
# Using the key "Lists" to fetch and print its corresponding value (the list [1, 2, 3, 45])
print(marks["Lists"])
