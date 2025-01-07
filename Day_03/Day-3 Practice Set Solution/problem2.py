# Solution 1:
a = input("ENTER YOUR NAME: ")  # Prompt user to enter their name
b = input("ENTER THE DATE: ")  # Prompt user to enter the date
letter = f"Dear,\n {a}, You are selected\n On {b}"  # Format the letter using an 'f' string
print(letter)

# Solution 2:
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''  # Multiline string template with placeholders

# Replace the placeholders with actual values
print(letter.replace("<|Name|>", "ROHAN").replace("<|Date|>", "12-5-25"))  # Perform a chaining of `string.replace`
