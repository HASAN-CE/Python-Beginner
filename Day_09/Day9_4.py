#with statement
file = open("sample.txt")
print(file.read())
file.close()

#the same code we can write like this with the help of 'with' statement

with open("sample1.txt") as file:
    print(file.read())

#with statement is basically less our burden of closing the file again and again