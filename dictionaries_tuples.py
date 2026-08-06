books = {
    'book1':{
        'title': 'Atomic Habits',
        'author': 'James Clear',
        'genres': (
            'Self-help',
            'Productivity'
        ), 
        'year': 2018
    },
    'book2':{
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'genres': (
            'Adventure',
            'Fiction'
        ),
        'year': 1988
    },
    'book3': {
        'title': "Harry Potter and the Philosopher's Stone",
        'author': 'J.K. Rowling',
        'genres': (
            'Fantasy',
            'Adventure'
        ),
        'year': 1997
    }
}

def display_books():
    for key, value in books.items():
        print(f"\n========== {key} ==========")
        for display_key, display_value in value.items():
            print(display_key, ':', display_value)

def view_one_book():
    user_book = input('Which book do you want to view? ').strip().lower()
    if user_book in books:
        selected_book = books[user_book]
        for book_key, book_value in selected_book.items():
            print(book_key,':', book_value)
    else:
        print('That book does not exist.')
def update_book():
    update_question = input('Which book do you want to update? ').strip().lower()
    if update_question in books:
        update_info = books[update_question]
        info_key = input('Which piece of information do you want to update? ').strip().lower()
        if info_key in update_info:
            if info_key == 'genres':
                print('Genres cannot be updated because they are stored as a tuple.')
            else:
                update_value = input('What should the new value be? ')
                update_info[info_key] = update_value
                print('Book updated successfully!')
                for update_key, update_key_value in update_info.items():
                    print(update_key, ':', update_key_value)
        else:
            print('This information is not available!')
    else:
        print('That book is not available!')

def add_book():
    book_id = input('Create a new book ID: ').strip().lower()
    if book_id in books:
        print('That book ID already exists.')
    else:
        title = input('Enter the title of the book: ')
        author = input('Enter the author of the book: ')
        genre1 = input('Enter the genre of the book: ')
        genre2 = input('Enter another genre of the book: ')
        year = int(input('Enter the year the book was created: '))
        books[book_id] = {
            'title': title,
            'author': author,
            'genres': (
                genre1,
                genre2
            ),
            'year': year
        }
        print('Book added successfully!')
        for book_key, book_value in books[book_id].items():
            print(book_key, ':', book_value)

def delete_book():
    delete_question = input('Which book ID do you want to delete? ').strip().lower()
    if delete_question in books:
        books.pop(delete_question)
        print('Book deleted successfully!')
        display_books()
    else:
        print('That book ID does not exist')
        
def pause():
    input("\nPress Enter to return to the menu...")

while True:
    print('\n========== LIBRARY MANAGEMENT SYSTEM ==========')
    print('\n1. Display all books')
    print('2. View one book')
    print('3. Update book')
    print('4. Add book')
    print('5. Delete book')
    print('6. Exit')
    choice = input('Enter your choice(1-6): ').strip().lower()

    if choice == '1':
        display_books()
        pause()
    elif choice == '2':
        view_one_book()
        pause()
    elif choice == '3':
        update_book()
        pause()
    elif choice == '4':
        add_book()
        pause()
    elif choice == '5':
        delete_book()
        pause()
    elif choice == '6':
        print('Goodbye!')
        break
    else:
        print('Invalid option. Please try again.')