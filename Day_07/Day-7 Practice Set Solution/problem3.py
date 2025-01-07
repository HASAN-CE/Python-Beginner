# Print the multiplication table using a while loop

# Input: Number for which the table is to be printed
a = int(input("Enter the number: "))

# Initialize counter for the table
i = 1
while i < 11:  # Loop from 1 to 10
    print(a, "x", i, "=", a * i)  # Print the multiplication for each value of i
    i += 1  # Increment the counter
