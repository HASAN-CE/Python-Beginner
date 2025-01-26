'Write a program to split a list into two lists based on a condition.'
# Input the number of elements the user wants to enter in the list
n = int(input("Enter the number of elements in the list: "))

# Initialize the original list and two separate lists for even and odd numbers
list = []  # This will store the original elements
even_list = []  # This will store even numbers
odd_list = []  # This will store odd numbers

# Loop to input elements into the list
for i in range(n):
    # Append the input element to the original list
    list.append(int(input("Enter the element: ")))

    # Check if the current element is even
    if list[i] % 2 == 0:
        # If the element is even, add it to the even_list
        even_list.append(list[i])
    else:
        # If the element is odd, add it to the odd_list
        odd_list.append(list[i])

# Output the original list and the two new lists (even and odd)
print("The original list is: ", list)  # Display the original list
print('The even list is: ', even_list)  # Display the list of even numbers
print('The odd list is: ', odd_list)  # Display the list of odd numbers
