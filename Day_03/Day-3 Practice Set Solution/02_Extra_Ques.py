'Count the number of vowels in a string using Python.'

# Define the vowels (both uppercase and lowercase)
vowels = 'aeiouAEIOU'

# Prompt the user to input a string
sample = input('Enter the string: ')

# Initialize the vowel counter
count = 0

# Iterate through each character in the input string
for i in range(len(sample)):
    if sample[i] in vowels:  # Check if the character is a vowel
        count += 1  # Increment the counter if a vowel is found

# Display the total count of vowels in the string
print(f"The string contains {count} vowels.")


