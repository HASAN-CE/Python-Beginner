'''
Write a program that:
Accepts a dictionary with student names as keys and their scores as values.
Computes the average score of the class.
Outputs the names of students who scored above average.
'''
# Initialize an empty dictionary to store student names and scores
dict1 = {}

# Ask the user for the number of student records to store
number_of_student = int(input("Enter the number of records you want to store: "))

# Loop to input each student's name and score
for i in range(number_of_student):
    name1 =  input('Enter Your Name: ')  # Input student's name
    score = int(input('Enter Your Score: '))  # Input student's score
    dict1[name1] = score  # Store the name and score in the dictionary

# Get all the student scores from the dictionary
Average_Of_Each_Student = dict1.values()

# Calculate the total score of the class and divide by the number of students to find the average
Total_of_Class = sum(Average_Of_Each_Student) / number_of_student

# Print the average score of the class
print("Average of Class", Total_of_Class)

# Set a fixed average score value for comparison
average = 33

# Loop through the dictionary and print the names and scores of students who scored above the fixed average
for i in dict1:
    if dict1[i] >= average:  # If the student's score is greater than or equal to 33
        print(i, dict1[i])  # Print the student's name and score
