# Dictionary Example

# Creating a dictionary with Hindi words as keys and their English meanings as values
Dict = {
    "Pyar": "Love",       
    "Dukh": "Sorrow",      
    "Sach": "Truth",       
    "Dosti": "Friendship"  
}

# Taking user input to search for a Hindi word in the dictionary
Word = input("Write a Word In Hindi: ")  # Prompts the user to enter a Hindi word
print(Dict[Word])  # Prints the English meaning of the entered word
