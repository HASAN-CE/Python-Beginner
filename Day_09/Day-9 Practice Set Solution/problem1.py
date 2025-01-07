'''Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.'''

with open("poems.txt") as file:
    c = file.read()
    if("twinkle" in c):
        print('Yes, twinkle is present in file')
    else:
        print('No, twinkle is not present in file')

