# Sumation of the first n numbers
n = int(input('Enter the number: '))  # Input the number n

# Initialize variables
i = 0
sum = 0

# Loop to calculate the sum from 0 to n
while(i <= n):
    sum = sum + i  # Add current number to sum
    i = i + 1  # Increment i by 1

print(f"Sum of numbers from 1 to {n} is", sum)  # Output the sum

# Multiplication of the first n numbers
i = 1
mul = 1

# Loop to calculate the multiplication from 1 to n
while(i <= n):
    mul = mul * i  # Multiply current number to mul
    i = i + 1  # Increment i by 1

print(f"Multiplication of numbers from 1 to {n} is", mul)  # Output the multiplication
