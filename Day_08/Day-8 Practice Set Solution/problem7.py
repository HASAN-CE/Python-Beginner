def rem(list1, word="an"):
    n = []  # Initialize an empty list to store filtered items
    for item in list1:
        if not (item == word):  # If the item is not the specified word
            n.append(item.strip(word))  # Remove the specified word from the item and append to the list
    return n  # Return the filtered list
        
list1 = ["Java", "Python"]  # Sample list of words
print(rem(list1))  # Output the filtered list
