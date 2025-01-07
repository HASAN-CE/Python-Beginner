'Write a program to check if a number is positive, negative, or zero.'

num1 = int(input('Enter the number: '))
if num1 < 0:
    print('Number is Negative')
elif num1 == 0:
    print('Number is Zero')
elif num1>0:
    print('Number is Positive')
else:
    print('Invalid input')