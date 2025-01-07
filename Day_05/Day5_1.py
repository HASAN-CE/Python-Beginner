# Dictionary Methods

# Creating a dictionary with various key-value pairs
Dict = {
    "Name": "Python",                             # Key "Name" maps to the value "Python"
    "Age": 33,                                   # Key "Age" maps to the value 33
    "Owner": "Guido van Rossum",                 # Key "Owner" maps to the value "Guido van Rossum"
    "Libraries": ["NumPy", "SciPy", "TensorFlow"], # Key "Libraries" maps to a list of library names
    1991: "Birth_year"                           # Numeric key 1991 maps to the value "Birth_year"
}

# Uncomment to print the entire dictionary
# print(Dict)

# Dictionary Methods

# 1). items()
# Returns a list-like object containing all key-value pairs in the dictionary as tuples
print(Dict.items())

# 2). keys()
# Returns a list-like object containing all keys in the dictionary
print(Dict.keys())

# 3). values()
# Returns a list-like object containing all values in the dictionary
print(Dict.values())

# 4). update()
# Updates the dictionary with the specified key-value pairs
Dict.update({"Name": "Js", "Editor": "Vs Code"})  # Updates the value of "Name" and adds a new key "Editor" with value "Vs Code"
print(Dict)
# Note: If a key already exists (e.g., "Name"), its value will be updated; otherwise, a new key-value pair is added.

# 5). get()
# Safely retrieves the value for a specified key. If the key does not exist, it returns `None` instead of raising an error.
print(Dict.get(1991))  # Fetches the value associated with key 1991 (returns "Birth_year")
print(Dict.get("Name1"))  # Fetches the value for key "Name1", which doesn't exist, so it returns `None`

# Accessing a non-existent key using square brackets raises a KeyError
# The following line will throw an error because "Name1" is not a valid key in the dictionary
# print(Dict["Name1"])  # Uncomment to test the error

# 6). clear()
# Removes all items from the dictionary, leaving it empty
# Example: Uncomment the line below to clear the dictionary
# Dict.clear()

# 7). copy()
# Creates a shallow copy of the dictionary
# Example: Uncomment the line below to create a copy
# new_dict = Dict.copy()

# 8). popitem()
# Removes and returns the last inserted key-value pair from the dictionary
# Example: Uncomment the line below to pop an item
# removed_item = Dict.popitem()
# print(removed_item)
