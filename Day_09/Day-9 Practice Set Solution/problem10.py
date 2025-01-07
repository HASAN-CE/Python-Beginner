'''
Write a program to wipe out the content of a file using python
'''
with open('sample.txt','r') as f:
    content =  f.read()
with open('sample.txt','w') as f:
    f.write("")