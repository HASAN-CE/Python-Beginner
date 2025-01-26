'Write a Python program to find the second largest number in a list.'

# Get the number of elements the user wants to enter in the list
n = int(input('Enter the number of elements you want to enter in the list: '))

# Initialize an empty list to store the elements
sample = []

# Loop to get each element from the user
for i in range(n):
    # Append the entered element to the list and sort it
    sample.append(int(input('Enter Element: ')))
    sample.sort()  # Keeps the list sorted at every iteration

# Print the second largest element from the sorted list
print('Second Largest Element is: ', sample[-2])
