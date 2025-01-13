'Create a program that demonstrates the use of global and local variables.'

# Demonstration of Local Variables in Python

# Define a function to illustrate the use of a local variable
def local_variable_example():
    a = 10  # Local variable 'a' is declared and initialized
    print("Value of 'a' inside the function:", a)  # Accessing the local variable within the function

# Call the function to display the value of the local variable
local_variable_example()

# Attempting to access the local variable 'a' outside the function
# This will raise an error because 'a' is not defined in the global scope
# print(a)  # NameError: name 'a' is not defined


# Demonstration of Global Variables in Python

# Global variable declaration
y = 20  # This variable is declared outside any function, making it accessible globally

# Define a function to demonstrate accessing a global variable
def global_variable_example():
    # Accessing the global variable 'y' inside the function
    print("Value of 'y' inside the function:", y)

# Call the function to display the value of the global variable
global_variable_example()

# The global variable 'y' can also be accessed directly outside the function
print("Value of 'y' outside the function:", y)
