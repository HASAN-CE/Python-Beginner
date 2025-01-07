'''Question: Create a Python program to manage a small library database. The program should:
Store book details as a dictionary, where keys are book titles (as strings) and values are tuples containing the author's name (string) and the publication year (integer).
Allow the user to:
Add a new book to the library.
Search for a book by title and display its details.
Update the details of an existing book.
Display all book titles as a sorted list.
'''

library = {
    "To Kill a Mockingbird": ("Harper Lee", 1960),
    "1984": ("George Orwell", 1949),
    "The Great Gatsby": ("F. Scott Fitzgerald", 1925),
    "Pride and Prejudice": ("Jane Austen", 1813),
    "The Catcher in the Rye": ("J.D. Salinger", 1951),
    "Moby Dick": ("Herman Melville", 1851),
    "The Hobbit": ("J.R.R. Tolkien", 1937)
}

# Search for a book by title and display its details.
Book_name  = input("Enter the Book Name: ")
print(library[Book_name])

#Add a new book to the library.
print("Enter the New Book DETAILS: ")
New_book = input("NEW BOOK: ")
New_Author = input("NEW AUTHOR: ") 
New_Year =  int(input("New YEAR: "))
library.update({New_book:(New_Author,New_Year)})
print(library)

# Update the details of an existing book.
Update_book = input("Update BOOK: ")
Update_Author = input("Update AUTHOR: ") 
Update_Year =  int(input("Update YEAR: "))
library.update({Update_book:(Update_Author,Update_Year)})
print(library)

# Display all book titles as a sorted list.
sorted_titles = sorted(library.keys())
print(sorted_titles)