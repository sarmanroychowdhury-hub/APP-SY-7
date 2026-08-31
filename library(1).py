# Class representing a Book
class Book:
    def _init_(self, title): 
        # Store the title of the book
        self.title = title
        
        # Set the book as available by default
        self.available = True


# Class representing a Library Patron
class Patron:
    def _init_(self, name):    
        # Store the name of the patron
        self.name = name


# Class representing the Library
class Library:
    def _init_(self):    
        # List to store all books
        self.books = []
        
        # List to store all registered patrons
        self.patrons = [] 
    
    # Method to add a new book to the library
    def add_book(self, title):
        self.title = title
        
        # Create a Book object and add it to the books list
        self.books.append(Book())
        
        print("Book added successfully.")
        
    # Method to register a new patron
    def register_patron(self, name="unknown"):
        # Create a Patron object and add it to the patrons list
        self.patrons.append(Patron(name))
        
        print("Patrons registered successfully.")
        
    # Method to borrow a book
    def borrow_book(self, title):
        # Search for the book in the library
        for book in self.books:
            if book.title == title:
                
                # Check whether the book is available
                if book.available:
                    book.available = False
                    print("Book borrowed successfully.")
                else:
                    print("Book is already borrowed.")
                    return
        
        # Display message if the book was not found
        print("Book not found.")
    
    # Method to return a book
    def return_book(self, title):
        # Search for the book in the library
        for book in self.books:
            if book.title == title:
                
                # Check whether the book was borrowed
                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book is already returned.")
                    return
        
        # Display message if the book was not found
        print("Book not found.")
            
    # Method to display all books
    def display_books(self):
        # Check if there are no books
        if len(self.books) == 0:
            print("No books in library")
        else:
            # Display each book and its status
            for book in self.books:
                if book.available:
                    status = "Available" 
                else:
                    status = "Borrowed"
                
                print(book.title, "_", status)


# Create a Library object
library = Library()
    
# Keep displaying the menu until the user chooses Exit
while True:
    print("\n--Library Management System--")
    print("1.Add Book")
    print("2.Register Patron")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Display Books")
    print("6.Exit")
      
    # Ask the user to enter a menu choice
    choice = int(input("Enter your choice:"))
    
    # Option 1: Add books
    if choice == 1:
        for i in range(2):
            # Take the book title from the user
            title = input("Enter book title:")
        
        # Add the book to the library
        Library.add_book(title)
    
    # Option 2: Register a patron
    elif choice == 2:
        name = input("Enter patron name:")
        
        # Register the patron in the library
        Library.register_patron(name)
    
    # Option 3: Borrow a book
    elif choice == 3:
        title = input("Enter book title to borrow:")
        
        # Call the borrow_book method
        Library.borrow_book(title)
    
    # Option 4: Return a book
    elif choice == 4:
        title = input("Enter book title to return:")
        
        # Call the return_book method
        Library.return_book(title)
    
    # Option 5: Display all books
    elif choice == 5:
        Library.display_books()
    
    # Option 6: Exit the program
    elif choice == 6:
        print("Exiting...")
        break
    
    # Handle an invalid menu choice
    else:
        print("Invalid choice")
