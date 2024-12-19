# Creating a list to store student marks
marks = []  # Initialize an empty list

# Prompting the user to input marks for each student
M1 = int(input("ENTER MARKS FOR 1 STUDENT: "))  # Input marks for the first student
marks.append(M1)  # Add the marks to the list

M2 = int(input("ENTER MARKS FOR 2 STUDENT: "))  # Input marks for the second student
marks.append(M2)  # Add the marks to the list

M3 = int(input("ENTER MARKS FOR 3 STUDENT: "))  # Input marks for the third student
marks.append(M3)  # Add the marks to the list

M4 = int(input("ENTER MARKS FOR 4 STUDENT: "))  # Input marks for the fourth student
marks.append(M4)  # Add the marks to the list

M5 = int(input("ENTER MARKS FOR 5 STUDENT: "))  # Input marks for the fifth student
marks.append(M5)  # Add the marks to the list

M6 = int(input("ENTER MARKS FOR 6 STUDENT: "))  # Input marks for the sixth student
marks.append(M6)  # Add the marks to the list

# Sort the list of marks in ascending order
marks.sort()  # Sort the marks list
print(marks)  # Output the sorted list of marks
