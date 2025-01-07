import os
with open('sample1.txt','r') as f:
    content = f.read()
with open('rename.txt','w') as f:
    f.write(content)

os.remove('sample1.txt')