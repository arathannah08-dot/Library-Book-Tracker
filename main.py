
books = []

while True:
    print("\n=== LIBRARY BOOK TRACKER ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    #TO ADD NEW BOOK
    if choice == "1":
        title = input("Enter book title: ")
        books.append({"title": title, "status": "Available"})
        print("Book added successfully!")

    #TO CHECK BOOK AVAILABILITY
    elif choice == "2":
        if len(books) == 0:
            print("No books in the library.")
        else:
            for book in books:
                print(book["title"], "-", book["status"])

    #TO BORROW BOOK
    elif choice == "3":
        title = input("Enter the title to borrow: ")
        found = False

        for book in books:
            if book["title"].lower() == title.lower():
                found = True
                if book["status"] == "Available":
                    book["status"] = "Borrowed"
                    print("Book borrowed successfully!")
                else:
                    print("This book is already borrowed.")
                break

        if not found:
            print("Book not found.")

    #TO RETURN BOOK
    elif choice == "4":
        title = input("Enter the title to return: ")
        found = False

        for book in books:
            if book["title"].lower() == title.lower():
                found = True
                if book["status"] == "Borrowed":
                    book["status"] = "Available"
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed.")
                break

        if not found:
            print("Book not found.")

    #TO EXIT
    elif choice == "5":
        print("Thank you for using the Library Book Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
