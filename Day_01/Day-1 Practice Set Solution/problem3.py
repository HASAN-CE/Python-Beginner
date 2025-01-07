import os

# Specify the path
path = "."

# List the contents of the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)
