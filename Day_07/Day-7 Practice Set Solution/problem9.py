# Input the number n
n = int(input("Enter the number: "))

# Loop to print the pattern
for i in range(1, n + 1):
    if i == 1 or i == n:
        # First and last rows with asterisks only
        print("*" * n, end="")
    else:
        # Middle rows with spaces in between asterisks
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print("")  # Move to the next line

'''
Output for n=4:
****
*  *
*  *
****
'''
