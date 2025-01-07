# Program to check if a post is about Cyber or not

# Prompt user for the post content
Post = input('Enter the post: ')

#1) First Solution
# Check if the term "Cyber" is in the post (case-insensitive)
if "Cyber".lower() in Post.lower():
    print('Post is about Cyber')  # Post mentions Cyber
else: 
    print('Post is not about Cyber')  # Post does not mention Cyber

#2) Second Solution
# Check if the term "Cyber" in uppercase is in the post (case-insensitive)
if "Cyber".upper() in Post.upper():
    print('Post is about Cyber')  # Post mentions Cyber
else: 
    print('Post is not about Cyber')  # Post does not mention Cyber
