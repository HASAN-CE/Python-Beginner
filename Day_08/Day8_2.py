# Arguments in Function

# Single argument
def goodDay(name):
    print(f'Good Day, {name}')  # Function that takes a single argument and prints a greeting

goodDay('John')
goodDay('Payal')
goodDay('Harry')
goodDay('Rohan')

# Double argument
def Greet(name, end):
    print(f'Dear, {name} {end}')  # Function that takes two arguments and prints a greeting with a closing statement

Greet('John', 'Thank you for Coming')
Greet('Payal', 'Thank you for Coming')
Greet('Harry', 'Thank you for Coming')

# return keyword
def avg(a, b):
    return (a + b) / 2  # Function that calculates and returns the average of two numbers

a = avg(7, 2)  # Calculates the average of 7 and 2
print("Average:", a)  # Output: Average: 4.5
