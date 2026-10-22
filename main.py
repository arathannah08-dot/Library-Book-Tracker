
books = []

while True:
    print("\n=== LIBRARY BOOK TRACKER ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    #TO ADD NEW BOOK
    if choice == "1":
        title = input("Enter book title: ")
        if title.strip() == "":
            print("Please enter the book title.")
        else:
            books.append({"title": title, "status": "Available"})
            print("Book added successfully!")

    #TO CHECK BOOK AVAILABILITY
    elif choice == "2":
        if len(books) == 0:
            print("No books in the library.")
        else:
            for book in books:
                print(book["title"], "-", book["status"])

    #TO SEARCH BOOK
    elif choice =="3":
        title = input ("Search book title: ")
        found = False

        for book in books:
            if title.lower() in book["title"].lower():
                print(book["title"], "-", book["status"])
                found = True

        if not found:
            print("Book not found.")

    #TO BORROW BOOK
    elif choice == "4":
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
    elif choice == "5":
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
    elif choice == "6":
        print("Thank you for using the Library Book Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
