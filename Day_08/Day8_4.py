# Recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1  # Base case: If the number is 0 or 1, return 1
    return num * factorial(num - 1)  # Recursive case: Calculate factorial by multiplying the number with the factorial of (num - 1)

num = int(input("Enter the number: "))  # Input the number for which the factorial needs to be calculated
value = factorial(num)  # Call the factorial function
print(f'Factorial of {num} is {factorial(num)}')  # Output the factorial of the given number
