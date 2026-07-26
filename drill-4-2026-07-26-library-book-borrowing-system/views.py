from models import books


def show_books():
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
    show_books()

    number = int(input("Select book number: ")) - 1

    if books[number]["is_borrowed"]:
        print("Book is already borrowed.")
    else:
        student = input("Student name: ")

        books[number]["is_borrowed"] = True
        books[number]["borrowed_by"] = student

        print("Book borrowed successfully.")


def return_book():
    show_books()

    number = int(input("Select book number: ")) - 1

    if books[number]["is_borrowed"]:
        books[number]["is_borrowed"] = False
        books[number]["borrowed_by"] = ""

        print("Book returned successfully.")
    else:
        print("Book is already available.")


def show_available_books():
    print("\n===== AVAILABLE BOOKS =====")

    for book in books:
        if not book["is_borrowed"]:
            print(f"- {book['title']} by {book['author']}")


def show_borrowed_books():
    print("\n===== BORROWED BOOKS =====")

    found = False

    for book in books:
        if book["is_borrowed"]:
            print(f"- {book['title']} (Borrowed by {book['borrowed_by']})")
            found = True

    if not found:
        print("No borrowed books.")