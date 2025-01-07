# Default Arguments
# Since the `end` argument is not changing and remains the same, we can set it as a default argument.
def Greet(name, end):
    print(f'Dear, {name} {end}')  # This function takes two arguments: `name` and `end`, and prints a greeting message with an optional ending.

Greet('John', 'Thank you for Coming')
Greet('Payal', 'Thank you for Coming')
Greet('Harry', 'Thank you for Coming')


# Default Arguments Example
def Greet1(name, end='Thanks for coming'):
    print(f'Dear, {name} {end}')  # This function takes two arguments: `name` and an optional `end` with a default value of 'Thanks for coming'.

print('\nWith the default arguments')
Greet1('John')
Greet1('Payal')
Greet1('Harry')
