'''
Sum (1) = 1

Sum (2) = 1+2 = 3

Sum (3) = 1+2+3 = 6

Sum (4) = 1+2+3+4 = 10

Sum (5) = 1+2+3+4+5 = 15
'''

def sum_n(n):
    if n == 1:
        return 1  # Base case: if n is 1, return 1
    return sum_n(n-1) + n  # Recursive case: sum the previous number with the current

print(sum_n(4))  # Output the sum of first 4 natural numbers
