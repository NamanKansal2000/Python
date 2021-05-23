import datetime
import sys


class Library:
    def __init__(self, count_dict, name):
        self.Count_book_dict = count_dict
        self.name = name
        self.bookdict = dict()
        self.max_book_count = dict()

    def display_books(self):
        count = 1
        for book, val in self.Count_book_dict.items():
            print(count, book, val)
            count += 1


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


def register():
    firstname = input("Please input first name:- ").lower()
    middlename = input("Please input middle name:- ").lower()
    lastname = input("Please input first name:- ").lower()
    if middlename.isalpha():
        username = (firstname.capitalize() +
                    middlename.capitalize() + lastname.capitalize())
    else:
        username = (firstname.capitalize() + lastname.capitalize())
    password = (input("Please input your desired password:- "))
    # username, password, user, email, mobile, address, member_id
    user = (firstname)
    id = input('please enter u r BITS id:- ')
    email = ('f'+id[:4]+id[8:12]+'@pilani.bits-pilani.ac.in')
    mobile = (input('Please enter u r mobile no:- '))
    address = (input('Enter u r hostel and room no (without space ex (RAM2118)) :- '))
    member_id = (id)
    usr_name = firstname[:2]+id[8:12]
    print('"{}" this is u r username'.format(usr_name))
    print()
    post = input('U r registering as student/staff:- ')
    post = post.lower()
    while True:
        if post in ['student', 'staff']:
            break
        print('please enter a valid input...')
        post = input('U r registering as student/staff:- ')
        post = post.lower()
    if post == 'student':
        file = open("student_file.txt", "a")
        file.write(usr_name)
        file.write("\t")
        file.write(password)
        file.write("\t")
        file.write(username)
        file.write("\t")
        file.write(user)
        file.write("\t")
        file.write(email)
        file.write("\t")
        file.write(mobile)
        file.write("\t")
        file.write(address)
        file.write("\t")
        file.write(member_id)
        file.write("\n")
        file.close()
        if login('student'):
            print("You are now logged in...")
            return 'student', usr_name
        else:
            print("You aren't logged in!")
    elif post == 'staff':
        print('Enter passkey to continue...')
        print('passkey:- 111')
        key = input('Enter passkey:- ')
        if key == '111':
            file = open("staff_file.txt", "a")
            file.write(usr_name)
            file.write("\t")
            file.write(password)
            file.write("\t")
            file.write(username)
            file.write("\t")
            file.write(user)
            file.write("\t")
            file.write(email)
            file.write("\t")
            file.write(mobile)
            file.write("\t")
            file.write(address)
            file.write("\t")
            file.write(member_id)
            file.write("\t")
            file.close()
            if login('staff'):
                print("You are now logged in...")
                return 'staff', usr_name
            else:
                print("You aren't logged in!")


def login(post):
    username = input("Please enter your username:- ")
    password = input("Please enter your password:- ")
    if post == 'student':
        for line in open("student_file.txt", "r").readlines():  # Read the lines
            login_info = line.split()  # Split on the space, and store the results in a list of two strings
            if username == login_info[0] and password == login_info[1]:
                print("Correct credentials!")
                return True, username
        print("Incorrect credentials.")
        return False
    if post == 'staff':
        for line in open("staff_file.txt", "r").readlines():  # Read the lines
            login_info = line.split()  # Split on the space, and store the results in a list of two strings
            if username == login_info[0] and password == login_info[1]:
                print("Correct credentials!")
                return True, username
        print("Incorrect credentials.")
        return False


################################################################################
# login page
################################################################################
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
res = False
usr_name = None
Count_book_dict = dict()

library = Library({'Introduction to Python': [
                  1, 'Samuel S Anthony', 'H120', '23-03-2011', '234']}, 'BITS')
# content list of book details of all books
# book_name, quantity, author, rack, publish_date, pages
catalog = Catalog()
while (res == False):
    print()
    print('Please login to continue:-')
    print('1. Staff Login\n2. Student Login\n3. Register')
    print()
    inp = input('Enter choice:- ')
    while True:
        if inp in ['1', '2', '3']:
            break
        print()
        print('please enter a valid input...')
        inp = input('Enter choice:- ')
    post = None
    if inp in '1':
        try:
            res, usr_name = login('staff')
            post = 'staff'
            print()
        except:
            inp = input('Have u registered yet (y/n):- ').lower()
            while True:
                if inp in ['y', 'yes']:
                    print('Enter correct username or password')
                    break
                elif inp in ['n', 'no']:
                    print('User has not registerd yet....')
                    break
                print()
                print('please enter a valid input...')
                inp = input('Have u registered yet:- ').lower()
            continue
    elif inp == '2':
        try:
            res, usr_name = login('student')
            post = 'student'
            print()
        except:
            print()
            inp = input('Have u registered yet (y/n):- ').lower()
            while True:
                if inp in ['y', 'yes']:
                    print('Enter correct username or password')
                    break
                elif inp in ['n', 'no']:
                    print('User has not registerd yet....')
                    break
                print()
                print('please enter a valid input...')
                inp = input('Have u registered yet:- ').lower()
            continue
    else:
        post, usr_name = register()
        res = True
        print()
################################################################################
# read books in stocks.txt
################################################################################
    try:
        file = open("stock.txt", 'r')
        lines = file.readlines()
        lines = [x.strip("\n") for x in lines]
        file.close()
        # print(lines)
        # content list of book details of all books
        # book_name, quantity, author, rack, publish_date, pages

        for book in lines:
            bd = book.split('\t')  # book details
            # print(bd)
            if bd[0] in Count_book_dict and Count_book_dict[bd[0]][1] == bd[2]:
                Count_book_dict[bd[0]][0] += 1
            else:
                Count_book_dict[bd[0]] = {int(bd[1]), bd[2], bd[3], bd[4], bd[5]}
                # print(Count_book_dict)
        # print(Count_book_dict)
        library = Library(Count_book_dict, 'BITS')

    except:
        if post == 'student':
            print('Sorry no books in the library yet!!')
            print('Ask library Staff to upload books....')
            print()
            print('Thanks for visiting Library Portal!')
            sys.exit()
################################################################################
# task by students
################################################################################
    while True:
        # print(usr_name)
        if post == 'student':
            mem = None
            file = open('student_file.txt', 'r')
            lines = file.readlines()
            lines = [x.strip('\n') for x in lines]
            file.close()
            # print(lines)
            for i in range(len(lines)):
                ind = 0
                ls = (lines[i].split('\t'))
                if ls[0] == usr_name:
                    mem = Member(ls[0], ls[1], ls[3], ls[4], ls[5], ls[6], ls[7])
            print()
            print('PLease choose option from following list :-')
            print()
            print("1.", "display_books")
            print("2.", "lend_book")
            print("3.", "return_book")
            print("4.", "pay_fine")
            print("5.", "search book by name")
            print("6.", "search book by author")
            print()
            user_choice = input('Enter Choice:- ')
            if user_choice not in ['1', '2', '3', '4', '5', '6']:
                print('Please enter correct choice...')
                continue
            else:
                user_choice = int(user_choice)
                if user_choice == 1:
                    print('We have following books in {} library'.format(library.name))
                    library.display_books()
                    print("\n")
                elif user_choice == 5:
                    book_name = input('Enter the name of the book: ')
                    catalog.searchByName(book_name)
                    print()
                elif user_choice == 6:
                    author = input('Enter the author of the book: ')
                    catalog.searchByAuthor(author)
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
    ################################################################################
    # tasks by librarian staff
    ################################################################################
        elif post == 'staff':
            mem = None
            file = open('staff_file.txt', 'r')
            lines = file.readlines()
            lines = [x.strip('\n') for x in lines]
            file.close()
            # print(lines)
            for i in range(len(lines)):
                ind = 0
                ls = (lines[i].split('\t'))
                if ls[0] == usr_name:
                    mem = librarian(ls[0], ls[1], ls[3], ls[4], ls[5], ls[6], ls[7])
            # book_name, quantity, author, rack, publish_date, pages
            print("\nlibrarian_tasks")
            print("1.", "add_book")
            print("2.", "remove_book")
            print()
            user_choice = input('Enter choice:- ')
            if user_choice not in ['1', '2']:
                print('Please enter correct choice...')
                continue
            else:
                if user_choice == '1':
                    print()
                    book_name = input('Enter the name of book u want to add:- ').lower()
                    quantity = int(input('Enter no of books to add:- '))
                    author = input('Enter the author of the book:- ').lower()
                    rack = input('Enter the rack number:- ')
                    publish_date = input('Enter the publish date of the book (d/m/Y):- ')
                    pages = input('Enter no of pages in the book:- ')
                    mem.add_book(book_name, quantity, author, rack, publish_date, pages)
                    file = open("stock.txt", "a")
                    file.write(book_name)
                    file.write("\t")
                    file.write(str(quantity))
                    file.write("\t")
                    file.write(author)
                    file.write("\t")
                    file.write(rack)
                    file.write("\t")
                    file.write(publish_date)
                    file.write("\t")
                    file.write(pages)
                    file.write("\n")
                    file.close()
                elif user_choice == '2':
                    print()
                    book_name = input('Enter the name of book u want to add:- ')
                    quantity = int(input('Enter no of books to add:- '))
                    author = input('Enter the author of the book:- ')
                    rack = input('Enter the rack number:- ')
                    publish_date = input('Enter the publish date of the book:- ')
                    pages = input('Enter no of pages in the book:- ')
                    mem.removeBook(book_name, quantity, author, rack, publish_date, pages)
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
