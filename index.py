# List to hold book data
books = [
    {
        'ID': 1,
        'Title': 'To Kill a Mockingbird',
        'Author': 'Harper Lee',
        'Genre': 'Fiction',
        'Status': 'Available'
    },
    {
        'ID': 2,
        'Title': '1984',
        'Author': 'George Orwell',
        'Genre': 'Dystopian',
        'Status': 'Borrowed'
    },
    {
        'ID': 3,
        'Title': 'Moby Dick',
        'Author': 'Herman Melville',
        'Genre': 'Adventure',
        'Status': 'Available'
    }
]

# List to hold user data
users = [
    {
        'ID': 101,
        'Name': 'Alice',
        'Borrowed Books': 2 , # User has borrowed the book with ID 2
        'Borrowed Books Names':[],
         "Borrowed Books id ":[]
    },
    {
        'ID': 102,
        'Name': 'Bob',
        'Borrowed Books ': 0,
        'Borrowed Books Names':[],
        "Borrowed Books id ":[]
    }
]

# Create separate functions for tasks like adding a book, borrowing a book, or searching for books to keep the code organized.

def addBook():
    BookId=int(input("enter your Book ID"))
    bookName=input("enter Your Book Name:-").capitalize()
    bookAuthor=input("enter Your Book Author:-").capitalize()
    bookGenre=input("enter Your Book Genre:-").capitalize()
    newBook={
        'ID':BookId,
        'Title':bookName,
        'Author':bookAuthor,
        'Genre':bookGenre,
        'Status':'Available'
    }
    books.append(newBook)
    print("Book Added Successfully",books)
def BorrowBook():
    bookId=int(input("enter your book id"))
    for book in books:
        if book['ID'] == bookId:
            if book['Status'] == 'Available':
                Ask=input("You Want to tak Book Entet Y and E for exit").lower()
                if Ask=='y':
                    book['Status']='Borrowed'
                    user=int(input("Enter Your User ID"))
                    for user1 in users:
                        if user1['ID'] == int(user):
                            user1['Borrowed Books']=+1
                            user1['Borrowed Books Names'].append(book['Title']) 
                            user1['Borrowed Books id'].append(bookId)
                            print("Book Borrowed Successfully >> Your All Books NAmes",user1['Borrowed Books Names'])
                elif Ask=='exit':
                    break



def AllBooks():
    for book in books:
        print(f"""
------------------------------------------
Book ID: {book['ID']}
Title: {book['Title']}
Author: {book['Author']}
Genre: {book['Genre']}
Status: {book['Status']}
------------------------------------------
        """)





def AllUsers():
    for user in users:
        print(f"""
------------------------------------------
User ID: {user['ID']}
User Name:{user['Name']}
User Borrowed Books:{user['Borrowed Books Names']}
------------------------------------------
        """)



def ReturnBook(user_id):
    # Find the user by ID
    user = next((u for u in users if u['ID'] == user_id), None)

    if user is None:
        print("User not found.")
        return

    # Check if the user has any borrowed books
    if len(user["Borrowed Books Names"]) > 0:
        try:
            bookId = int(input("Id of the book you want to return: "))
            if bookId in user['Borrowed Books id']:
                for book in books:
                    if book['ID'] == bookId:
                        if book['Status'] == 'Borrowed':
                            Ask = input("Do you want to return the book? Enter 'Y' for yes or 'E' to exit: ")
                            if Ask == 'Y':
                                book['Status'] = 'Available'
                                # Remove the book from the user's borrowed books list
                                book_name = user["Borrowed Books Names"][user["Borrowed Books id"].index(bookId)]
                                user["Borrowed Books Names"].remove(book_name)
                                user["Borrowed Books id"].remove(bookId)
                                user['Borrowed Books'] -= 1
                                print(f"Book '{book_name}' returned successfully!")
                            elif Ask == 'E':
                                print("Return process exited.")
                            break
                else:
                    print("Book ID not found in the system.")
            else:
                print("Book ID not found in user's borrowed books.")
        except ValueError:
            print("Invalid book ID. Please enter a number.")
    else:
        print(f"{user['Name']} has no borrowed books to return.")


def SearchBook():
    search_term = input("Enter the book title or author to search: ").capitalize()
    found_books = []

    for book in books:
       
        if search_term in book['Title'].capitalize() or search_term in book['Author'].capitalize():
            found_books.append(book)

    if found_books:
        print("Books found:")
        for b in found_books:
            print(f"ID: {b['ID']}, Title: {b['Title']}, Author: {b['Author']}, Status: {b['Status']}")
    else:
        print("No books found matching your search.")




while True:
    print('Welcome to the Community Library System!')
    print('----------------------------------------')
    print('Please choose an option:')
    print('1. View all books')
    print('2. Search for a book')
    print('3. Borrow a book')
    print('4. Return a book')
    print('5. View all users')
    print('6. Exit')
    Option=int(input('Enter Your Option 1 to 6 :- '))
    if Option==6:
        break
    elif Option==1:
        AllBooks()
    elif Option==2:
        SearchBook()
    elif Option==3:
        BorrowBook()
    elif Option==4:
        Id=int(input("Enter Your Id"))
        ReturnBook(Id)
    elif Option==5:
        AllUsers()

    


# Alhamdulillah 