n1 = int(input('Enter the first number: '))  # Input for the first number
n2 = int(input('Enter the second number: '))  # Input for the second number
n3 = int(input('Enter the third number: '))  # Input for the third number

def greatest(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1  # If the first number is greater
    elif n2 > n1 and n2 > n3:
        return n2  # If the second number is greater
    else:
        return n3  # If the third number is greater or equal

print('The Greatest of all 3 numbers is:', greatest(n1, n2, n3))  # Output the greatest number
