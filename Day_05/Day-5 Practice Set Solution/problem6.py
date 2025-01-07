# Creating an empty dictionary to store friends' names and their favorite programming languages
friends = {}

# Taking input for the first friend's name and their favorite language
name = input("Enter the friend's Name: ")  # Prompt for the friend's name
lang = input("Enter the language: ")  # Prompt for the friend's favorite language
friends.update({name: lang})  # Adding the friend's name and language to the dictionary

# Taking input for the second friend's name and their favorite language
name = input("Enter the friend's Name: ")  # Prompt for the friend's name
lang = input("Enter the language: ")  # Prompt for the friend's favorite language
friends.update({name: lang})  # Adding the friend's name and language to the dictionary

# Taking input for the third friend's name and their favorite language
name = input("Enter the friend's Name: ")  # Prompt for the friend's name
lang = input("Enter the language: ")  # Prompt for the friend's favorite language
friends.update({name: lang})  # Adding the friend's name and language to the dictionary

# Taking input for the fourth friend's name and their favorite language
name = input("Enter the friend's Name: ")  # Prompt for the friend's name
lang = input("Enter the language: ")  # Prompt for the friend's favorite language
friends.update({name: lang})  # Adding the friend's name and language to the dictionary

# Printing the length of the dictionary (number of key-value pairs)
print("Length Of The Dictionary is: ", len(friends))  # Prints the number of entries in the dictionary

# Printing the dictionary containing friends' names and their favorite languages
print(friends)  # Displays the dictionary
