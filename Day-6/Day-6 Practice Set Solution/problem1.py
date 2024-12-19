# Input: Four numbers
a = int(input("Enter First Number: "))  # Input for the first number
b = int(input("Enter Second Number: ")) # Input for the second number
c = int(input("Enter Third Number: "))  # Input for the third number
d = int(input("Enter Fourth Number: ")) # Input for the fourth number

# Here, the difference between 'or' & 'and' (Logical Operators) is that:
# - 'or' will execute the `if-elif` statement even if the first condition matches in the statement.
# - 'and' will only execute the `if-elif` statement when all conditions match in the `if-elif` statement.

# Example with 'and' operator
if (a > b and a > c and a > d):  # Check if `a` is the greatest among the numbers
    print(f'{a} is Greatest')  # Print if `a` is the greatest
elif (b > a and b > c and b > d):  # Check if `b` is the greatest among the numbers
    print(f'{b} is Greatest')  # Print if `b` is the greatest
elif (c > a and c > b and c > d):  # Check if `c` is the greatest among the numbers
    print(f'{c} is Greatest')  # Print if `c` is the greatest
elif (d > a and d > b and d > c):  # Check if `d` is the greatest among the numbers
    print(f'{d} is Greatest')  # Print if `d` is the greatest

# Example with 'or' operator
if (a > b or a > c or a > d):  # Check if `a` is the greatest among the numbers using 'or' operator
    print(f'{a} is Greatest')  # Print if `a` is the greatest
elif (b > a or b > c or b > d):  # Check if `b` is the greatest among the numbers using 'or' operator
    print(f'{b} is Greatest')  # Print if `b` is the greatest
elif (c > a or c > b or c > d):  # Check if `c` is the greatest among the numbers using 'or' operator
    print(f'{c} is Greatest')  # Print if `c` is the greatest
elif (d > a or d > b or d > c):  # Check if `d` is the greatest among the numbers using 'or' operator
    print(f'{d} is Greatest')  # Print if `d` is the greatest
