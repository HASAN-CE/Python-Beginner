h = (35, "HASAN")  # Creating a tuple with mixed data types

# Trying to change the value of the first element
try:
    h[0] = "JS"  # This will raise an error because tuples are immutable
except TypeError as e:
    print(f"Error: {e}")  # Print the error message
