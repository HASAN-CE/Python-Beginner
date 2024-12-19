# List of programming languages
Langname = ['Python', 'Js', 'Css', 'Html', 'Ruby', 'Rust']

# Prompt user for a language name
Guess_name = input('Enter the language name: ')

# Check if the guessed language is present in the list
if (Guess_name in Langname):
    print('Language is present in the list')  # If the language is found, print this message
else:
    print('Language is not present in the list')  # If the language is not found, print this message
