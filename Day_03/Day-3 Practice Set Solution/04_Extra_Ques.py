'Replace all occurrences of a specific word in a string with another word.'

word = 'a'  # Word to replace
r_word = 'the'  # Replacement word

# # Take the input string and split it into words
sample = input('Enter the string: ').split()

# # Initialize an empty list to store the result
a_answer = []

# Iterate through each word in the sample
for i in range(len(sample)):
    if sample[i] == word:  # If the word matches 'a'
        a_answer.append(r_word)  # Replace it with 'the'
    else:
        a_answer.append(sample[i])  # Keep the original word

# # # Join the list back into a string and print the result
print(" ".join(a_answer))

