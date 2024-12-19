# Type Casting

# Below are a few examples of functions used for typecasting:
# int()
# float()
# str()

a = "312.25"  # 'a' is a string representing a number
at = type(a)  # Check the type of 'a'
print(at)

# Convert 'a' to a float
b = float(a)
print(b)
bt = type(b)  # Check the type after conversion
print(bt)

c = "PYTHON"
# Trying to convert 'c' (a string) to an integer will raise an error because it's not a valid integer string
# sc = int(c)  # This would raise a ValueError

# Correct way to attempt an invalid conversion with error handling:
try:
    sc = int(c)
except ValueError:
    print("Cannot convert a non-numeric string to an integer.")
