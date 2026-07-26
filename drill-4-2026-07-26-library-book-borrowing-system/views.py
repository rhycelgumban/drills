from models import books

def show_books():
    print("\n===== ALL BOOKS =====")
    for i, book in enumerate(books, start=1):
        status = "Borrowed" if book["is_borrowed"] else "Available"
        borrower = book["borrowed_by"] if book["borrowed_by"] else "-"
        print(f"{i}. {book['title']} by {book['author']}")
        print(f"   Status: {status}")
        print(f"   Borrowed By: {borrower}\n")


def borrow_book():
    show_books()

    choice = int(input("Enter book number to borrow: "))

    if 1 <= choice <= len(books):
        book = books[choice - 1]

        if book["is_borrowed"]:
            print("This book is already borrowed.")
        else:
            student = input("Enter student name: ")
            book["is_borrowed"] = True
            book["borrowed_by"] = student
            print("Book borrowed successfully!")
    else:
        print("Invalid book number.")


def return_book():
    show_books()

    choice = int(input("Enter book number to return: "))

    if 1 <= choice <= len(books):
        book = books[choice - 1]

        if not book["is_borrowed"]:
            print("This book is already available.")
        else:
            book["is_borrowed"] = False
            book["borrowed_by"] = ""
            print("Book returned successfully!")
    else:
        print("Invalid book number.")


def show_available_books():
    print("\n===== AVAILABLE BOOKS =====")

    found = False

    for i, book in enumerate(books, start=1):
        if not book["is_borrowed"]:
            print(f"{i}. {book['title']} by {book['author']}")
            found = True

    if not found:
        print("No available books.")


def show_borrowed_books():
    print("\n===== BORROWED BOOKS =====")

    found = False

    for i, book in enumerate(books, start=1):
        if book["is_borrowed"]:
            print(f"{i}. {book['title']} - Borrowed by {book['borrowed_by']}")
            found = True

    if not found:
        print("No borrowed books.")