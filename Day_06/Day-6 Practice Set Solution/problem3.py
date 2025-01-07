# Example strings that are considered spammy
str1 = 'Make a lot of money'
str2 = 'Buy now'
str3 = 'Subscribe this'
str4 = 'Click this'

# Prompt user for a comment
comment = input('Comment: ')

# Check each string explicitly to identify spammy comments
if (str1 == comment):
    print('Spammer!  Don’t try to fool me, I’m not falling for it!')
elif (str2 == comment):
    print('Spammer!  Buy your stuff somewhere else!')
elif (str3 == comment):
    print('Spammer!  Subscribing is a trap!')
elif (str4 == comment):
    print('Spammer!  No clicking on shady links!')
else:
    print('Thanks for Commenting!  Just keep it real next time!')


#2) Second Solution
# Using the 'in' keyword to check if the comment contains any spammy keywords
if (comment in str1 or comment in str2 or comment in str3 or comment in str4):
    print('Spammer')  # If any of the keywords match, label as spammer
else:
    print('Thanks for Commenting')  # If no spammy keywords match, thank the user for commenting