a = int(input("Enter the number: "))  # Input for the number
def table(a):
    i = 1  # Initialize counter
    while i < 11:  # Loop from 1 to 10
        print(a, "x", i, "=", a * i)  # Print the multiplication table
        i += 1  # Increment counter

table(a)  # Call the function to display the multiplication table
