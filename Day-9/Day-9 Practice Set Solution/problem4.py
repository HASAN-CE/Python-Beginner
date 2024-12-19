'''A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file.'''

with open("file.txt","r") as f:
    content = f.read()

NewContent = content.replace("Donkeys","#######")


with open("file.txt","w") as f:
    content = f.write(NewContent)


 