'''
For n = 3
***
**
*
'''

n = int(input('Enter the number: '))  # Input for the number of lines

def pattern(n):
    if n == 0:
        return  # Base case: If n is 0, do nothing
    print("*" * n)  # Print `*` n times
    pattern(n - 1)  # Recursive call with n-1

pattern(n)  # Call the function to print the pattern
