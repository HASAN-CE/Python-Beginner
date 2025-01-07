# List of names
l1 = ["Harry", "Soham", "Sachin", "Rahul"]

# Using While Loop
i = 0
while i < len(l1):
    if l1[i].startswith('S'):  # Check if the name starts with 'S'
        print(l1[i], "Good Morning")  # Print the greeting
    i += 1

# Using For Loop
for name in l1:
    if name.startswith('S'):  # Check if the name starts with 'S'
        print(name, "Good Morning")  # Print the greeting
