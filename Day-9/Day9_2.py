#Read From the file
file = open("sample1.txt")

# #SOLUTION 1
#readlines() is a inbuilt python function which returns all lines from the file in the form of list
file_lines = file.readlines()
print(file_lines , type(file_lines))

# #SOLUTION 2 
# returns First line from the file
file_read_line1 = file.readline()
print(file_read_line1)

#returns Second line from the file
file_read_line2 = file.readline()
print(file_read_line2)

#returns Third line from the file
file_read_line3 = file.readline()
print(file_read_line3)

#returns Fourth line from the file
file_read_line4 = file.readline()
print(file_read_line4)

#returns Fifth line from the file
file_read_line5 = file.readline()
print(file_read_line5)

#SOLUTION 3
lines = file.readline()
while(lines != ""):
    print(lines)
    lines = file.readline()
file.close()