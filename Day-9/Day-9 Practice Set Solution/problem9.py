'''
Write a program to find out whether a file is identical & matches the content of
another file.
'''

with open('this.txt') as f:
    content = f.readlines()

with open ('this_copy.txt', 'r') as f:
    content1 = f.readlines()

if(content == content1):
    print('Content is same')
else:
    print('Not same')