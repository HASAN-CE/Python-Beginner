'''
Write a Python program that reads a text file and counts the number of occurrences of each word in the file. The programshould output the words and their counts in a dictionary.
'''

words = ['python', 'js', 'html', 'css', 'cyber', 'java']
with open('file.txt') as f:
    content = f.read()

dict1 = {}

# Iterate through each word in the list 'words'
for word in words:
    count = content.lower().split().count(word)  # Count occurrences of each word in the content
    if count > 0:  # Only print the word if it occurs at least once
        dict1[word] = count

# Print the word counts
for word, count in dict1.items():
    print(f'{word}: {count}')
