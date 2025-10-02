#List of Dictionaries
books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "available": True},
    {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart", "available": True},
    {"id": 3, "title": "Think Python", "author": "Allen B. Downey", "available": False},
    {"id": 4, "title": "Data Science from Scratch", "author": "Joel Grus", "available": True},
    {"id": 5, "title": "Fluent Python", "author": "Luciano Ramalho", "available": False}
]

def add_book():
    #ask for book details
    title = input("Enter book title:- ")
    author = input("Enter book author:- ")

    #generate unique ID
    if books:
        new_id = max(book["id"] for book in books) + 1
    else:
        new_id = 1
    
    #creating new dictionary 
    new_book={
        "id":new_id,
        "title": title,
        "author":author,
        "available":True
    }
    #add the book into the list
    books.append(new_book)

    print(f"Book {title} Wriiten By {author} added Succesfully with ID {new_id}")


# Function to Borrow a book
def borrow_book(book_id):
    for book in books:
        if book["id"] == book_id:#Checking if the book exist 
            if book["available"]:
                book["available"] = False
                print(f"You have succesfully Borrowed '{book['title']}'. ")
            else:
                print(f"Sorry '{book['title']}' is already Borrowed")
            return
    print("book not found")

# Function to return a book
def return_book(book_id):
    for book in books:
        if book["id"] == book_id:# check if book exists
            if not book["available"]: # if it was borrowed
                book["available"] = True
                print(f"You have successfully returned '{book['title']}'.")
            else:
                print(f"'{book['title']}' was not returned.")
            return
    print("Book not found")

## Function to display all books
def display_books():
    if not books:
        print("No Books in the Library.")
        return

    print("\nID | Title                     | Author               | Status")
    print("-" * 60)
    for book in books:
        status = "Available" if book["available"] else "Borrowed"
        print(f"{book['id']:2} | {book['title']:<25} | {book['author']:<20} | {status}")

while True:
    print("\n=========Library Managment system==========")
    print("1. Add Book")
    print("2. Display Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter Your Choice (1-5)")

    if choice == "1":
      add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        book_id = input("Enter the ID of the book to borrow: ")
        # Need to ensure it's an integer before passing
        try:
            borrow_book(int(book_id))
        except ValueError:
            print("Invalid input. Please enter a number for the book ID.")
    elif choice == "4":
        book_id = input("Enter the ID of the book to return: ")
        # Need to ensure it's an integer before passing
        try:
            return_book(int(book_id))
        except ValueError:
            print("Invalid input. Please enter a number for the book ID.")
    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid Choice, Enter a Valid Choice 1-5.")








