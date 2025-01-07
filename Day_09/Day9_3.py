#Different modes of Opening file 
#append 
# 'a' append the string at the end of the file 
str = "Here we go again why to go again and again because we can"
file = open("sample.txt","a")
file.write(str)
file.close()
