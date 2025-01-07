'''
cm = in X 2.54
'''

inc = int(input('Enter the Inches: '))  # Input for the inches

def inc_to_cm(inc):
    return inc * 2.54  # Conversion from inches to centimeters

print("Answer is:", inc_to_cm(inc))  # Output the converted value
