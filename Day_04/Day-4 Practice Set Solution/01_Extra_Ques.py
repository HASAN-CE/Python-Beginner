'Write a program to find the largest and smallest elements in a list'

# Take input for the size of the list
n = int(input("Enter the size of the list: "))

# Initialize an empty list
numbers = []

# Taking user input to populate the list
for i in range(n):
    numbers.append(int(input(f"Enter element {i+1}: ")))

# Initialize largest and smallest with the first element of the list
largest = numbers[0]
smallest = numbers[0]

# Iterate through the list to find the largest and smallest elements
for num in numbers:
    if num > largest:
        largest = num  # Update largest if a bigger number is found

    if num < smallest:
        smallest = num  # Update smallest if a smaller number is found

# Display the results
print(f"Largest Element in the list: {largest}")
print(f"Smallest Element in the list: {smallest}")
        


