'''
Write a program to mine a log file and find out whether it contains ‘python’
'''
word = 'python'
with open("file2.txt","r") as f:
    content = f.read()

if (word in content):
    print(f'{word} is present')
else:
    print(f'{word} is not present')
