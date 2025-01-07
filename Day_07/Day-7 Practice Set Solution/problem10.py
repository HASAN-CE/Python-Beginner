# Input the number n for which the table is to be printed in reverse order
n = int(input('Enter the number: '))

# Loop to print the table in reverse order from 15 to 1
for i in range(1, 16):
    # Print the multiplication table in reverse order
    print(f'{n} x {16 - i} = {n * (16 - i)}')

'''
1 15
2 14
3 13
4 12
5 11
6 10
7 9
8 8
9 7
10 6
11 5
12 4
13 3
14 2
15 1
'''

# This prints the multiplication table of n from 15 down to 1.
