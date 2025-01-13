'Write a program to swap two variables without using a third variable.'

# Input: Prompt the user to enter two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swap the values using arithmetic operations
# Step 1: Add both numbers and store the result in 'a'
a = a + b

# Step 2: Subtract the new value of 'a' by 'b' to get the original value of 'a' into 'b'
b = a - b

# Step 3: Subtract the new value of 'b' from 'a' to get the original value of 'b' into 'a'
a = a - b

# Output: Print the swapped values
print("After swapping, the values of a and b are:", a, b)