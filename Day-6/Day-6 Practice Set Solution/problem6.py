# Program to assign grades based on student marks

# Prompt user for marks
student_marks = int(input('Enter your marks: '))

# Determine the grade based on the marks
if (90 <= student_marks < 100):
    print('Grade: Ex')  # Excellent
elif (80 <= student_marks < 90):
    print('Grade: A')  # Very Good
elif (70 <= student_marks < 80):
    print('Grade: B')  # Good
elif (60 <= student_marks < 70):
    print('Grade: C')  # Average
elif (50 <= student_marks < 60):
    print('Grade: D')  # Below Average
else:
    print('Grade: F')  # Fail
