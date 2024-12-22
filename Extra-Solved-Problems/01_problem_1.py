'''
Write a Python program that reads a text file and counts the number of occurrences of each word in the file. The programshould output the words and their counts in a dictionary.
'''

# List of words to search for in the file content
words = ['python', 'js', 'html', 'css', 'cyber', 'java']

# Open the file 'file.txt' in read mode and store its content
with open('file.txt') as f:
    content = f.read()  # Read the content of the file into the variable 'content'

# Initialize an empty dictionary to store word counts
dict1 = {}

# Iterate through each word in the list 'words'
for word in words:
    # Count occurrences of each word in the content (case-insensitive)
    count = content.lower().split().count(word)  # Convert content to lowercase and split into words, then count occurrences of the word
    if count > 0:  # Only add to dictionary if the word occurs at least once in the content
        dict1[word] = count  # Store the word and its count in the dictionary

# Iterate through the dictionary and print each word with its count
for word, count in dict1.items():
    print(f'{word}: {count}')  # Print the word and its corresponding count

