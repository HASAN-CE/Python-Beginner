# Input the number n
n = int(input('Enter the number: '))

# Initialize the multiplication result
mul = 1

# Loop to calculate the factorial of n
for i in range(1, n + 1):
    mul = mul * i  # Multiply current i to mul

# Output the factorial of the number
print(f"Factorial of {n} is", mul)
