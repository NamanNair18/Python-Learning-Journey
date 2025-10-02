# 📚 Library Management System (Python)

A simple **Library Management System** implemented in Python using dictionaries and lists.  
This project demonstrates basic concepts of **data structures, functions, and user interaction**.

---

## 🚀 Features
- ➕ **Add Book** – Add new books with unique ID, title, and author.  
- 📖 **Display Books** – View all available books in a neat tabular format.  
- 📚 **Borrow Book** – Borrow a book if it is available.  
- 🔄 **Return Book** – Return a previously borrowed book.  
- ❌ **Exit** – Quit the system safely.  

---

## 🛠️ How It Works
- Each book is stored as a **dictionary** with keys:
  - `id`: Unique book ID
  - `title`: Title of the book
  - `author`: Author of the book
  - `available`: Availability status (`True` = Available, `False` = Borrowed)
- All books are maintained in a **list of dictionaries**.
- Menu-driven system for user interaction.

---

## 📑 Sample Books (Preloaded)
```python
books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "available": True},
    {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart", "available": True},
    {"id": 3, "title": "Think Python", "author": "Allen B. Downey", "available": False},
    {"id": 4, "title": "Data Science from Scratch", "author": "Joel Grus", "available": True},
    {"id": 5, "title": "Fluent Python", "author": "Luciano Ramalho", "available": False}
]
