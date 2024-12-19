#Write in File 

user_input = input('Enter The String To Write In File: ')

file = open('sample1.txt','w')

#write() is a inbuilt python function which is used to write in file
file.write(user_input)

file.close()