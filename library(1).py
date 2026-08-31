class Book:
    def _init_(self,title): 
     self.title = title
     self.available = True
      
class Patron :
    def _init_(self,name):    
     self.name = name
      
class Library:
    def _init_(self):    
     self.books =[]
     self.patrons=[] 
    
    def add_book(self,title):
     self.title= title
     self.books.append(Book())
     print("Book added successfully.")
        
    def register_patron(self, name="unknown"):
     self.patrons.append(Patron(name))
     print("Patrons registered successfully.")
        
    def borrow_book(self,title):
      for book in self.books:
        if book.title==title:
            if book.available:
                book.available= False
                print("Book borrowed successfully.")
            else:
                print("Book is already borrowed.")
                return
            print("Book not found.")
    
    def return_book(self,title):
      for book in self.books:
        if book.title==title:
            if not book.available:
                book.available= True
                print("Book returned successfully.")
            else:
                print("Book is already returned.")
                return
            print("Book not found.")
            
    def display_books(self):
        if len(self.books)==0:
          print("No books in library")
        else:
          for book in self.books:
            if book.available:
               status="Available" 
            else:
               "Borrowed"
               print(book.title,"_",status)
    
library = Library()
    
while True:
    print("\n--Library Management System--")
    print("1.Add Book")
    print("2.Register Patron")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Display Books")
    print("6.Exit")
      
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        for i in range(2):
          title = input("Enter book title:")
        Library.add_book(title)
    elif choice ==2:
          name = input("Enter patron name:")
          Library.register_patron(name)
    elif choice == 3:
          title =input("Enter book title to borrow:")
          Library.borrow_book(title)
    elif choice == 4 :
          title =input("Enter book title to return:")
          Library.return_book(title)
    elif choice == 5:
          Library.display_books()
    elif choice == 6:
          print("Existing...")
          break
    else:
          print("Invalid choice")
