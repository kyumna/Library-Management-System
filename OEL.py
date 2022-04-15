import sys
def home_page():
    print('''Login As:
1)User
2)Administrator
3)Exit''')
    login_as = int(input('Enter Your Choice :'))
    if login_as<1 or login_as>3:
        print('Invalid Entry!!!')
        home_page()
    else:
        if login_as == 1:
            us=user()
            inv=Library()
            print('''1)Login to your account
2)Create an account''')
            while True:
                choice = input('enter your choice : ')
                if choice < '1' or choice > '2':
                    print('Invalid entry!!!')
                else:
                    break
            if choice == '2':
                us.create_account()
            if choice == '1':
                inv.login()
                inv.read_from_file()
                inv.features()
        if login_as==2:
            a = Librarian()
        if login_as==3:
            sys.exit(0)

class user():                                                        #CLASS USER
    dic = {}

    current_borrows_all_users={}

# Reading user information from the file
    def __init__(self):
        self.user_name=None

    def write_current_borrowed_books(self,lst2 ,user_name, obj=None):
        f = open('current_borrows.txt', 'w')
        lst = user.current_borrows_all_users.get(user_name)
        if user.current_borrows_all_users.get(user_name) == None:
            user.current_borrows_all_users.update({user_name: lst2})
        else:
            user.current_borrows_all_users.pop(user_name)
            user.current_borrows_all_users.update({user_name: lst2})
        for j in user.current_borrows_all_users.items():
            j = list(j)
            f.write(f'{j}\n')
        f.close()

    def read_current_borrowed_books(self,user_name,obj=None):
        f=open('current_borrows.txt','a+')
        f.seek(0)
        for i in f:
            lst=eval(i)
            user.current_borrows_all_users.update({lst[0]:lst[1]})
        if user.current_borrows_all_users.get(user_name)==None:
            return []
        else:
            lst1=user.current_borrows_all_users.get(user_name)
            return lst1
        f.close()

    def read_user_info(self,obj=None):
        if obj==None:
            obj=self
        f = open('user_admin.txt', 'a+')
        f.seek(0)
        for i in f:
            lst = eval(i)
            user.dic.update({lst[0]: lst[1]})
        f.close()

    def create_account(self):
        d = {}
        lst = []
        self.read_user_info()
        while True:
            try:  # EXCEPTION HANDLING
                f_name = input('Enter your first name in block letters :')
                if f_name.isupper() == False:
                    raise Exception
                break
            except:
                print('Enter name in block letters!!!')
        while True:
            try:  # EXCEPTION HANDLING
                l_name = input('Enter your last name in block letters :')
                if l_name.isupper() == False:
                    raise Exception
                break
            except:
                print('Enter name in block letters!!!')

        user_name = input('Enter user name :')
        while True:
            if user_name in user.dic:
                user_name = input('Enter another user name :')
            else:
                break
        DOB = input('Enter your date of birth :')
        phone_number = input('Enter your phone number :')
        city = input('Enter your city :')
        address = input('Enter your address :')
        email = input('Enter your email address :')
        password = input('Enter your password :')
        print('PROCESSING...')
        lst = [f_name, l_name, DOB, phone_number, city, address, email, password]
        d = {user_name: lst}
        f = open('user_admin.txt', 'w')
        user.dic.update(d)
        for j in user.dic.items():
            j = list(j)
            f.write(f"{j}\n")
        f.close()
        home_page()

class Library():                                         # CLASS Library
    books = []
    unit_price = {}
    stock = {}
    author_name={}
    publication_date={}
    subject={}

# Initializing instance variables

    def __init__(self):
        self.u=user()
        self.borrows=None
        self.lst=[]

    def login(self):
        '''it reads the file and appends it to the dictionary '''
        self.u.read_user_info(self)
        while True:
            try:  # EXCEPTION HANDLING

                self.user_name = input('Enter Username :')
                if self.user_name not in user.dic:
                    raise Exception
                break
            except:
                print('Incorrect Username!!!')
        while True:
            self.password = input('Enter Password :')
            if self.password == user.dic.get(self.user_name)[7]:
                self.borrows = self.u.read_current_borrowed_books(self.user_name)
                print('LOGGING IN...')
                print('HI', str(user.dic.get(self.user_name)[0]), str(user.dic.get(self.user_name)[1]))
                break
            else:
                print('Incorrect password!!!')

    def features(self):
        print('''Select from the following option:
1)Borrow A book
2)Display All Available Books
3)View Your Current Borrowed Books
4)Renew A Book
5)Return a book
6)Search a book
7)Sort Books
8)Logout''')
        choice=int(input('Enter Your Choice:'))
        if choice<1 or choice>8:
            print('Invalid entry!!!')
            self.features()
        else:
            if choice == 1:
                self.display()
                self.select_book()
            if choice==2:
                self.display()
                self.features()
            if choice == 3:
                self.display_borrowed_books()
                self.features()
            if choice==4:
                self.renew_a_book()
                self.features()
            if choice==5:
                self.return_book()
                self.features()
            if choice==6:
                self.search()
                self.features()
            if choice ==7:
                self.merge_sort(Library.books)
                self.display()
                input("Press Enter To Continue...")
                self.features()
            if choice == 8:
                self.logout()
                home_page()

    def read_from_file(self):
        details = open('stock.txt', 'r')

        # First line of the file is number of items

        number_of_items = int((details.readline()).rstrip("\n"))
        for i in range(0, number_of_items):
            line = (details.readline()).rstrip("\n")
            Library.books.append(line)

        # Adding author name to dictionary

        for i in range(0, number_of_items):
            line = (details.readline()).rstrip("\n")
            o1, o2 = line.split('#')
            o1 = str(o1)
            o2 = str(o2)
            Library.author_name.update({o1: o2})

            #adding price to dictionary

        for i in range(0, number_of_items):
            line = (details.readline()).rstrip('\n')
            o1, o2 = line.split("#")
            o1 = str(o1)
            o2 = str(o2)
            Library.unit_price.update({o1: o2})

        # Adding stock dictioanry

        for i in range(0, number_of_items):
            line = (details.readline()).rstrip('\n')
            o1, o2 = line.split("#")
            o1 = str(o1)
            o2 = str(o2)
            Library.stock.update({o1: o2})

        for i in range(0, number_of_items):
            line = (details.readline()).rstrip('\n')
            o1, o2 = line.split("#")
            o1 = str(o1)
            o2 = str(o2)
            Library.publication_date.update({o1: o2})

        for i in range(0, number_of_items):
            line = (details.readline()).rstrip('\n')
            o1, o2 = line.split("#")
            o1 = str(o1)
            o2 = str(o2)
            Library.subject.update({o1: o2})

        details.close()
        return Library.books

    def update_file(self,num):
        details = open('stock.txt', 'w')
        details.write(str(num) + '\n')
        for i in Library.books:
            details.write(str(i)+'\n')
        for i in Library.author_name:
            details.write(str(i) + '#' + str(Library.author_name.get(i)) + '\n')
        for i in Library.unit_price:
            details.write(str(i) + '#' + str(Library.unit_price.get(i)) + '\n')
        for i in Library.stock:
            details.write(str(i) + '#' + str(Library.stock.get(i)) + '\n')
        for i in Library.publication_date:
            details.write(str(i) + '#' + str(Library.publication_date.get(i)) + '\n')
        for i in Library.subject:
            details.write(str(i) + '#' + str(Library.subject.get(i)) + '\n')
        details.close()

    def display(self):
        details = open('stock.txt', 'r')
        count = int((details.readline()).rstrip("\n"))
        print('DISPLAYING ALL BOOKS...')
        print("\n")
        a = 'Book Name'
        b='Author Name'
        d='Subject'
        e='Publication Date'
        c = 'Price'
        print(f'{a:^20}{b:^20}{d:^20}{e:^20}{c:^20}')
        print()
        for i in range(0,count ):
            print(
                f'{Library.books[i]:^20}{Library.author_name.get(Library.books[i]):^20}'
                f'{Library.subject.get(Library.books[i]):^20}{Library.publication_date.get(Library.books[i]):^20}{Library.unit_price.get(Library.books[i]):^20}')

    def select_book(self):
        selection = int(input('How many books do you want to borrow?'))
        print("Enter book names one by one : ")
        for i in range(0,selection):
            selected_book=str(input("Enter name of the book : "))
            if selected_book in self.borrows:
                print("You have already borrowed this book!!!")
                continue
            if selected_book not in Library.books or Library.stock.get(selected_book)==0:
                print("The book is not available at the moment\n Do you want to reserve it fpr future?[y/n]")
                desicion=str(input("Enter your choice : "))
                if desicion=='y' or desicion=='Y':
                    self.reserve_books(selected_book)
                    print("RESERVING BOOK...")
                    input("Press Enter To Continue...")
                    pass
                else:
                    continue
            else:
                self.lst.append(selected_book)
        shopping=input("Do you want to continue borrowing books [y/n] : ")
        if shopping=="y" or shopping=="Y":
            self.select_book()
        else:
                    if len(self.lst)!=0:
                        stock_update=int(Library.stock.get(selected_book))
                        stock_update-=1
                        stock_update=str(stock_update)
                        Library.stock.pop(selected_book)
                        Library.stock.update({selected_book:stock_update})
                        self.update_file(len(Library.books))
                        for o in self.lst:
                            self.borrows.append(o)
                        self.u.write_current_borrowed_books(self.borrows,self.user_name)
                        print(self.lst)
                        self.checkout(self.lst)
                        self.lst=[]
        self.features()

    def display_borrowed_books(self):
        if self.borrows==None or self.borrows==[]:
            print("You have not borrowed any books!!!")
        else:
            print("DISPLAYING YOUR BORROWED BOOKS...")
            a="BOOKS"
            b="AUTHOR NAME"
            c="PRICE"
            d="PUBLICATION DATE"
            e="SUBJECT"
            print(f'{a:^20}{b:^20}{d:^20}{e:^20}{c:^20}')
            print()
            for i in self.borrows:
                print(f'{i:^20}{Library.author_name.get(i):^20}{Library.publication_date.get(i):^20}'
                      f'{Library.subject.get(i):^20}{Library.unit_price.get(i):^20}')
        input("Press Enter to continue...")

    def renew_a_book(self):
        book_name=input("Enter name of the book you want to renew : ")
        if book_name in self.borrows:
            print("Your book is renewed!!!")
        else:
            print("You don't have this book in your borrowed books!!!")
        input("Press Enter to continue...")

    def return_book(self):
        book_return=str(input("Enter the name of the book you want to return : "))
        if book_return in self.borrows:
            index=self.borrows.index(book_return)
            self.borrows.pop(index)
            quantity=int(self.stock.get(book_return))
            quantity+=1
            self.stock.pop(book_return)
            self.stock.update({book_return:quantity})
            self.update_file(len(Library.books))
            self.u.write_current_borrowed_books(self.borrows,self.user_name)
        else:
            print("You don't have this book in your borrowed books!!!")
        input("Press Enter To Continue...")
    def checkout(self,lst):
        if lst==[]:
            print("You don't have any books!!!")
        else:
            print("DISPLAYING YOUR BORROWED BOOKS...")
            a = "BOOKS"
            b = "AUTHOR NAME"
            c = "PRICE"
            d = "PUBLICATION DATE"
            e = "SUBJECT"
            print(f'{a:^20}{b:^20}{d:^20}{e:^20}{c:^20}')
            print()
            for i in lst:
                print(f'{i:^20}{Library.author_name.get(i):^20}{Library.publication_date.get(i):^20}'
                      f'{Library.subject.get(i):^20}{Library.unit_price.get(i):^20}')
            total=0
            for i in lst:
                temp=int(Library.unit_price.get(i))
                total+=temp
            print("YOUR TOTAL BILL IS :",total,"Rs.")
            print('CHECKING OUT...')
            input("Press Enter To Continue...")
            self.features()

    def merge_sort(self,arr):

        if len(arr) <= 1:
            return
        mid = int((0 + len(arr)) / 2)
        left = arr[:mid]
        right = arr[mid:]
        self.merge_sort(left)
        self.merge_sort(right)
        self.merge_two_sorted_lists(left, right, arr)

    def merge_two_sorted_lists(self,a, b, arr):
        len_a = len(a)
        len_b = len(b)
        i = j = k = 0
        while i < len_a and j < len_b:
            if a[i] <= b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
        while i < len_a:
            arr[k] = a[i]
            i += 1
            k += 1

        while j < len_b:
            arr[k] = b[j]
            j += 1
            k += 1

    def search(self):
        print("How do you want to search a book?\n1)By Author Name\n2)By Book Name\n3)BySubject\n4)ByPublication Date")
        choice=int(input("Enter your choice : "))
        if choice==1:
            auth=input("Enter name of book author you want to search : ")
            keys=list(Library.author_name.keys())
            val=list(Library.author_name.values())
            lst1=[]
            for i in val:
                if auth == i:
                    key = val.index(auth)
                    val.pop(key)
                    lst1.append(keys[key])
                    keys.pop(key)
        if choice==2:
            searching=input("Enter name of the book you want : ")
            lst1=[]
            if searching in Library.books:
                lst1.append(searching)
        if choice==3:
            subject=input("Enter the subject of the book you want to search : ")
            keys=list(Library.subject.keys())
            val=list(Library.subject.values())
            lst1=[]
            for i in val:
                if subject ==i:
                    key=val.index(subject)
                    val.pop(key)
                    lst1.append(keys[key])
                    keys.pop(key)
        if choice==4:
            date=input("Enter publication date of the book you want to search : ")
            keys = list(Library.publication_date.keys())
            val = list(Library.publication_date.values())
            lst1 = []
            for i in val:
                if date == i:
                    key = val.index(date)
                    val.pop(key)
                    lst1.append(keys[key])
                    keys.pop(key)
        if lst1!=[]:
            a = "BOOKS"
            b = "AUTHOR NAME"
            c = "PRICE"
            d = "PUBLICATION DATE"
            e = "SUBJECT"
            print(f'{a:^20}{b:^20}{d:^20}{e:^20}{c:^20}')
            print()
            for j in lst1:
                print(
                    f'{j:^20}{Library.author_name.get(j):^20}{Library.publication_date.get(j):^20}{Library.subject.get(j):^20}{Library.unit_price.get(j):^20}')

        else:
            print("No Book Found")
        input("Press Enter To Continue...")

    def reserve_books(self,book):
        if self.stock.get(book)!=0:
            self.borrows.append(book)
        print("The book will be added to your borowed books as soon as it is available!!!")

    def logout(self):
        self.borrows=None
        Library.stock={}
        Library.books=[]
        Library.unit_price={}
        Library.author_name={}
        Library.publication_date={}
        Library.subject={}
        user.dic={}
        user.current_borrows_all_users={}

class Librarian(Library,user):
    def __init__(self):
        self.user_list=[]
        super().read_from_file()
        self.check_password()

    def check_password(self):
        super().read_user_info()
        while True:
                self.name = input('Enter Admin name :')
                if self.name not in user.dic:
                    print('Invalid Username!!!')
                else:
                    break
        while True:
            self.password = input('Enter Password :')
            if self.password!=user.dic.get(self.name)[7]:
                print('Wrong Password!!!')
            else:
                print('LOGGING IN...')
                break
        self.display_admin_operations()
    def display_admin_operations(self):
        print('''What do you want to do:
1)Add Stock
2)Update Books
3)Add books
4)Cancel Membership
5)Search Books
6)Sort Books
7)Display All Members
8)Logout''')
        operation = int(input('Enter your choice:'))
        if operation < 1 or operation > 8:
            print('invalid choice!!!')
            self.display_admin_operations()
        else:
            if operation == 1:
                self.Add_stock()
            if operation == 2:
                self.update_books()
                self.display_admin_operations()
            if operation==3:
                self.add_book()
                self.display_admin_operations()
            if operation == 4:
                self.cancel_membership()
                self.display_admin_operations()
            if operation==5:
                super().search()
                self.display_admin_operations()
            if operation==6:
                super().merge_sort(Library.books)
                super().display()
                input("Press Enter To Continue...")
                self.display_admin_operations()
            if operation == 7:
                self.display_users()
                self.display_admin_operations()
            if operation == 8:
                super().logout()
                home_page()

    def Add_stock(self):
        super().read_from_file()
        book = input('Enter book name :')
        stock = int(input('Enter stock:'))
        total_stock = stock +int( Library.stock.get(book))
        super().stock.update({book: total_stock})
        super().update_file(len(Library.books))
        print('Stock Added Successfuly')
        input('Press enter to continue...')
        self.display_admin_operations()
    def update_books(self):
        print("What do you want to update?\n1)Author name\n2)Price\n3)Publication Date\n4)Subject")
        choice=int(input("Enter your choice : "))
        if choice==2:
            name=input("Enter book name : ")
            if name in Library.books:
                new=input("Enter new price : ")
                Library.unit_price.pop(name)
                Library.unit_price.update({name:new})
                print("Price has been updated!!!")
            else:
                print("No book with this name found")
                self.update_books()
        if choice==1:
            name = input("Enter book name : ")
            if name in Library.books:
                new = input("Enter updated author name : ")
                Library.author_name.pop(name)
                Library.author_name.update({name: new})

                print("Author name has been updated!!!")
            else:
                print("No book with this name found")
                self.update_books()

        if choice==3:
            name = input("Enter book name : ")
            if name in Library.books:
                new = input("Enter updated publication date : ")
                Library.publication_date.pop(name)
                Library.publication_date.update({name: new})
                print("Publication date has been updated!!!")
            else:
                print("No book with this name found")
                self.update_books()


        if choice==4:
            name = input("Enter book name : ")
            if name in Library.books:
                new = input("Enter updated Subject : ")
                Library.subject.pop(name)
                Library.subject.update({name: new})
                print("Subject has been updated!!!")
            else:
                print("No book with this name found")
                self.update_books()
        super().update_file(len(Library.books))
        input('Press enter to continue...')
    def users(self):
        f=open('user_admin.txt','a+')
        f.seek(0)
        for i in f:
            lst=eval(i)
            self.user_list.append(lst[0])
        self.user_list.pop(0)

    def cancel_membership(self):
        user_no = 0
        self.users()
        print()
        print('Displaying All Members')
        print()
        print('**********************************************************')
        print()
        for i in self.user_list:
            user_no += 1
            print('Member No.', user_no)
            print(i)
            print()
            print('******************************************************')
            print()
        print('which user do you want to delete?\nEnter user name :', end='')
        user_name = input()
        super().read_current_borrowed_books(user_name)

        if user_name in self.user_list:
            indices = self.user_list.index(user_name)
            self.user_list.pop(indices)
            user.dic.pop(user_name)


            if user_name in user.current_borrows_all_users:
                user.current_borrows_all_users.pop(user_name)
                self.write_current_borrowed_books()

            f = open('user_admin.txt', 'w')
            for j in user.dic.items():
                j = list(j)
                f.write(f"{j}\n")
            f.close()
            print('Membership Cancelled Successfuly!!!')
            input("Press Enter to continue...")
            print()
            self.user_list = []

    def write_current_borrowed_books(self):                                                   #METHOD OVERRIDING
        e=open('current_borrows.txt','w')
        for o in user.current_borrows_all_users.items():
            o=list(o)
            e.write(f'{o}\n')
        e.close()

    def display_users(self):

        users = 1
        for j in user.dic:
            if j == 'kyumna14':
                pass
            else:
                print('User No.', users)
                print('First Name :', user.dic.get(j)[0])
                print('Last Name :', user.dic.get(j)[1])
                print('Date Of Birth :', user.dic.get(j)[2])
                print('Phone Number :', user.dic.get(j)[3])
                print('City :', user.dic.get(j)[4])
                print('Address :', user.dic.get(j)[5])
                print('Email :', user.dic.get(j)[6])
                print('********************************************')
                users += 1
        input('press enter to continue...')
        self.display_admin_operations()

    def add_book(self):
        old_books_count=len(Library.books)
        count=int(input("How many books do you want to add : "))
        for i in range(0,count):
            name=input("Enter book name : ")
            author=input("Enter author name : ")
            date=input("Enter publication date : ")
            subject=input("Enter book subject : ")
            price=input("Enter book price : ")
            stock=input("Enter book stock : ")
            Library.author_name.update({name:author})
            Library.books.append(name)
            Library.stock.update({name:stock})
            Library.publication_date.update({name:date})
            Library.subject.update({name:subject})
            Library.unit_price.update({name:price})
            new_books_count=old_books_count+count
            super().update_file(new_books_count)

print("NOTE:\nAdmin User Name and Password is fixed : \nUSER NAME:kyumna14\nPASSWORD:yumna1")
home_page()