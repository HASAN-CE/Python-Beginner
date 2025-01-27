'Write a program to count the number of occurrences of an element in a tuple'
# Define the tuple
t = (1, 2, 3, 4, 5, 6, 1, 2, 34, 5, 34, 156, 12, 5651, 15, 3, 4)

# Loop through each element in the tuple
for i in t:
    # Print the current element and the number of times it is repeated in the tuple
    # t.count(i) returns the count of the element i in the tuple
    print(f"{i} is repeated: ", t.count(i))
