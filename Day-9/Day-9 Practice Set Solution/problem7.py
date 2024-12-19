'''
Write a program to find out the line number where python is present from ques 6
'''
word = 'python'
with open("file2.txt") as f:
    content = f.readlines()

linenum = 1
for lines in content:
    if(word in lines):
        print(f'{word} is present at Line No: {linenum}')
        break
    linenum = linenum + 1

else: 
    print('No, Python is not present')


