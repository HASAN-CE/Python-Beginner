# Countine, Break, and Pass Statements

# Break Statement
for i in range(1, 101):
    if (i == 37):
        break  # Exit the loop
    print(i)

# Continue Statement
for i in range(1, 101):
    if (i % 2 != 0):
        continue  # Skip this (current) iteration
    print(i)

# Pass Statement
i = 0
for i in range(1, 101):
    pass  # Not feeling like it today, let's look at it tomorrow.

while (i < 45):
    print(i)
