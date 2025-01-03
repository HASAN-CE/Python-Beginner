#Object Oriented Programming 
#OOP is a paradime of programming 

# Define the Emp class with two class variables
# Define the Emp class with two class variables
class Emp:
    language = 'JavaScript'  # Class attribute shared by all instances
    Salary = 200000          # Class attribute shared by all instances

# Create an instance 'harsh' of the Emp class
harsh = Emp()
harsh.name = 'Harsh'  # 'name' is an instance attribute, unique to 'harsh'
# Print 'name', 'Salary', and 'language' for 'harsh'
print(harsh.name, harsh.Salary, harsh.language)

# Create another instance 'kaviya' of the Emp class
kaviya = Emp()
kaviya.name = 'Kaviya'  # 'name' is an instance attribute, unique to 'kaviya'
# Print 'name', 'Salary', and 'language' for 'kaviya'
print(kaviya.name, kaviya.language, kaviya.Salary)

# Explanation:
# 'name' is an instance attribute, unique to each object
# 'Salary' and 'language' are class attributes, shared by all instances of the class

