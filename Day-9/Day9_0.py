#Files I/o in Python

#open() is a built in function in python to open the file, open take two parameter ("Filename","mode")
file = open("sample.txt")
#read() is a built in function in python to read from the file
file_data = file.read()
print(file_data) 
#close() is a built in function in python to close the file (VERY IMP)
file.close()