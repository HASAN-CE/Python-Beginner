'''
Repeat program 4 for a list of such words to be censored.
'''
words = ['MakeMoneyOnline','LikePlease','Buythis']

with open("file1.txt","r") as f:
    content =  f.read()

for i in words:
    content =  content.replace(i, "*" * len(i))

with open("file1.txt","w") as f:
    f.write(content)
