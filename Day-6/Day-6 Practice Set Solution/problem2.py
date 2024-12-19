# Input: Marks of three subjects
sub1 = int(input("Enter marks of 1 subject: "))  # Input for the first subject's marks
sub2 = int(input("Enter marks of 2 subject: "))  # Input for the second subject's marks
sub3 = int(input("Enter marks of 3 subject: "))  # Input for the third subject's marks

# Calculate total marks
total = sub1 + sub2 + sub3

# Calculate percentage
percentage = (total / 300) * 100
total_percentage = float(percentage)  # Convert percentage to float for precision

print('Your percentage is: ', total_percentage)

# Determine if the student has passed based on the criteria:
# - Overall percentage must be greater than 40%
# - Each subject must have at least 33 marks
if (percentage > 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print('Congratulations!! You Pass', total_percentage)  # If all conditions are met, print pass message
else:
    print('You Fail!! Better luck next year', total_percentage)  # If any condition fails, print fail message
