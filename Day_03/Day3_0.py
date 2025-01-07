# String 
# Strings in Python are immutable
a = "PYTHON"
b = '''PYTHON'''
c = 'PYTHON'

# Get the length of the string 'a'
name = len(a)  # len(var_name) gives the length of the string
print(name)

# Extract characters from index 0 to 1 (excluding index 2)
name_short = a[0:2]
print(name_short)

# Extract the fourth character from the end of the string 'c'
short_form = c[-4]  # Output 'T'
print(short_form)

# Extract the second character from the string 'b'
short_form = b[1]  # Output 'Y'
print(short_form)

# Additional string manipulations
ex = '''DECIMALL'''
print(ex[:-1])  # Print all characters except the last one
print(ex[0:])   # Print the entire string

# Skipping values
d = '''abcdefghijklmnopqrstuvwxyz'''
print(d[2:12])  # Extract characters from index 2 to 11
print(d[2:12:2])  # Start from index 2, go till index 11, and skip every second index
