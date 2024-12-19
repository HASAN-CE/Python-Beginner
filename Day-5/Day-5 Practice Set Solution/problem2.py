# Creating an empty set
s = set()  # A set to store unique numbers entered by the user

# Taking inputs from the user and adding them to the set
N1 = input("ENTER THE 1 NUMBER: ")  # Prompt user for the 1st number
s.add(int(N1))  # Convert the input to an integer and add it to the set

N2 = input("ENTER THE 2 NUMBER: ")  # Prompt user for the 2nd number
s.add(int(N2))  # Convert the input to an integer and add it to the set

N3 = input("ENTER THE 3 NUMBER: ")  # Prompt user for the 3rd number
s.add(int(N3))  # Convert the input to an integer and add it to the set

N4 = input("ENTER THE 4 NUMBER: ")  # Prompt user for the 4th number
s.add(int(N4))  # Convert the input to an integer and add it to the set

N4 = input("ENTER THE 4 NUMBER: ")  # Prompt user for the 4th number again
s.add(int(N4))  # Convert the input to an integer and add it to the set (duplicates will be ignored)

N5 = input("ENTER THE 5 NUMBER: ")  # Prompt user for the 5th number
s.add(int(N5))  # Convert the input to an integer and add it to the set

N6 = input("ENTER THE 6 NUMBER: ")  # Prompt user for the 6th number
s.add(int(N6))  # Convert the input to an integer and add it to the set

N7 = input("ENTER THE 7 NUMBER: ")  # Prompt user for the 7th number
s.add(int(N7))  # Convert the input to an integer and add it to the set

N8 = input("ENTER THE 8 NUMBER: ")  # Prompt user for the 8th number
s.add(int(N8))  # Convert the input to an integer and add it to the set

# Printing the final set
# The set will only include unique numbers entered by the user, as sets automatically remove duplicates
print("Set Follows: ", s)  # Prints the unique numbers stored in the set
