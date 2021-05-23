from datetime import date, timedelta
import sys


class Library:
    def __init__(self, count_dict, name):
        self.Count_book_dict = count_dict
        self.name = name
        self.bookdict = dict()
        self.max_book_count = dict()

    def display_books(self):
        for book in self.Count_book_dict.items():
            print(book, Count_book_dict[book][0])


class User():
    def __init__(self, username, password, user, email, mobile, address):
        self.username = username
        self.password = password
        self.user = user
        self.email = email
        self.mobile = mobile
        self.address = address


class Member(User):
    def __init__(self, username, password, user, email, mobile, address, member_id):
        super().__init__(username, password, user, email, mobile, address)
        self.member_id = member_id
        self.max_book_count = dict()
        self.bookdict = dict()

    def Count_book(self, user, book):
        if user not in self.max_book_count:
            self.max_book_count[user] = [book]
            return len(self.max_book_count[user])
        else:
            if len(self.max_book_count[user]) <= 4:
                self.max_book_count[user].append(book)
                return len(self.max_book_count[user])
            else:
                return len(self.max_book_count[user])

    def lend_book(self, user, book):
        if book in library.Count_book_dict.keys():
            if library.Count_book_dict[book][0] >= 1:
                if (book, user) not in self.bookdict.keys():
                    if not self.check_previous_fine(book, user):
                        if self.Count_book(user, book) <= 5:
                            lend_date = date.today()
                            return_date = lend_date + timedelta(days=10)
                            self.bookdict.update({(book, user): return_date})
                            library.Count_book_dict[book][0] -= 1
                            for value in self.bookdict.keys():
                                if value == (book, user):
                                    print('{} book is used to your name {} on {}'.format(
                                        book, user, lend_date))
                                    print('Please return {} by {}'.format(book, return_date))
                                    print(self.max_book_count)
                        else:
                            print('you can issue max 5 books')
                    else:
                        print(
                            'you will have to pay previous fine first, then only u are allowed to issue new book')
                else:
                    print('this book is already issued to u r name')
            else:
                print('this book is out of stock')
        else:
            print('Sorry! we dont have this book in our library')

    def check_previous_fine(self, book, user):
        current.date = date.today()
        for key, val in self.bookdict.items():
            if key[1] == user:
                return_date = self.bookdict[key]
                if current_date > return_date:
                    delay_days = (current_date - return_date).days
                    total_fine = delay_days * 10
                    return total_fine
                else:
                    return 0

    def return_book(self, book, user):
        if (book, user) in self.bookdict.keys():
            return_date = self.bookdict[(book, user)]
            current_date = date.today
            if current_date > return_date:
                delay_days = (current_date - return_date).days
                total_fine = delay_days * 10
                print('please pay the fine, you have to pay Rs {}'.format(total_fine))
                self.payment(book, user)
            else:
                self.max_book_count[user].remove(book)
                self.bookdict.pop((book, user))
                library.Count_book_dict[book][0] += 1
                print('Book sucessfully returned!!')
        else:
            print('Please provide correct username and bookname')

    def payment(self, book, user):
        print('For payment process, Enter u r choice....')
        choice = input('yes', 'no')
        choice = choice.lower()
        while true:
            if choice in ['yes', 'no', 'y', 'n']:
                break
            print('please try again ......')
            choice = input('yes', 'no')
        if choice in ['yes', 'y']:
            print('Your choice is processing.......')
            print('payment sucessfully')
            self.max_book_count[user].remove[book]
            self.bookdict.pop((book, user))
            library.Count_book_dict[book][0] += 1
        else:
            print('Redirecting to homepage.....')

    def check_fine(self, book, user):
        if (book, user) in self.bookdict.keys():
            return_date = self.bookdict[(book, user)]
            current_date = date.today
            if current_date > return_date:
                delay_days = (current_date - return_date).days
                total_fine = delay_days * 10
                print('please pay the fine, you have to pay Rs {}'.format(total_fine))
                print('Do u want to pay fine now ?')
                choice = input('yes', 'no')
                choice = choice.lower()
                while true:
                    if choice in ['yes', 'no', 'y', 'n']:
                        break
                    print('please try again ......')
                    choice = input('yes', 'no')
                    choice = choice.lower()
                if choice in ['yes', 'y']:
                    self.payment(book, user)
                else:
                    print('Redirecting to homepage.....')
            else:
                print('you dont need to pay fine')
        else:
            print('Enter correct information!!')


class librarian(User):

    def __init__(self, username, password, user, email, mobile, address, librarian_id):
        super().__init__(username, password, user, email, mobile, address)
        self.librarian_id = librarian_id

    def add_book(self, book_name, quantity, author, rack, publish_date, pages):
        if quantity > 0:
            if book_name in library.Count_book_dict.keys():
                library.Count_book_dict[book_name][0] += 1
            else:
                library.Count_book_dict.update(
                    {book_name: [quantity, author, rack, publish_date, pages]})
                print('Book is sucessfully added to the libray')
        else:
            print('Please enter positive quantity')

    def removeBook(self, book_name, quantity, author, rack, publish_date, pages):
        if quantity > 0:
            if book_name in library.Count_book_dict.keys():
                if library.Count_book_dict[book_name][0] >= 1:
                    library.Count_book_dict[book_name][0] -= quantity
                    if library.Count_book_dict[book_name][0] < 0:
                        library.Count_book_dict[book_name][0] += quantity
                        print('please enter correct quantity of books, we have only {} books in our library'.format(
                            library.Count_book_dict[book_name][0]))
                    else:
                        print('Book has been sucessfully removed!!')
                else:
                    library.Count_book_dict.pop(book_name)
                    print('sorry we dont have any book with name {}'.format(book_name))
            else:
                print('please enter correct bookname')
        else:
            print('Please enter positive quantity')


class Catalog:

    def searchByName(self, book_name):
        for key, val in library.Count_book_dict.items():
            if book_name in library.Count_book_dict.keys():
                print('Fetching book details.......')
                print()
                print('book name: {} and other details like quantity, author, rack, publish_date, pages: {}'.format(
                    key, val))
                print('')
                choice = input('yes', 'no')
                choice = choice.lower()
                while true:
                    if choice in ['yes', 'no', 'y', 'n']:
                        break
                    print('please try again ......')
                    choice = input('yes', 'no')
                    choice = choice.lower()
                if choice in ['yes', 'y']:
                    break
                else:
                    print('you are exiting the system......')
                    sys.exit()
            else:
                print('we dont have this book in our library, Please check name')
                break

    def searchByAuthor(self, author):
        for key, val in library.Count_book_dict.items():
            if author in library.Count_book_dict.keys():
                print('Fetching book details.......')
                print()
                print('book name: {} and other details like quantity, author, rack, publish_date, pages: {}'.format(
                    key, val))
                print('')
                choice = input('yes', 'no')
                choice = choice.lower()
                while true:
                    if choice in ['yes', 'no', 'y', 'n']:
                        break
                    print('please try again ......')
                    choice = input('yes', 'no')
                    choice = choice.lower()
                if choice in ['yes', 'y']:
                    break
                else:
                    print('you are exiting the system......')
                    sys.exit()
            else:
                print('we dont have this book in our library, Please check name')
                break


library = Library({"the reader": [4, "bernard kansal", "120H", 1995, 218]}, 'BITS')
m1 = Member("na0508", "ajay", "NamanKansal", "f20170508@pilani.bits-pilani.ac.in",
            "9478916123", "NA", '2017A4PS0508P')
catalog = Catalog()
while True:
    string = 'Welcome to libray portal!!'
    print()
    print('*'*len(string))
    print()
    print(string)
    print()
    print('*'*len(string))
    print()
    c = input('press any key to continue.....')
    print()
    print("1.", "display_books")
    print("2.", "lend_book")
    print("3.", "return_book")
    print("4.", "pay_fine")
    print("5.", "search book by name")
    print("6.", "search book by author")
    print()
    print("librarian_tasks")
    print("7.", "add_book")
    print("8.", "remove_book")
    print()
    user_choice = input('Enter Choice:- ')
    if user_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('Please enter correct choice...')
        continue
    else:
        user_choice = int(user_choice)
        if user_choice == 1:
            print('We have following books in {} library'.format(library.name))
            library.display_books()
            print("\n")
        elif user_choice == 2:
            book = input('Please enter the name of the book u want to lend: ')
            user = input('please enter u r name: ')
            m1.lend_book(book, user)
            print()
        elif user_choice == 3:
            book = input('Please enter the name of the book u want to return: ')
            user = input('please enter u r name: ')
            m1.return_book(book, user)
            print()
        elif user_choice == 4:
            book = input('Please enter the name of the book having a fine: ')
            user = input('please enter u r name: ')
            m1.check_fine(book, user)
            print()
        elif user_choice == 5:
            book_name = input('Enter the name of the book: ')
            catalog.searchByName(book_name)
            print()
        elif user_choice == 6:
            author = input('Enter the author of the book: ')
            catalog.searchByName(author)
            print()
        elif user_choice == 7:
            username = input('username:- ')
            password = input('password:- ')
            libr = librarian(username, password, "kumar",
                             'namankansaldui2000@gmail.com', '9660299333', "NA", "11120170508")
            print('now you can add book in the library')
            print()
            book_name = input('Enter the name of book u want to add:- ')
            quantity = int(input('Enter no of books to add:- '))
            author = input('Enter the author of the book:- ')
            rack = input('Enter the rack number:- ')
            publish_date = input('Enter the publish date of the book:- ')
            pages = input('Enter no of pages in the book:- ')
            libr.add_book(book_name, quantity, author, rack, publish_date, pages)
            print()
        elif user_choice == 8:
            username = input('username:- ')
            password = input('password:- ')
            libr = librarian(username, password, "kumar",
                             'namankansaldui2000@gmail.com', '9660299333', "NA", "11120170508")
            print('now you can add book in the library')
            print()
            book_name = input('Enter the name of book u want to add:- ')
            quantity = int(input('Enter no of books to add:- '))
            author = input('Enter the author of the book:- ')
            rack = input('Enter the rack number:- ')
            publish_date = input('Enter the publish date of the book:- ')
            pages = input('Enter no of pages in the book:- ')
            libr.removeBook(book_name, quantity, author, rack, publish_date, pages)
            print()
        else:
            print('Not a valid option!!')
            print()
        print("q to quit or c to continue.....")
        choice = ""
        while choice != 'c' and choice != 'q':
            choice = input('Enter u r choice:- ')
            if choice in ['c', 'C']:
                continue
            elif choice in ['q', 'Q']:
                sys.exit()
            else:
                print('please enter correct choice....')
                print()
