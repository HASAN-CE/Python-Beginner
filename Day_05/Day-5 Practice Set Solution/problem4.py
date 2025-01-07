# Creating an empty set
s = set()

# Adding elements to the set
s.add(20)      # Adding the integer 20 to the set
s.add(20.0)    # Adding the float 20.0 to the set (Python treats 20 and 20.0 as the same value)
s.add("20")    # Adding the string "20" to the set (this is different from the integer and float)

# Printing the length of the set
print("Length of the set is: ", len(s))  # The length will be 2 because 20 and 20.0 are considered the same

# Printing the set
print(s)  # The set will contain 20 (or 20.0) and "20" as unique elements

# Python checks only the value of numeric elements, not their datatype
if (1 == '1'):  # Comparing an integer `1` with a string `'1'`
    print("True")
else:
    print("False")  # This will execute, as Python considers 1 (integer) and '1' (string) to be different

# From this, we can interpret that in Python sets, 1 and 1.0 are treated as the same element
# This is because Python considers their values equal even though their datatypes differ.
