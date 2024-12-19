# For loop with if-else ladder

l = [2, 4, 6, 8, 10, 12, 14, 18, 16, 20, 16, 198561, 23530356, 5165, 165]  # Define a list
for i in l:  # Iterate over each element in the list
    if (i % 2 == 0):  # Check if the number is even
        print(i)  # Print the even number
else:
    print('Odd Numbers are skipped')  # If no even numbers are found, print this message
