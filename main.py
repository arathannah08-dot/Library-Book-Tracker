#LIBRARY BOOK MANAGEMENT SYSTEM

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
        print("\n=== ADD NEW BOOK ===")
        title = input("Enter book title: ")
        if title.strip() == "":
            print("Please enter the book title.")
        else:
            found = False

            for book in books:
                if book["title"].lower() == title.lower():
                    book["copies"] += 1
                    found = True
                    print("Book added successfully (copy)!")
                    break

            if not found:
                books.append({
                    "title": title,
                    "copies": 1,
                    "borrowed": 0
                })
                print("Book added successfully!")

    #TO CHECK BOOK AVAILABILITY
    elif choice == "2":
        print("\n=== VIEW BOOKS ===")
        if len(books) == 0:
            print("No books in the library.")
        else:
            for book in books:
                available = book["copies"] - book["borrowed"]

                print("\nTitle: ", book["title"])
                print("Total Copies: ", book["copies"])
                print("Available Copies: ", available)
                print("Borrowed Copies: ", book["borrowed"])
                print("---------------------------")

    #TO SEARCH BOOK
    elif choice =="3":
        print("\n=== SEARCH BOOK ===")
        title = input ("Search book title: ")
        found = False

        for book in books:
            if title.lower() in book["title"].lower():
                
                available = book["copies"] - book["borrowed"]

                print("\nTitle: ", book["title"])
                print("Total Copies: ", book["copies"])
                print("Available Copies: ", available)
                print("Borrowed Copies: ", book["borrowed"])
                print("---------------------------")
                
                found = True

        if not found:
            print("Book not found.")

    #TO BORROW BOOK
    elif choice == "4":
        print("\n=== BORROW BOOK ===")
        title = input("Enter the title to borrow: ")
        found = False

        for book in books:
            if book["title"].lower() == title.lower():
                found = True

                available = book["copies"] - book["borrowed"]

                if available > 0:
                    book["borrowed"] += 1
                    print("Book borrowed successfully!")
                else:
                    print("Sorry. No available copy/copies for this book.")
                break

        if not found:
            print("Book not found.")

    #TO RETURN BOOK
    elif choice == "5":
        print("\n=== RETURN BOOK ===")
        title = input("Enter the title to return: ")
        found = False

        for book in books:
            if book["title"].lower() == title.lower():
                found = True

                if book["borrowed"] > 0:
                    book["borrowed"] -= 1
                    print("Book returned successfully!")
                else:
                    print("No copy/copies of this book was borrowed.")
                break

        if not found:
            print("Book not found.")

    #TO EXIT
    elif choice == "6":
        print("Thank you for using the Library Book Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
