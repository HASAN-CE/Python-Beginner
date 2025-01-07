# print 'Python' 10 times using while loop
a = 0
while (a < 10):
    print('Python')  # Print 'Python'
    a += 1  # Increment the counter

print('Exiting...')  # Print message when exiting the loop

# write the content of the list using while loop

list = [1, 45, 65, 'Python', 'Js', 'Go', 'Shell', True, None, 1235, 65]

print('Printing list with len method\n')
l = 0
while (l < len(list)):  # Loop through the list
    print(list[l])  # Print each element in the list
    l += 1  # Move to the next element

print('\nPrinting without len method...')
# Without using len method
for i in list:  # Iterate over each item in the list
    print(i)  # Print the item
