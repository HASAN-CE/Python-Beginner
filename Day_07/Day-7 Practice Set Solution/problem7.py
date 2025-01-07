'''

Example output for n=3

  *
 ***
*****

'''



# Input the number n
n = int(input('Enter the number: '))

# Loop to print the pattern
for i in range(1, n):
    # Print spaces with no new line at the end
    print(" " * (n - i), end="")  # 'end' parameter avoids a new line after printing spaces
    # Print stars with no new line at the end
    print("*" * (2 * i - 1), end="")
    print("")  # Move to the next line

