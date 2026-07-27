from models import books


def show_all_books():
    print("\n===== ALL BOOKS =====")

    for i, book in enumerate(books, start=1):
        status = "Borrowed" if book["is_borrowed"] else "Available"

        print(f"{i}. {book['title']}")
        print(f"   Author: {book['author']}")
        print(f"   Status: {status}")

        if book["is_borrowed"]:
            print(f"   Borrowed by: {book['borrowed_by']}")

        print()


def borrow_book():
    show_all_books()

    choice = int(input("Enter book number: ")) - 1

    if books[choice]["is_borrowed"]:
        print("This book is already borrowed.")
    else:
        student = input("Student Name: ")

        books[choice]["is_borrowed"] = True
        books[choice]["borrowed_by"] = student

        print("Book borrowed successfully!")


def return_book():
    show_all_books()

    choice = int(input("Enter book number: ")) - 1

    if books[choice]["is_borrowed"]:
        books[choice]["is_borrowed"] = False
        books[choice]["borrowed_by"] = ""

        print("Book returned successfully!")
    else:
        print("This book is already available.")


def show_available_books():
    print("\n===== AVAILABLE BOOKS =====")

    for i, book in enumerate(books, start=1):
        if not book["is_borrowed"]:
            print(f"{i}. {book['title']} - {book['author']}")


def show_borrowed_books():
    print("\n===== BORROWED BOOKS =====")

    found = False

    for i, book in enumerate(books, start=1):
        if book["is_borrowed"]:
            print(f"{i}. {book['title']} - Borrowed by {book['borrowed_by']}")
            found = True

    if not found:
        print("No borrowed books.")