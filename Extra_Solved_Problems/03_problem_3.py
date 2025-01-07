'''
Student Performance Tracker
Problem Statement:
Write a program to manage student data and analyze their performance.
- Use a file to store student data (name, marks in 3 subjects).
- Read the data from the file into a dictionary where the key is the student's name and the value is a tuple of their marks.
- Calculate and display the average marks for each student using a loop.
- Identify students scoring above 75% and write their names to a new file.
- Allow the user to add new student data using input and update the file accordingly.
'''
# Input the strength of the class
n = int(input("Enter the strength of the class: "))

# Loop to collect student details and write them to a file
for i in range(n):
    with open('Student_info.txt', 'a') as f:  # Open the file in append mode to add new student details
        name = input('Enter the student name: ')  # Input student name
        mark1 = int(input('Enter the marks for the first subject: '))  # Input marks for subject 1
        mark2 = int(input('Enter the marks for the second subject: '))  # Input marks for subject 2
        mark3 = int(input('Enter the marks for the third subject: '))  # Input marks for subject 3
        
        # Format the student data and add a blank line at the end for separation
        data = f'STUDENT NAME: {name}\nSUBJECT1 :{mark1}\nSUBJECT2 :{mark2}\nSUBJECT3 :{mark3}\n\n'
        f.write(data)  # Write the formatted data to the file

# Initialize an empty dictionary to store student data
students_dict = {}

# Open the file in read mode to process its content
with open('Student_info.txt', 'r') as f:
    content = f.read().strip().split('\n\n')  # Split the data into blocks for each student

# Loop through each block of student data to extract details
for block in content:
    lines = block.split('\n')  # Split each block into individual lines
    name_line = lines[0].split(': ')[1]  # Extract the student's name from the first line
    mark1 = int(lines[1].split(':')[1])  # Extract marks for the first subject
    mark2 = int(lines[2].split(':')[1])  # Extract marks for the second subject
    mark3 = int(lines[3].split(':')[1])  # Extract marks for the third subject
    
    # Add the student's name and their marks as a tuple to the dictionary
    students_dict[name_line] = (mark1, mark2, mark3)

# Display the dictionary of student data
print(students_dict)

# Calculate and display the average marks for each student
for student in students_dict:
    avg_marks = sum(students_dict[student]) / 3  # Calculate the average of the marks
    print(f"Average marks for {student}: {avg_marks}")  # Print the average marks
